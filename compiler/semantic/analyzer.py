from __future__ import annotations
from typing import Optional

from compiler.ast.nodes import (
    AccessMod, ArrayLiteral, ArrayType, BaseType, BinaryExpr, BoolLiteral,
    Break, CodeBlock, Continue, Defer, DoWhileLoop, Expr,
    FieldAccessor, FloatLiteral, ForInLoop, ForLoop, FuncCall, FuncDecl,
    GlobalVarDecl, IfElse, IndexAccessor, InterfaceDecl, InterfaceField,
    IntLiteral, MapField, MapLiteral, MapType, MultiReturnType, MultiVarAssign,
    MultiVarDecl, NoAcsModeVarDecl, NullLiteral, ParamDecl, PostfixExpr,
    Prog, Return, SetLiteral, SetType, SingleReturnType, StringLiteral,
    StructLiteral, TernaryExpr, Type, UnaryExpr, UserType,
    VarAssign, VarDecl, VarRef, VoidReturnType, WhileLoop, ReturnType,
)
from compiler.errors.errors import SemanticError
from compiler.semantic.builtins import builtin_symbols
from compiler.semantic.symbols import Symbol, SymbolKind, SymbolTable
from compiler.semantic.type_table import TypeTable
from compiler.semantic.type_ops import (
    binary_result_type, fmt_type, is_assignable, is_numeric, unary_result_type,
)


class SemanticAnalyzer:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.symbols = SymbolTable()
        self.types = TypeTable()
        self.errors: list[SemanticError] = []
        self._loop_depth: int = 0
        self._current_return_type: Optional[ReturnType] = None
        self._current_node = None  # last-seen AST node; used for error positions

    def analyze(self, prog: Prog) -> tuple[SymbolTable, TypeTable, list[SemanticError]]:
        for sym in builtin_symbols():
            self.symbols.define(sym)
        self._pre_pass(prog)
        self._check_prog(prog)
        return self.symbols, self.types, self.errors
    def _pre_pass(self, prog: Prog) -> None:
        """Hoist all top-level FuncDecl and InterfaceDecl into global scope
        before the main walk, enabling forward references."""
        for stmt in prog.stmts:
            self._current_node = stmt
            match stmt:
                case FuncDecl(name=name):
                    sym = Symbol(
                        name=name,
                        kind=SymbolKind.FUNCTION,
                        type=None,
                        is_mutable=False,
                        decl_node=stmt,
                    )
                    if not self.symbols.define(sym):
                        self._error(f"'{name}' already declared", "RedefinitionError")
                case InterfaceDecl(name=name):
                    sym = Symbol(
                        name=name,
                        kind=SymbolKind.INTERFACE,
                        type=None,
                        is_mutable=False,
                        decl_node=stmt,
                    )
                    if not self.symbols.define(sym):
                        self._error(f"'{name}' already declared", "RedefinitionError")

    def _check_prog(self, prog: Prog) -> None:
        for stmt in prog.stmts:
            match stmt:
                case FuncDecl():
                    self._check_func_decl(stmt, nested=False)
                case InterfaceDecl():
                    self._check_interface_decl(stmt)
                case GlobalVarDecl():
                    self._check_global_var_decl(stmt)
                case _:
                    pass

    def _check_func_decl(self, node: FuncDecl, nested: bool) -> None:
        if nested:
            sym = Symbol(
                name=node.name,
                kind=SymbolKind.FUNCTION,
                type=None,
                is_mutable=False,
                decl_node=node,
            )
            if not self.symbols.define(sym):
                self._error(f"'{node.name}' already declared in this scope", "RedefinitionError")

        prev_return_type = self._current_return_type
        self._current_return_type = node.return_type

        self.symbols.enter_scope()
        for param in node.params:
            self._check_param_decl(param)
        self._check_code_block(node.body)
        self.symbols.exit_scope()

        self._current_return_type = prev_return_type

    def _check_param_decl(self, node: ParamDecl) -> None:
        sym = Symbol(
            name=node.name,
            kind=SymbolKind.PARAMETER,
            type=node.type_ann,
            is_mutable=True,
            decl_node=node,
        )
        if not self.symbols.define(sym):
            self._error(f"duplicate parameter '{node.name}'", "RedefinitionError")

    def _check_interface_decl(self, node: InterfaceDecl) -> None:
        for parent_name in node.extends:
            parent_sym = self.symbols.lookup(parent_name)
            if parent_sym is None:
                self._error(
                    f"interface '{node.name}' extends unknown '{parent_name}'",
                    "InterfaceError",
                )
            elif parent_sym.kind != SymbolKind.INTERFACE:
                self._error(
                    f"'{parent_name}' is not an interface",
                    "InterfaceError",
                )

        if self._has_cycle(node.name, set()):
            self._error(
                f"circular inheritance involving '{node.name}'",
                "InterfaceError",
            )

    def _has_cycle(self, name: str, visited: set[str]) -> bool:
        if name in visited:
            return True
        visited.add(name)
        sym = self.symbols.lookup(name)
        if sym is None or sym.kind != SymbolKind.INTERFACE:
            return False
        iface: InterfaceDecl = sym.decl_node  # type: ignore[assignment]
        return any(self._has_cycle(p, visited) for p in iface.extends)

    def _collect_all_fields(
        self, iface_name: str, _visited: Optional[set[str]] = None
    ) -> dict[str, InterfaceField]:
        """Recursively collect all fields (own + inherited), own fields win."""
        if _visited is None:
            _visited = set()
        if iface_name in _visited:
            return {}
        _visited.add(iface_name)

        sym = self.symbols.lookup(iface_name)
        if sym is None or sym.kind != SymbolKind.INTERFACE:
            return {}

        iface: InterfaceDecl = sym.decl_node  # type: ignore[assignment]
        fields: dict[str, InterfaceField] = {}
        for parent in iface.extends:
            fields.update(self._collect_all_fields(parent, _visited))
        for f in iface.fields:
            fields[f.name] = f
        return fields

    def _check_code_block(self, node: CodeBlock) -> None:
        for stmt in node.func_stmts:
            self._check_func_stmt(stmt)

    def _check_func_stmt(self, node) -> None:
        self._current_node = node
        match node:
            case FuncDecl():
                self._check_func_decl(node, nested=True)
            case VarDecl():
                self._check_var_decl(node)
            case MultiVarDecl():
                self._check_multi_var_decl(node)
            case NoAcsModeVarDecl():
                self._check_no_acs_mode_var_decl(node)
            case VarAssign():
                self._check_var_assign(node)
            case MultiVarAssign():
                self._check_multi_var_assign(node)
            case IfElse():
                self._check_if_else(node)
            case WhileLoop():
                self._check_while_loop(node)
            case DoWhileLoop():
                self._check_do_while_loop(node)
            case ForLoop():
                self._check_for_loop(node)
            case ForInLoop():
                self._check_for_in_loop(node)
            case Return():
                self._check_return(node)
            case Break():
                self._check_break()
            case Continue():
                self._check_continue()
            case Defer(expr=e):
                self._infer_expr(e)
            case Expr():
                self._infer_expr(node)

    def _check_global_var_decl(self, node: GlobalVarDecl) -> None:
        self._current_node = node
        val_type = self._infer_expr(node.val)

        if node.type_ann is not None:
            if isinstance(node.type_ann, UserType) and isinstance(node.val, StructLiteral):
                self._check_struct_satisfies(node.type_ann.name, node.val)
            elif not isinstance(node.val, NullLiteral) and not is_assignable(node.type_ann, val_type):
                self._error(
                    f"cannot assign '{fmt_type(val_type)}' to '{fmt_type(node.type_ann)}'",
                    "TypeError",
                )
            declared_type = node.type_ann
        else:
            if isinstance(node.val, StructLiteral):
                declared_type = self._make_anon_struct_type(node.name, node.val)
            else:
                declared_type = val_type

        sym = Symbol(
            name=node.name,
            kind=SymbolKind.VARIABLE,
            type=declared_type,
            is_mutable=(node.access_mod == AccessMod.LET),
            decl_node=node,
        )
        if not self.symbols.define(sym):
            self._error(f"'{node.name}' already declared in this scope", "RedefinitionError")

    def _check_var_decl(self, node: VarDecl) -> None:
        val_type = self._infer_expr(node.val)

        if node.type_ann is not None:
            if isinstance(node.type_ann, UserType) and isinstance(node.val, StructLiteral):
                self._check_struct_satisfies(node.type_ann.name, node.val)
            elif not isinstance(node.val, NullLiteral) and not is_assignable(node.type_ann, val_type):
                self._error(
                    f"cannot assign '{fmt_type(val_type)}' to '{fmt_type(node.type_ann)}'",
                    "TypeError",
                )
            declared_type = node.type_ann
        else:
            if isinstance(node.val, StructLiteral):
                declared_type = self._make_anon_struct_type(node.name, node.val)
            else:
                declared_type = val_type

        sym = Symbol(
            name=node.name,
            kind=SymbolKind.VARIABLE,
            type=declared_type,
            is_mutable=(node.access_mod == AccessMod.LET),
            decl_node=node,
        )
        if not self.symbols.define(sym):
            self._error(f"'{node.name}' already declared in this scope", "RedefinitionError")

    def _check_multi_var_decl(self, node: MultiVarDecl) -> None:
        func_sym = self.symbols.lookup(node.val.func)
        if func_sym is None:
            self._error(f"undefined function '{node.val.func}'", "NameError")
            return
        if func_sym.kind != SymbolKind.FUNCTION or func_sym.decl_node is None:
            self._error(f"'{node.val.func}' is not callable", "TypeError")
            return

        func_decl: FuncDecl = func_sym.decl_node  # type: ignore[assignment]
        match func_decl.return_type:
            case MultiReturnType(types=rtypes):
                if len(node.names) != len(rtypes):
                    self._error(
                        f"'{node.val.func}' returns {len(rtypes)} values, "
                        f"got {len(node.names)} names",
                        "TypeError",
                    )
                    return
                mutable = node.access_mod == AccessMod.LET
                for name, rtype in zip(node.names, rtypes):
                    sym = Symbol(
                        name=name,
                        kind=SymbolKind.VARIABLE,
                        type=rtype,
                        is_mutable=mutable,
                        decl_node=node,
                    )
                    if not self.symbols.define(sym):
                        self._error(f"'{name}' already declared in this scope", "RedefinitionError")
            case _:
                self._error(
                    f"'{node.val.func}' does not return multiple values",
                    "TypeError",
                )

    def _check_no_acs_mode_var_decl(self, node: NoAcsModeVarDecl) -> None:
        val_type = self._infer_expr(node.val)
        declared_type = node.type_ann if node.type_ann is not None else val_type

        if node.type_ann is not None and not isinstance(node.val, NullLiteral):
            if not is_assignable(node.type_ann, val_type):
                self._error(
                    f"cannot assign '{fmt_type(val_type)}' to '{fmt_type(node.type_ann)}'",
                    "TypeError",
                )

        sym = Symbol(
            name=node.name,
            kind=SymbolKind.VARIABLE,
            type=declared_type,
            is_mutable=True,
            decl_node=node,
        )
        if not self.symbols.define(sym):
            self._error(f"'{node.name}' already declared in this scope", "RedefinitionError")

    def _check_var_assign(self, node: VarAssign) -> None:
        sym = self.symbols.lookup(node.var.name)
        if sym is None:
            self._error(f"undefined name '{node.var.name}'", "NameError")
            return
        # Only block direct reassignment of const; indexed/field mutation is allowed
        # (e.g. `const arr: int[] = [1,2,3]; arr[0] = 9` is valid).
        if not sym.is_mutable and not node.var.accessors:
            self._error(f"cannot assign to const '{node.var.name}'", "TypeError")

        target_type = self._infer_expr(node.var)
        val_type = self._infer_expr(node.val)

        if not isinstance(node.val, NullLiteral) and not is_assignable(target_type, val_type):
            self._error(
                f"cannot assign '{fmt_type(val_type)}' to '{fmt_type(target_type)}'",
                "TypeError",
            )

    def _check_multi_var_assign(self, node: MultiVarAssign) -> None:
        func_sym = self.symbols.lookup(node.val.func)
        if func_sym is None:
            self._error(f"undefined function '{node.val.func}'", "NameError")
            return
        if func_sym.kind != SymbolKind.FUNCTION or func_sym.decl_node is None:
            self._error(f"'{node.val.func}' is not callable", "TypeError")
            return

        func_decl: FuncDecl = func_sym.decl_node  # type: ignore[assignment]
        match func_decl.return_type:
            case MultiReturnType(types=rtypes):
                if len(node.vars) != len(rtypes):
                    self._error(
                        f"'{node.val.func}' returns {len(rtypes)} values, "
                        f"got {len(node.vars)} targets",
                        "TypeError",
                    )
                    return
                for var_ref, rtype in zip(node.vars, rtypes):
                    target_type = self._infer_expr(var_ref)
                    if not is_assignable(target_type, rtype):
                        self._error(
                            f"cannot assign '{fmt_type(rtype)}' to '{fmt_type(target_type)}'",
                            "TypeError",
                        )
            case _:
                self._error(
                    f"'{node.val.func}' does not return multiple values",
                    "TypeError",
                )

    def _check_return(self, node: Return) -> None:
        if self._current_return_type is None:
            self._error("return statement outside function", "ControlFlowError")
            return

        match self._current_return_type:
            case VoidReturnType():
                if node.vals:
                    self._error("void function cannot return a value", "TypeError")
                else:
                    for v in node.vals:
                        self._infer_expr(v)
            case SingleReturnType(type_ann=expected):
                if len(node.vals) != 1:
                    self._error(
                        f"expected 1 return value, got {len(node.vals)}", "TypeError"
                    )
                    for v in node.vals:
                        self._infer_expr(v)
                    return
                val_type = self._infer_expr(node.vals[0])
                if not isinstance(node.vals[0], NullLiteral) and not is_assignable(expected, val_type):
                    self._error(
                        f"return type mismatch: expected '{fmt_type(expected)}', "
                        f"got '{fmt_type(val_type)}'",
                        "TypeError",
                    )
            case MultiReturnType(types=expected_types):
                if len(node.vals) != len(expected_types):
                    self._error(
                        f"expected {len(expected_types)} return values, got {len(node.vals)}",
                        "TypeError",
                    )
                    for v in node.vals:
                        self._infer_expr(v)
                    return
                for i, (val, expected) in enumerate(zip(node.vals, expected_types)):
                    val_type = self._infer_expr(val)
                    if not isinstance(val, NullLiteral) and not is_assignable(expected, val_type):
                        self._error(
                            f"return value {i + 1}: expected '{fmt_type(expected)}', "
                            f"got '{fmt_type(val_type)}'",
                            "TypeError",
                        )

    def _check_break(self) -> None:
        if self._loop_depth == 0:
            self._error("break outside loop", "ControlFlowError")

    def _check_continue(self) -> None:
        if self._loop_depth == 0:
            self._error("continue outside loop", "ControlFlowError")

    def _check_while_loop(self, node: WhileLoop) -> None:
        cond_type = self._infer_expr(node.condition)
        if cond_type != BaseType.BOOL and cond_type != BaseType.ERROR:
            self._error("while condition must be bool", "TypeError")
        self._loop_depth += 1
        self.symbols.enter_scope()
        self._check_code_block(node.body)
        self.symbols.exit_scope()
        self._loop_depth -= 1

    def _check_do_while_loop(self, node: DoWhileLoop) -> None:
        self._loop_depth += 1
        self.symbols.enter_scope()
        self._check_code_block(node.body)
        self.symbols.exit_scope()
        self._loop_depth -= 1
        cond_type = self._infer_expr(node.condition)
        if cond_type != BaseType.BOOL and cond_type != BaseType.ERROR:
            self._error("do-while condition must be bool", "TypeError")

    def _check_for_loop(self, node: ForLoop) -> None:
        self.symbols.enter_scope()
        if node.init is not None:
            self._check_no_acs_mode_var_decl(node.init)
        if node.condition is not None:
            cond_type = self._infer_expr(node.condition)
            if cond_type != BaseType.BOOL and cond_type != BaseType.ERROR:
                self._error("for condition must be bool", "TypeError")
        if node.update is not None:
            from compiler.ast.nodes import VarAssign
            if isinstance(node.update, VarAssign):
                self._check_var_assign(node.update)
            else:
                self._infer_expr(node.update)
        self._loop_depth += 1
        self._check_code_block(node.body)
        self._loop_depth -= 1
        self.symbols.exit_scope()

    def _check_for_in_loop(self, node: ForInLoop) -> None:
        iterable_type = self._infer_expr(node.iterable)

        elem_type: Type
        match iterable_type:
            case ArrayType(element=e):
                elem_type = e
            case SetType(element=e):
                elem_type = e
            case MapType(key=k):
                elem_type = k
            case _:
                elem_type = BaseType.ERROR  # range() or unknown

        self._loop_depth += 1
        self.symbols.enter_scope()
        sym = Symbol(
            name=node.var,
            kind=SymbolKind.VARIABLE,
            type=elem_type,
            is_mutable=False,
            decl_node=node,
        )
        self.symbols.define(sym)
        self._check_code_block(node.body)
        self.symbols.exit_scope()
        self._loop_depth -= 1

    def _check_if_else(self, node: IfElse) -> None:
        cond_type = self._infer_expr(node.condition)
        if cond_type != BaseType.BOOL and cond_type != BaseType.ERROR:
            self._error("if condition must be bool", "TypeError")

        self.symbols.enter_scope()
        self._check_code_block(node.if_body)
        self.symbols.exit_scope()

        for elif_clause in node.elif_clauses:
            elif_cond = self._infer_expr(elif_clause.condition)
            if elif_cond != BaseType.BOOL and elif_cond != BaseType.ERROR:
                self._error("elif condition must be bool", "TypeError")
            self.symbols.enter_scope()
            self._check_code_block(elif_clause.body)
            self.symbols.exit_scope()

        if node.else_body is not None:
            self.symbols.enter_scope()
            self._check_code_block(node.else_body)
            self.symbols.exit_scope()

    def _infer_expr(self, node: Expr) -> Type:
        t = self._infer_expr_inner(node)
        if t is not None:
            self.types.set(node, t)
        return t if t is not None else BaseType.ERROR

    def _infer_expr_inner(self, node: Expr) -> Optional[Type]:
        self._current_node = node
        match node:
            case IntLiteral():
                return BaseType.INT
            case FloatLiteral():
                return BaseType.FLOAT
            case StringLiteral():
                return BaseType.STRING
            case BoolLiteral():
                return BaseType.BOOL
            case NullLiteral():
                return BaseType.ERROR # null sentinel
            case VarRef():
                return self._resolve_var_ref(node)
            case FuncCall():
                return self._infer_func_call(node)
            case BinaryExpr(left=left, op=op, right=right):
                return self._infer_binary(left, op, right)
            case UnaryExpr(op=op, operand=operand):
                return self._infer_unary(op, operand)
            case PostfixExpr(operand=var, op=op):
                return self._infer_postfix(var, op)
            case TernaryExpr(condition=cond, true_expr=t_expr, false_expr=f_expr):
                return self._infer_ternary(cond, t_expr, f_expr)
            case ArrayLiteral(elements=elems):
                return self._infer_array_literal(elems)
            case SetLiteral(elements=elems):
                return self._infer_set_literal(elems)
            case MapLiteral(fields=fields):
                return self._infer_map_literal(fields)
            case StructLiteral(fields=struct_fields):
                for sf in struct_fields:
                    self._infer_expr(sf.val)
                return UserType("__anon__")
            case _:
                return BaseType.ERROR

    def _infer_binary(self, left, op, right) -> Type:
        lt = self._infer_expr(left)
        rt = self._infer_expr(right)
        result = binary_result_type(op, lt, rt)
        if result is None:
            self._error(
                f"operator '{op.value}' not defined for '{fmt_type(lt)}' and '{fmt_type(rt)}'",
                "TypeError",
            )
            return BaseType.ERROR
        return result

    def _infer_unary(self, op, operand) -> Type:
        ot = self._infer_expr(operand)
        result = unary_result_type(op, ot)
        if result is None:
            self._error(
                f"operator '{op.value}' not defined for '{fmt_type(ot)}'",
                "TypeError",
            )
            return BaseType.ERROR
        return result

    def _infer_postfix(self, var, op) -> Type:
        var_type = self._infer_expr(var)
        sym = self.symbols.lookup(var.name)
        if sym is not None and not sym.is_mutable:
            self._error(f"cannot modify const '{var.name}'", "TypeError")
        if not is_numeric(var_type) and var_type != BaseType.ERROR:
            self._error(
                f"'{op.value}' requires a numeric type, got '{fmt_type(var_type)}'",
                "TypeError",
            )
        return var_type

    def _infer_ternary(self, cond, t_expr, f_expr) -> Type:
        cond_type = self._infer_expr(cond)
        if cond_type != BaseType.BOOL and cond_type != BaseType.ERROR:
            self._error("ternary condition must be bool", "TypeError")
        tt = self._infer_expr(t_expr)
        ft = self._infer_expr(f_expr)
        if tt != ft and tt != BaseType.ERROR and ft != BaseType.ERROR:
            self._error(
                f"ternary branches have incompatible types: "
                f"'{fmt_type(tt)}' vs '{fmt_type(ft)}'",
                "TypeError",
            )
        return tt

    def _infer_array_literal(self, elems) -> Type:
        if not elems:
            return ArrayType(BaseType.ERROR)
        types = [self._infer_expr(e) for e in elems]
        first = types[0]
        for i, t in enumerate(types[1:], 1):
            if t != first and t != BaseType.ERROR and first != BaseType.ERROR:
                self._error(f"array element {i} type mismatch: expected '{fmt_type(first)}', got '{fmt_type(t)}'", "TypeError")
        return ArrayType(first)

    def _infer_set_literal(self, elems) -> Type:
        if not elems:
            return SetType(BaseType.ERROR)
        types = [self._infer_expr(e) for e in elems]
        first = types[0]
        for i, t in enumerate(types[1:], 1):
            if t != first and t != BaseType.ERROR and first != BaseType.ERROR:
                self._error(f"set element {i} type mismatch: expected '{fmt_type(first)}', got '{fmt_type(t)}'", "TypeError")
        return SetType(first)

    def _infer_map_literal(self, fields: list[MapField]) -> Type:
        if not fields:
            return MapType(BaseType.ERROR, BaseType.ERROR)
        key_types = [self._infer_expr(f.key) for f in fields]
        val_types = [self._infer_expr(f.val) for f in fields]
        k0, v0 = key_types[0], val_types[0]
        for i, (kt, vt) in enumerate(zip(key_types[1:], val_types[1:]), 1):
            if kt != k0 and kt != BaseType.ERROR and k0 != BaseType.ERROR:
                self._error(f"map key {i} type mismatch", "TypeError")
            if vt != v0 and vt != BaseType.ERROR and v0 != BaseType.ERROR:
                self._error(f"map value {i} type mismatch", "TypeError")
        return MapType(k0, v0)

    def _resolve_var_ref(self, node: VarRef) -> Type:
        sym = self.symbols.lookup(node.name)
        if sym is None:
            self._error(f"undefined name '{node.name}'", "NameError")
            return BaseType.ERROR
        if sym.kind == SymbolKind.INTERFACE:
            self._error(f"'{node.name}' is an interface, not a value", "TypeError")
            return BaseType.ERROR
        if sym.kind == SymbolKind.FUNCTION:
            self._error(f"'{node.name}' is a function — did you mean to call it?", "TypeError")
            return BaseType.ERROR

        base: Type = sym.type if sym.type is not None else BaseType.ERROR
        return self._resolve_accessors(base, node.accessors)

    def _resolve_accessors(self, current: Type, accessors) -> Type:
        for acc in accessors:
            match acc:
                case IndexAccessor(index=idx):
                    acc.type_ann = current
                    if idx is not None:
                        idx_type = self._infer_expr(idx)
                        if idx_type != BaseType.INT and idx_type != BaseType.ERROR:
                            self._error(
                                f"index must be 'int', got '{fmt_type(idx_type)}'",
                                "TypeError",
                            )
                    match current:
                        case ArrayType(element=e):
                            current = e
                        case MapType(value=v):
                            current = v
                        case _ if current == BaseType.STRING:
                            current = BaseType.STRING # string[i] → string (char)
                        case _:
                            if current != BaseType.ERROR:
                                self._error(
                                    f"cannot index into '{fmt_type(current)}'", "TypeError"
                                )
                            return BaseType.ERROR
                case FieldAccessor(field=field_vr):
                    acc.type_ann = current
                    match current:
                        case UserType(name=iname):
                            all_fields = self._collect_all_fields(iname)
                            if field_vr.name not in all_fields:
                                self._error(
                                    f"'{iname}' has no field '{field_vr.name}'", "TypeError"
                                )
                                return BaseType.ERROR
                            field_base = all_fields[field_vr.name].type_ann
                            current = self._resolve_accessors(field_base, field_vr.accessors)
                        case _:
                            if current != BaseType.ERROR:
                                self._error(
                                    f"cannot access field on '{fmt_type(current)}'", "TypeError"
                                )
                            return BaseType.ERROR
        return current

    def _infer_func_call(self, node: FuncCall) -> Type:
        # Always infer arg types (side-effect: record in TypeTable)
        def infer_args():
            for arg in node.args:
                self._infer_expr(arg)


        func_sym = self.symbols.lookup(node.func)
        if func_sym is None:
            self._error(f"undefined function '{node.func}'", "NameError")
            infer_args()
            return BaseType.ERROR

        if func_sym.kind != SymbolKind.FUNCTION:
            self._error(f"'{node.func}' is not callable", "TypeError")
            infer_args()
            return BaseType.ERROR

        if func_sym.decl_node is None:
            # polymorphic builtin (e.g. println) — accept any args, return void
            infer_args()
            return None

        func_decl: FuncDecl = func_sym.decl_node  # type: ignore[assignment]

        if len(node.args) != len(func_decl.params):
            self._error(
                f"'{node.func}' expects {len(func_decl.params)} argument(s), "
                f"got {len(node.args)}",
                "TypeError",
            )

        for i, (arg, param) in enumerate(zip(node.args, func_decl.params)):
            arg_type = self._infer_expr(arg)
            if not isinstance(arg, NullLiteral) and not is_assignable(param.type_ann, arg_type):
                self._error(
                    f"argument {i + 1} of '{node.func}': "
                    f"expected '{fmt_type(param.type_ann)}', got '{fmt_type(arg_type)}'",
                    "TypeError",
                )
        # Infer remaining args if counts differ
        for arg in node.args[len(func_decl.params):]:
            self._infer_expr(arg)

        match func_decl.return_type:
            case SingleReturnType(type_ann=t):
                return t if t is not None else None
            case MultiReturnType():
                # Multi-return used as a single expression — caller must handle
                return None
            case VoidReturnType():
                return None  # void — don't annotate in tree
            case _:
                return None

    def _check_struct_satisfies(self, iface_name: str, struct: StructLiteral) -> None:
        sym = self.symbols.lookup(iface_name)
        if sym is None or sym.kind != SymbolKind.INTERFACE:
            self._error(f"unknown interface '{iface_name}'", "InterfaceError")
            return

        all_fields = self._collect_all_fields(iface_name)
        struct_fields = {sf.name: sf for sf in struct.fields}

        for fname, ifield in all_fields.items():
            if fname not in struct_fields:
                if not ifield.optional:
                    self._error(
                        f"struct literal missing required field "
                        f"'{fname}' of interface '{iface_name}'",
                        "InterfaceError",
                    )
            else:
                got = self._infer_expr(struct_fields[fname].val)
                if not isinstance(struct_fields[fname].val, NullLiteral) and \
                        not is_assignable(ifield.type_ann, got):
                    self._error(
                        f"field '{fname}': expected '{fmt_type(ifield.type_ann)}', "
                        f"got '{fmt_type(got)}'",
                        "TypeError",
                    )

        for fname in struct_fields:
            if fname not in all_fields:
                self._error(
                    f"struct literal has unknown field "
                    f"'{fname}' for interface '{iface_name}'",
                    "InterfaceError",
                )

    def _make_anon_struct_type(self, var_name: str, struct: StructLiteral) -> UserType:
        """Build and register an anonymous interface from an untyped struct literal
        so that field access on the variable resolves correctly."""
        anon_name = f"__struct_{var_name}"
        fields = [
            InterfaceField(
                name=sf.name,
                type_ann=self.types.get(sf.val) or self._infer_expr(sf.val),
                optional=False,
            )
            for sf in struct.fields
        ]
        iface_node = InterfaceDecl(name=anon_name, extends=[], fields=fields)
        sym = Symbol(
            name=anon_name,
            kind=SymbolKind.INTERFACE,
            type=None,
            is_mutable=False,
            decl_node=iface_node,
        )
        self.symbols.define(sym)  # silently overwrite on re-entry (e.g. loops)
        return UserType(anon_name)

    def _error(self, message: str, kind: str) -> None:
        n = self._current_node
        line = n.line if n is not None else 0
        col  = n.col  if n is not None else 0
        loc  = f"{self.filename}:{line}:{col}" if line else self.filename
        self.errors.append(SemanticError(
            kind=kind,
            filename=self.filename,
            line=line,
            column=col,
            message=f"[{kind}] {loc}: {message}",
        ))
