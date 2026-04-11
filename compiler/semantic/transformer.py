"""Type-dependent AST transformation pass.

Runs after SemanticAnalyzer. Mutates the AST in-place:
  1. Fills in inferred type_ann on VarDecl / NoAcsModeVarDecl.
  2. Inserts CastExpr nodes wherever implicit int→float widening occurs:
       - BinaryExpr operands
       - FuncCall arguments
       - Return values
       - VarDecl / VarAssign right-hand sides
"""
from __future__ import annotations
from typing import Optional

from compiler.ast.nodes import (
    ArrayLiteral, BaseType, BinaryExpr, CastExpr, CodeBlock, Defer,
    DoWhileLoop, Expr, FieldAccessor, ForInLoop, ForLoop,
    FuncCall, FuncDecl, IfElse, IndexAccessor, MapLiteral,
    NoAcsModeVarDecl, PostfixExpr, Prog, Return, ReturnType,
    SetLiteral, SingleReturnType, StructLiteral, TernaryExpr, Type,
    UnaryExpr, VarAssign, VarDecl, VarRef, VoidReturnType, WhileLoop,
)
from compiler.semantic.symbols import SymbolKind, SymbolTable
from compiler.semantic.type_table import TypeTable


class ASTTransformer:
    def __init__(self, types: TypeTable, symbols: SymbolTable) -> None:
        self.types = types
        self.symbols = symbols
        self._current_return_type: Optional[ReturnType] = None

    def transform(self, prog: Prog) -> None:
        for stmt in prog.stmts:
            self._stmt(stmt)

    def _stmt(self, node) -> None:
        match node:
            case FuncDecl():
                self._func_decl(node)
            case VarDecl():
                self._var_decl(node)

    def _func_decl(self, node: FuncDecl) -> None:
        prev = self._current_return_type
        self._current_return_type = node.return_type
        self._code_block(node.body)
        self._current_return_type = prev

    def _code_block(self, node: CodeBlock) -> None:
        for stmt in node.func_stmts:
            self._func_stmt(stmt)

    def _func_stmt(self, node) -> None:
        match node:
            case FuncDecl():
                self._func_decl(node)
            case VarDecl():
                self._var_decl(node)
            case NoAcsModeVarDecl():
                self._no_acs_var_decl(node)
            case VarAssign(var=var, val=val):
                target_type = self.types.get(var)
                node.val = self._expr(val, want=target_type)
            case Return():
                self._return(node)
            case IfElse():
                self._if_else(node)
            case WhileLoop(condition=cond, body=body):
                node.condition = self._expr(cond)
                self._code_block(body)
            case DoWhileLoop(body=body, condition=cond):
                self._code_block(body)
                node.condition = self._expr(cond)
            case ForLoop(init=init, condition=cond, update=update, body=body):
                if init:
                    self._no_acs_var_decl(init)
                if cond:
                    node.condition = self._expr(cond)
                if update:
                    node.update = self._expr(update)
                self._code_block(body)
            case ForInLoop(body=body, iterable=iterable):
                node.iterable = self._expr(iterable)
                self._code_block(body)
            case Defer(expr=e):
                node.expr = self._expr(e)
            case Expr():
                self._expr(node)  # walk children for side-effects

    def _var_decl(self, node: VarDecl) -> None:
        node.val = self._expr(node.val, want=node.type_ann)
        if node.type_ann is None:
            node.type_ann = self.types.get(node.val)

    def _no_acs_var_decl(self, node: NoAcsModeVarDecl) -> None:
        node.val = self._expr(node.val, want=node.type_ann)
        if node.type_ann is None:
            node.type_ann = self.types.get(node.val)

    def _return(self, node: Return) -> None:
        match self._current_return_type:
            case SingleReturnType(type_ann=expected) if len(node.vals) == 1:
                node.vals[0] = self._expr(node.vals[0], want=expected)
            case VoidReturnType():
                pass
            case _ if node.vals:
                # MultiReturnType or mismatch — transform each val without casting
                from compiler.ast.nodes import MultiReturnType
                match self._current_return_type:
                    case MultiReturnType(types=expected_types):
                        for i, (val, want) in enumerate(zip(node.vals, expected_types)):
                            node.vals[i] = self._expr(val, want=want)
                    case _:
                        for i, val in enumerate(node.vals):
                            node.vals[i] = self._expr(val)

    def _if_else(self, node: IfElse) -> None:
        node.condition = self._expr(node.condition)
        self._code_block(node.if_body)
        for clause in node.elif_clauses:
            clause.condition = self._expr(clause.condition)
            self._code_block(clause.body)
        if node.else_body:
            self._code_block(node.else_body)

    def _expr(self, node: Expr, want: Optional[Type] = None) -> Expr:
        """Transform expression children, then cast the result if widening is needed."""
        result = self._transform_expr(node)
        if want is not None and self._needs_cast(result, want):
            return self._cast(result, want)
        return result

    def _transform_expr(self, node: Expr) -> Expr:
        match node:
            case BinaryExpr():
                return self._binary_expr(node)
            case UnaryExpr(operand=operand):
                node.operand = self._expr(operand)
                return node
            case PostfixExpr():
                return node
            case TernaryExpr(condition=cond, true_expr=t, false_expr=f):
                node.condition = self._expr(cond)
                node.true_expr = self._expr(t)
                node.false_expr = self._expr(f)
                return node
            case FuncCall():
                return self._func_call(node)
            case ArrayLiteral(elements=elems):
                for i, e in enumerate(elems):
                    elems[i] = self._expr(e)
                return node
            case SetLiteral(elements=elems):
                for i, e in enumerate(elems):
                    elems[i] = self._expr(e)
                return node
            case MapLiteral(fields=fields):
                for f in fields:
                    f.key = self._expr(f.key)
                    f.val = self._expr(f.val)
                return node
            case StructLiteral(fields=fields):
                for sf in fields:
                    sf.val = self._expr(sf.val)
                return node
            case VarRef(accessors=accessors):
                for acc in accessors:
                    match acc:
                        case FieldAccessor():
                            pass  # no sub-expressions
                        case IndexAccessor(index=idx) if idx is not None:
                            acc.index = self._expr(idx)
                return node
            case _:
                return node  # literals — no children

    def _binary_expr(self, node: BinaryExpr) -> BinaryExpr:
        node.left = self._transform_expr(node.left)
        node.right = self._transform_expr(node.right)

        result_type = self.types.get(node)
        if result_type == BaseType.FLOAT:
            if self._type_of(node.left) == BaseType.INT:
                node.left = self._cast(node.left, BaseType.FLOAT)
            if self._type_of(node.right) == BaseType.INT:
                node.right = self._cast(node.right, BaseType.FLOAT)
        return node

    def _func_call(self, node: FuncCall) -> FuncCall:
        sym = self.symbols.lookup(node.func)
        if sym and sym.kind == SymbolKind.FUNCTION and sym.decl_node is not None:
            decl: FuncDecl = sym.decl_node  # type: ignore[assignment]
            for i, (arg, param) in enumerate(zip(node.args, decl.params)):
                node.args[i] = self._expr(arg, want=param.type_ann)
            for i in range(len(decl.params), len(node.args)):
                node.args[i] = self._expr(node.args[i])
        else:
            for i, arg in enumerate(node.args):
                node.args[i] = self._expr(arg)
        return node

    def _cast(self, node: Expr, to: Type) -> CastExpr:
        cast = CastExpr(expr=node, to=to)
        self.types.set(cast, to)
        return cast

    def _type_of(self, node: Expr) -> Optional[Type]:
        return self.types.get(node)

    def _needs_cast(self, node: Expr, want: Type) -> bool:
        """Currently handles int→float widening only."""
        got = self.types.get(node)
        return got == BaseType.INT and want == BaseType.FLOAT
