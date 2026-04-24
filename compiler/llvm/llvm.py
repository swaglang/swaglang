from typing import List

from compiler.ast.nodes import (
    AssignOp,
    BinaryExpr,
    BinaryOp,
    Break,
    Continue,
    Expr,
    ForLoop,
    IfElse,
    PostfixExpr,
    PostfixOp,
    VarAssign,
    VoidReturnType,
    FuncStmt,
    SingleReturnType,
    MultiReturnType,
    ReturnType,
    ASTNode,
    BaseType,
    BoolLiteral,
    CodeBlock,
    FloatLiteral,
    FuncCall,
    FuncDecl,
    GlobalVarDecl,
    IntLiteral,
    Prog,
    Return,
    StringLiteral,
    Type,
    VarDecl,
    VarRef,
    WhileLoop,
)
from compiler.llvm.llvm_builtins import BUILTINS
from compiler.semantic.symbols import SymbolTable
from compiler.semantic.type_table import TypeTable


class Block:
    def __init__(self):
        self.instructions: list[str] = []
        self._condition_label = None  # for break in loops
        self._end_label = None  # for continue in loops

    def add_instruction(self, instruction: str):
        self.instructions.append(instruction)

    def emit_instructions(self):
        return "\n".join(self.instructions)

    def condition_label(self):
        return self._condition_label

    def set_condition_label(self, label: str):
        self._condition_label = label

    def end_label(self):
        return self._end_label

    def set_end_label(self, label: str):
        self._end_label = label


class LLVMCompiler:
    _HEADER = "; https://github.com/swaglang/swaglang to https://github.com/llvm/llvm-project compiler"
    _STRING_TYPE_NAME = "%Str"
    _STRING_DECL = f"\n{_STRING_TYPE_NAME} = type {{ i64, ptr }}\n"

    def __init__(self, ast: ASTNode, types: TypeTable, symbols: SymbolTable):
        self._ast = ast
        self._types = types
        self._symbols = symbols
        self._blocks: List[Block] = []
        self._global_decl = ""
        self._nesting = 0
        self._ssa = 0
        self._unique_seq = 0
        self._locals: set[str] = set()

    def compile(self) -> str:
        return self._codegen(self._ast)

    def _enter_scope(self):
        self._nesting += 1
        self._blocks.append(Block())

    def _exit_scope(self):
        self._nesting -= 1
        block = self._blocks.pop()
        return block.emit_instructions()

    def _recent_ssa(self):
        return self._ssa

    def _reset_ssa(self):
        self._ssa = 0

    def _reg(self):
        self._ssa += 1
        return f"%r{self._ssa}"

    def _unique(self):
        self._unique_seq += 1
        return self._unique_seq

    def _block_top_level(self, instruction: str):
        indent = "  " * self._nesting
        self._blocks[-1].add_instruction(indent + instruction)

    def _label(self, name: str):
        self._blocks[-1].add_instruction(f"{name}:")

    def _set_condition_label(self, label: str):
        self._blocks[-1].set_condition_label(label)

    def _condition_label(self):
        return self._blocks[-1].condition_label()

    def _set_end_label(self, label: str):
        self._blocks[-1].set_end_label(label)

    def _end_label(self):
        return self._blocks[-1].end_label()

    def _codegen(self, node: ASTNode) -> str:
        match node:
            case Prog():
                return self._prog(node)
            case GlobalVarDecl():
                return self._global_var_decl(node)
            case FuncCall():
                return self._func_call(node)
            case FuncDecl():
                return self._func_decl(node)
            case _:
                print(f"Codegen for {type(node).__name__} not implemented yet")
                return ""

    def _global_declare(self, decl_str: str):
        self._global_decl += decl_str + "\n"

    def _prog(self, prog: Prog) -> str:
        out = ""

        self._global_declare(self._HEADER)
        self._global_declare(self._STRING_DECL)
        self._global_declare(self._printf_decl())
        self._global_declare("declare ptr @malloc(i64)")
        self._global_declare("declare void @llvm.memcpy.p0.p0.i64(ptr, ptr, i64, i1)\n")

        for stmt in prog.stmts:
            out += self._codegen(stmt)
        out = self._global_decl + out
        return out

    def _printf_decl(self) -> str:
        printf_decl = "declare i32 @printf(i8*, ...)  ; printf decl\n\n"
        printf_decl += '@fmt_int = private constant [6 x i8] c"%lld\\0A\\00"\n'
        printf_decl += '@fmt_float = private constant [4 x i8] c"%f\\0A\\00"\n'
        printf_decl += '@fmt_str = private constant [6 x i8] c"%.*s\\0A\\00"\n'
        printf_decl += '@fmt_true = private constant [6 x i8] c"true\\0A\\00"\n'
        printf_decl += '@fmt_false = private constant [7 x i8] c"false\\0A\\00"\n'
        printf_decl += '@fmt_int_inline = private constant [5 x i8] c"%lld\\00"\n'
        printf_decl += '@fmt_float_inline = private constant [3 x i8] c"%f\\00"\n'
        printf_decl += '@fmt_str_inline = private constant [5 x i8] c"%.*s\\00"\n'
        printf_decl += '@fmt_true_inline = private constant [5 x i8] c"true\\00"\n'
        printf_decl += '@fmt_false_inline = private constant [6 x i8] c"false\\00"\n'
        return printf_decl

    def _global_var_decl(self, node: GlobalVarDecl):
        type = self._llvm_type(node.type_ann)
        return f"@{node.name} = global {type} {node.val.val}\n"

    def _func_call(self, node: FuncCall):
        fn_name = node.func
        if fn_name in BUILTINS:
            return BUILTINS[fn_name](self, node.args)

        function = self._symbols.lookup(fn_name)
        if function is None:
            print("Something is very wrong 1, function is None (_func_call)")
        function = function.decl_node
        if function is None:
            print("Something is very wrong 2, function is None (_func_call)")
        decl: FuncDecl = function
        type = self._return_type(decl.return_type)
        reg = self._reg()
        call_str = f"{reg} = call {type} @{fn_name}("

        args_str = ", ".join(
            f"{self._llvm_type(p.type_ann)} {self._expr(a)}"
            for p, a in zip(decl.params, node.args)
        )
        call_str = f"{reg} = call {type} @{fn_name}({args_str})"
        self._block_top_level(call_str)
        return reg

    def _llvm_type(self, type: Type) -> str:
        match type:
            case BaseType.INT:
                return "i64"
            case BaseType.FLOAT:
                return "double"
            case BaseType.BOOL:
                return "i1"
            case BaseType.STRING:
                return self._STRING_TYPE_NAME
            case _:
                raise NotImplementedError(f"LLVM type for {type} not implemented yet")

    def _func_decl(self, node: FuncDecl) -> str:
        self._reset_ssa()
        self._locals = set()
        return_type = self._return_type(node.return_type)
        self._enter_scope()

        arg_strs = []
        for param in node.params:
            t = self._llvm_type(param.type_ann)
            self._alloca_store(param.name, t, f"%{param.name}")
            arg_strs.append(f"{self._llvm_type(param.type_ann)} %{param.name}")
        args_str = ", ".join(arg_strs)

        self._code_block(node.body)
        # TODO hacky, functions always need a ret at the end, but it's not required for void
        if isinstance(node.return_type, VoidReturnType):
            last = self._blocks[-1].instructions
            if not last or not last[-1].strip().startswith("ret"):
                self._block_top_level("ret void")
        body = self._exit_scope()

        return (
            f"define {return_type} @{node.name}({args_str}) nounwind {{\n{body}\n}}\n"
        )

    def _code_block(self, node: CodeBlock):
        for stmt in node.func_stmts:
            self._func_stmt(stmt)

    def _func_stmt(self, node: FuncStmt):
        match node:
            case FuncCall():
                self._func_call(node)
            case VarDecl():
                self._var_decl(node)
            case Return():
                self._return(node)
            case IfElse():
                self._ifelse(node)
            case WhileLoop():
                self._while(node)
            case Break():
                self._break()
            case Continue():
                self._continue()
            case PostfixExpr():
                self._postfix_op(node)
            case ForLoop():
                self._for(node)
            case VarAssign():
                self._var_assign(node)
            case _:
                print(f"implement func_stmt{type(node)} l{node.line} c{node.col}")

    def _var_decl(self, node: VarDecl):
        t = self._llvm_type(node.type_ann)
        self._alloca_store(node.name, t, self._expr(node.val))

    def _alloca_store(self, name: str, llvm_type: str, val: str):
        self._locals.add(name)
        slot = f"%{name}.addr"
        self._block_top_level(f"{slot} = alloca {llvm_type}, align 8")
        self._block_top_level(f"store {llvm_type} {val}, ptr {slot}, align 8")

    def _return_type(self, node: ReturnType):
        match node:
            case VoidReturnType():
                return "void"
            case SingleReturnType():
                return self._llvm_type(node.type_ann)
            case MultiReturnType():
                print("implement multi_return")
                return self._llvm_type(node.types[0])

    def _expr(self, node: Expr):
        match node:
            case IntLiteral(val=v):
                return str(v)
            case BoolLiteral(val=v):
                return "1" if v else "0"
            case FloatLiteral(val=v):
                return str(v)
            case StringLiteral(val=v):
                return self._string_struct(v)
            case VarRef():
                string_ptr = self._reg()
                llvm_t = self._llvm_type(self._types.get(node))
                ptr = (
                    f"%{node.name}.addr"
                    if node.name in self._locals
                    else f"@{node.name}"
                )
                self._block_top_level(
                    f"{string_ptr} = load {llvm_t}, ptr {ptr}, align 8"
                )
                return string_ptr
            case BinaryExpr(op=op, left=left, right=right):
                return self._binary_op(op, left, right)
            case FuncCall():
                return self._func_call(node)
            case PostfixExpr():
                self._postfix_op(node)
            case _:
                print(f"implement expr: {type(node)}")
        return ""

    def _string_struct(self, string: str) -> str:
        str_l = len(string)
        n = self._unique()
        self._global_declare(f'@str{n} = private constant [{str_l} x i8] c"{string}"')
        string_ptr = self._reg()
        ptr_aq = (
            f"{string_ptr} = getelementptr [{str_l} x i8], ptr @str{n}, i32 0, i32 0"
        )
        self._block_top_level(ptr_aq)
        sized_reg = f"%len_ass_{n}"
        self._block_top_level(
            f"{sized_reg} = insertvalue {self._STRING_TYPE_NAME} undef, i64 {str_l}, 0"
        )
        populated_reg = f"%str_ass_{n}"
        self._block_top_level(
            f"{populated_reg} = insertvalue {self._STRING_TYPE_NAME} {sized_reg}, ptr {string_ptr}, 1"
        )
        return populated_reg

    def _return(self, node: Return):
        match len(node.vals):
            case 0:
                self._block_top_level("ret void")
            case 1:
                ret = node.vals[0]
                val = self._expr(ret)
                type = self._llvm_type(self._types.get(ret))
                self._block_top_level(f"ret {type} {val}")
            case _:
                print("implement multi-return in _return")

    def _binary_op(self, op: BinaryOp, left: Expr, right: Expr):
        left_val = self._expr(left)
        right_val = self._expr(right)
        match self._types.get(left):
            case BaseType.INT:
                return self._binary_op_int(op, left_val, right_val)
            case BaseType.BOOL:
                return self._binary_op_bool(op, left_val, right_val)
            case BaseType.STRING:
                return self._binary_op_string(op, left_val, right_val)
            case _:
                print(f"implement binary op {op}")
                return ""

    def _binary_op_int(self, op: BinaryOp, left: str, right: str):
        reg = self._reg()

        match op:
            case BinaryOp.ADD:
                self._block_top_level(f"{reg} = add i64 {left}, {right}")
            case BinaryOp.SUB:
                self._block_top_level(f"{reg} = sub i64 {left}, {right}")
            case BinaryOp.MUL:
                self._block_top_level(f"{reg} = mul i64 {left}, {right}")
            case BinaryOp.DIV:
                self._block_top_level(f"{reg} = sdiv i64 {left}, {right}")
            case BinaryOp.MOD:
                self._block_top_level(f"{reg} = srem i64 {left}, {right}")
            case BinaryOp.EQ:
                self._block_top_level(f"{reg} = icmp eq i64 {left}, {right}")
            case BinaryOp.NEQ:
                self._block_top_level(f"{reg} = icmp ne i64 {left}, {right}")
            case BinaryOp.LT:
                self._block_top_level(f"{reg} = icmp slt i64 {left}, {right}")
            case BinaryOp.GT:
                self._block_top_level(f"{reg} = icmp sgt i64 {left}, {right}")
            case BinaryOp.LTE:
                self._block_top_level(f"{reg} = icmp sle i64 {left}, {right}")
            case BinaryOp.GTE:
                self._block_top_level(f"{reg} = icmp sge i64 {left}, {right}")
            case _:
                print(f"implement int binary op {op} for int")
        return reg

    def _binary_op_bool(self, op: BinaryOp, left: str, right: str):
        reg = self._reg()
        match op:
            case BinaryOp.AND:
                self._block_top_level(f"{reg} = and i1 {left}, {right}")
            case BinaryOp.OR:
                self._block_top_level(f"{reg} = or i1 {left}, {right}")
            case BinaryOp.EQ:
                self._block_top_level(f"{reg} = icmp eq i1 {left}, {right}")
            case BinaryOp.NEQ:
                self._block_top_level(f"{reg} = icmp ne i1 {left}, {right}")
            case BinaryOp.NOT:
                self._block_top_level(f"{reg} = xor i1 {left}, 1")
            case _:
                print(f"implement bool binary op {op} for bool (should not happen)")
        return reg

    def _binary_op_string(self, op: BinaryOp, left: str, right: str):
        match op:
            case BinaryOp.ADD:
                n = self._unique()
                len_a = f"%concat_len_a_{n}"
                data_a = f"%concat_data_a_{n}"
                len_b = f"%concat_len_b_{n}"
                data_b = f"%concat_data_b_{n}"
                self._block_top_level(
                    f"{len_a} = extractvalue {self._STRING_TYPE_NAME} {left}, 0"
                )
                self._block_top_level(
                    f"{data_a} = extractvalue {self._STRING_TYPE_NAME} {left}, 1"
                )
                self._block_top_level(
                    f"{len_b} = extractvalue {self._STRING_TYPE_NAME} {right}, 0"
                )
                self._block_top_level(
                    f"{data_b} = extractvalue {self._STRING_TYPE_NAME} {right}, 1"
                )
                new_len = f"%concat_len_{n}"
                buf = f"%concat_buf_{n}"
                self._block_top_level(f"{new_len} = add i64 {len_a}, {len_b}")
                self._block_top_level(f"{buf} = call ptr @malloc(i64 {new_len})")
                self._block_top_level(
                    f"call void @llvm.memcpy.p0.p0.i64(ptr {buf}, ptr {data_a}, i64 {len_a}, i1 false)"
                )
                self._block_top_level(
                    f"%offset_{n} = getelementptr i8, ptr {buf}, i64 {len_a}"
                )
                self._block_top_level(
                    f"call void @llvm.memcpy.p0.p0.i64(ptr %offset_{n}, ptr {data_b}, i64 {len_b}, i1 false)"
                )
                sized_reg = f"%concat_sized_{n}"
                self._block_top_level(
                    f"{sized_reg} = insertvalue {self._STRING_TYPE_NAME} undef, i64 {new_len}, 0"
                )
                populated_reg = f"%concat_populated_{n}"
                self._block_top_level(
                    f"{populated_reg} = insertvalue {self._STRING_TYPE_NAME} {sized_reg}, ptr {buf}, 1"
                )
            case BinaryOp.MUL:
                n = self._unique()
                len_s = f"%mul_len_{n}"
                data_s = f"%mul_data_{n}"
                new_len = f"%mul_newlen_{n}"
                buf = f"%mul_buf_{n}"
                i_slot = f"%mul_i_{n}.addr"
                p_slot = f"%mul_ptr_{n}.addr"
                self._block_top_level(f"{len_s}  = extractvalue %Str {left}, 0")
                self._block_top_level(f"{data_s} = extractvalue %Str {left}, 1")
                self._block_top_level(f"{new_len} = mul i64 {len_s}, {right}")
                self._block_top_level(f"{buf} = call ptr @malloc(i64 {new_len})")
                self._block_top_level(f"{i_slot} = alloca i64, align 8")
                self._block_top_level(f"store i64 0, ptr {i_slot}, align 8")
                self._block_top_level(f"{p_slot} = alloca ptr, align 8")
                self._block_top_level(f"store ptr {buf}, ptr {p_slot}, align 8")
                cond_lbl = f"mul_cond_{n}"
                body_lbl = f"mul_body_{n}"
                end_lbl = f"mul_end_{n}"
                self._block_top_level(f"br label %{cond_lbl}")
                self._label(cond_lbl)
                i_cur = f"%mul_i_cur_{n}"
                cmp = f"%mul_cmp_{n}"
                self._block_top_level(f"{i_cur} = load i64, ptr {i_slot}, align 8")
                self._block_top_level(f"{cmp} = icmp slt i64 {i_cur}, {right}")
                self._block_top_level(
                    f"br i1 {cmp}, label %{body_lbl}, label %{end_lbl}"
                )
                self._label(body_lbl)
                cur_ptr = f"%mul_curptr_{n}"
                next_ptr = f"%mul_nextptr_{n}"
                i_next = f"%mul_inext_{n}"
                self._block_top_level(f"{cur_ptr} = load ptr, ptr {p_slot}, align 8")
                self._block_top_level(
                    f"call void @llvm.memcpy.p0.p0.i64(ptr {cur_ptr}, ptr {data_s}, i64 {len_s}, i1 false)"
                )
                self._block_top_level(
                    f"{next_ptr} = getelementptr i8, ptr {cur_ptr}, i64 {len_s}"
                )
                self._block_top_level(f"store ptr {next_ptr}, ptr {p_slot}, align 8")
                self._block_top_level(f"{i_next} = add i64 {i_cur}, 1")
                self._block_top_level(f"store i64 {i_next}, ptr {i_slot}, align 8")
                self._block_top_level(f"br label %{cond_lbl}")
                self._label(end_lbl)
                tmp = f"%mul_tmp_{n}"
                res = f"%mul_res_{n}"
                self._block_top_level(
                    f"{tmp} = insertvalue %Str undef, i64 {new_len}, 0"
                )
                self._block_top_level(f"{res} = insertvalue %Str {tmp}, ptr {buf}, 1")
                return res

        return populated_reg

    def _ifelse(self, node: IfElse):
        end_label = f"end_{self._unique()}"
        elif_labels = [f"elif_{self._unique()}" for _ in node.elif_clauses]
        else_label = f"else_{self._unique()}" if node.else_body else end_label
        if_label = f"if_{self._unique()}"

        first = elif_labels[0] if elif_labels else else_label
        cond = self._expr(node.condition)
        self._block_top_level(f"br i1 {cond}, label %{if_label}, label %{first}")

        # elif checks
        for i, (label, clause) in enumerate(zip(elif_labels, node.elif_clauses)):
            next_label = elif_labels[i + 1] if i + 1 < len(elif_labels) else else_label
            self._label(label)
            cond = self._expr(clause.condition)
            self._block_top_level(
                f"br i1 {cond}, label %{label}_body, label %{next_label}"
            )

        # bodies
        self._label(if_label)
        self._code_block(node.if_body)
        self._block_top_level(f"br label %{end_label}")

        for label, clause in zip(elif_labels, node.elif_clauses):
            self._label(f"{label}_body")
            self._code_block(clause.body)
            self._block_top_level(f"br label %{end_label}")

        if node.else_body:
            self._label(else_label)
            self._code_block(node.else_body)
            self._block_top_level(f"br label %{end_label}")

        self._label(end_label)

    def _while(self, node: WhileLoop):
        n = self._unique()
        condition_label = f"while_cond_{n}"
        body_label = f"while_body_{n}"
        end_label = f"while_end_{n}"
        self._set_condition_label(condition_label)
        self._set_end_label(end_label)

        self._label(condition_label)
        cond = self._expr(node.condition)
        self._block_top_level(f"br i1 {cond}, label %{body_label}, label %{end_label}")

        self._label(body_label)
        self._code_block(node.body)
        self._block_top_level(f"br label %{condition_label}")

        self._label(end_label)

    def _break(self):
        end_label = self._end_label()
        if end_label is None:
            print("?! break statement not within a loop")
            return
        self._block_top_level(f"br label %{end_label}")

    def _continue(self):
        condition_label = self._condition_label()
        if condition_label is None:
            print("?! continue statement not within a loop")
            return
        self._block_top_level(f"br label %{condition_label}")

    def _postfix_op(self, postfix: PostfixExpr):
        match postfix.op:
            case PostfixOp.INC:
                op = "add"
            case PostfixOp.DEC:
                op = "sub"

        ptr = f"{postfix.operand.name}.addr"
        reg_old = f"{ptr}.old"
        reg_new = f"{ptr}.new"
        llvm_t = self._llvm_type(self._types.get(postfix.operand))
        self._block_top_level(f"%{reg_old} = load {llvm_t}, ptr %{ptr}, align 8")
        self._block_top_level(f"%{reg_new} = {op} {llvm_t} %{reg_old}, 1")
        self._block_top_level(f"store {llvm_t} %{reg_new}, ptr %{ptr}")

    def _for(self, loop: ForLoop):
        n = self._unique()
        update_label = f"for_update_{n}"
        cond_label = f"for_cond_{n}"
        end_label = f"for_end_{n}"
        body_label = f"for_body_{n}"
        if loop.update:
            self._set_condition_label(update_label)
        else:
            self._set_condition_label(cond_label)
        self._set_end_label(end_label)

        if loop.init:
            self._var_decl(loop.init)

        if loop.condition:
            self._block_top_level(f"br label %{cond_label}")
        else:
            self._block_top_level(f"br label %{body_label}")
        if loop.update:
            self._label(update_label)
            match loop.update:
                case VarAssign():
                    self._var_assign(loop.update)
                case Expr():
                    self._expr(loop.update)
            if loop.condition:
                self._block_top_level(f"br label %{cond_label}")
            else:
                self._block_top_level(f"br label %{body_label}")

        if loop.condition:
            self._label(cond_label)
            cond = self._expr(loop.condition)
            self._block_top_level(
                f"br i1 {cond}, label %{body_label}, label %{end_label}"
            )
        self._label(body_label)
        self._code_block(loop.body)
        if loop.update:
            self._block_top_level(f"br label %{update_label}")
        elif loop.condition:
            self._block_top_level(f"br label %{cond_label}")
        else:
            self._block_top_level(f"br label %{body_label}")
        self._label(end_label)

    _ASSIGN_TO_BINARY = {
        AssignOp.ADD_ASSIGN: BinaryOp.ADD,
        AssignOp.SUB_ASSIGN: BinaryOp.SUB,
        AssignOp.MUL_ASSIGN: BinaryOp.MUL,
        AssignOp.DIV_ASSIGN: BinaryOp.DIV,
        AssignOp.MOD_ASSIGN: BinaryOp.MOD,
    }

    def _var_assign(self, assign: VarAssign):
        val = self._expr(assign.val)
        var_type = self._types.get(assign.var)
        llvm_t = self._llvm_type(var_type)

        if assign.op == AssignOp.ASSIGN:
            self._block_top_level(
                f"store {llvm_t} {val}, ptr %{assign.var.name}.addr, align 8"
            )
            return

        n = self._unique()
        old = f"%{assign.var.name}.old{n}"
        self._block_top_level(
            f"{old} = load {llvm_t}, ptr %{assign.var.name}.addr, align 8"
        )

        if var_type == BaseType.STRING and assign.op == AssignOp.ADD_ASSIGN:
            new = self._binary_op_string(BinaryOp.ADD, old, val)
            self._block_top_level(
                f"store {llvm_t} {new}, ptr %{assign.var.name}.addr, align 8"
            )
            return

        binary_op = self._ASSIGN_TO_BINARY[assign.op]
        new = self._binary_op_int(binary_op, old, val)
        self._block_top_level(
            f"store {llvm_t} {new}, ptr %{assign.var.name}.addr, align 8"
        )
