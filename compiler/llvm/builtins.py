from __future__ import annotations
from typing import TYPE_CHECKING, Callable

from compiler.ast.nodes import BaseType, Expr

if TYPE_CHECKING:
    from compiler.llvm.llvm import LLVMCompiler

BuiltinHandler = Callable[["LLVMCompiler", list[Expr], bool], None]


def _print_handler(compiler: "LLVMCompiler", args: list[Expr], newline: bool) -> None:
    arg = args[0]
    arg_type = compiler._types.get(arg)
    val = compiler._expr(arg)
    suffix = "" if newline else "_inline"

    match arg_type:
        case BaseType.INT:
            insn = f"call i32 (ptr, ...) @printf(ptr @fmt_int{suffix}, i64 {val})"
        case BaseType.FLOAT:
            insn = f"call i32 (ptr, ...) @printf(ptr @fmt_float{suffix}, double {val})"
        case BaseType.STRING:
            insn = f"call i32 (ptr, ...) @printf(ptr @fmt_str{suffix}, ptr {val})"
        case BaseType.BOOL:
            # branch on the i1 value to pick true/false format string
            reg = compiler._reg()
            n = compiler._unique()
            compiler._block_top_level(
                f"br i1 {val}, label %bool_true_{n}, label %bool_false_{n}"
            )
            compiler._label(f"bool_true_{n}")
            compiler._block_top_level(
                f"call i32 (ptr, ...) @printf(ptr @fmt_true{suffix})"
            )
            compiler._block_top_level(f"br label %bool_end_{n}")
            compiler._label(f"bool_false_{n}")
            compiler._block_top_level(
                f"call i32 (ptr, ...) @printf(ptr @fmt_false{suffix})"
            )
            compiler._block_top_level(f"br label %bool_end_{n}")
            compiler._label(f"bool_end_{n}")
            return
        case _:
            return

    compiler._block_top_level(insn)


BUILTINS: dict[str, Callable[["LLVMCompiler", list[Expr]], None]] = {
    "println": lambda c, args: _print_handler(c, args, newline=True),
    "print":   lambda c, args: _print_handler(c, args, newline=False),
}
