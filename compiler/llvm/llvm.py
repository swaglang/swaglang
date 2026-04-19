from typing import List

from compiler.ast.nodes import (
    BinaryExpr,
    BinaryOp,
    Expr,
    IfElse,
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
    VarRef
)
from compiler.llvm.builtins import BUILTINS
from compiler.semantic.symbols import SymbolTable
from compiler.semantic.type_table import TypeTable


class Block:
    def __init__(self):
        self.instructions: list[str] = []

    def add_instruction(self, instruction: str):
        self.instructions.append(instruction)

    def emit_instructions(self):
        return "\n".join(self.instructions)


class LLVMCompiler:
    _HEADER = "; https://github.com/swaglang/swaglang to https://github.com/llvm/llvm-project compiler\n"

    def __init__(self, ast: ASTNode, types: TypeTable, symbols: SymbolTable):
        self._ast = ast
        self._types = types
        self._symbols = symbols
        self._blocks: List[Block] = []
        self._global_decl = ""
        self._nesting = 0
        self._ssa = 0
        self._unique_seq = 0

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
        self._global_declare(self._printf_decl())

        for stmt in prog.stmts:
            out += self._codegen(stmt)
        out = self._global_decl + out
        return out

    def _printf_decl(self) -> str:
        printf_decl = "declare i32 @printf(i8*, ...)  ; printf decl\n\n"
        printf_decl += '@fmt_int = private constant [6 x i8] c"%lld\\0A\\00"\n'
        printf_decl += '@fmt_float = private constant [4 x i8] c"%f\\0A\\00"\n'
        printf_decl += '@fmt_str = private constant [4 x i8] c"%s\\0A\\00"\n'
        printf_decl += '@fmt_true = private constant [6 x i8] c"true\\0A\\00"\n'
        printf_decl += '@fmt_false = private constant [7 x i8] c"false\\0A\\00"\n'
        printf_decl += '@fmt_int_inline = private constant [5 x i8] c"%lld\\00"\n'
        printf_decl += '@fmt_float_inline = private constant [3 x i8] c"%f\\00"\n'
        printf_decl += '@fmt_str_inline = private constant [3 x i8] c"%s\\00"\n'
        printf_decl += '@fmt_true_inline = private constant [5 x i8] c"true\\00"\n'
        printf_decl += '@fmt_false_inline = private constant [6 x i8] c"false\\00"\n'
        return printf_decl

    def _global_var_decl(self, node: GlobalVarDecl):
        type = self._llvm_type(node.type_ann)
        return f"@{node.name} = global {type} {node.val.val}\n"

    def _func_call(self, node: FuncCall):
        fn_name = node.func
        if fn_name in BUILTINS:
            BUILTINS[fn_name](self, node.args)
            return
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
                return "ptr"
            case _:
                raise NotImplementedError(f"LLVM type for {type} not implemented yet")

    def _func_decl(self, node: FuncDecl) -> str:
        self._reset_ssa()
        return_type = self._return_type(node.return_type)
        self._enter_scope()

        arg_strs = []
        for param in node.params:
            t = self._llvm_type(param.type_ann)
            self._alloca_store(param.name, t, f"%{param.name}")
            arg_strs.append(f"{self._llvm_type(param.type_ann)} %{param.name}")
        args_str = ", ".join(arg_strs)

        self._code_block(node.body)
        body = self._exit_scope()

        return f"define {return_type} @{node.name}({args_str}) nounwind {{\n{body}\n}}\n"

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
            case _:
                print(f"implement func_stmt{type(node)}")

    def _var_decl(self, node: VarDecl):
        t = self._llvm_type(node.type_ann)
        self._alloca_store(node.name, t, self._expr(node.val))

    def _alloca_store(self, name: str, llvm_type: str, val: str):
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
                n = len(v) + 1
                name = self._unique()
                self._global_declare(
                    f'@str{name} = private constant [{n} x i8] c"{v}\\00"'
                )
                reg = self._reg()
                ptr_aq = (
                    f"{reg} = getelementptr [{n} x i8], ptr @str{name}, i32 0, i32 0"
                )
                self._block_top_level(ptr_aq)
                return reg
            case VarRef():
                reg = self._reg()
                llvm_t = self._llvm_type(self._types.get(node))
                sym = self._symbols.lookup(node.name)
                is_global = sym is not None and isinstance(sym.decl_node, GlobalVarDecl)
                ptr = f"@{node.name}" if is_global else f"%{node.name}.addr"
                self._block_top_level(f"{reg} = load {llvm_t}, ptr {ptr}, align 8")
                return reg
            case BinaryExpr(op=op, left=left, right=right):
                return self._binary_op(op, left, right)
            case FuncCall():
                return self._func_call(node)
            case _:
                print(f"implement expr: {type(node)}")
        return ""

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
                print(f"implement binary op {op} for int")
        return reg

    def _ifelse(self, node: IfElse):
        cond = self._expr(node.condition)
        n = self._unique()
        if_label = f"if_true_{n}"
        else_label = f"if_false_{n}" if node.else_body else f"end_{n}"
        self._block_top_level(f"br i1 {cond}, label %{if_label}, label %{else_label}")
        self._label(if_label)
        self._code_block(node.if_body)
        self._label(f"end_{n}")
