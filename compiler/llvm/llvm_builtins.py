from __future__ import annotations
from typing import TYPE_CHECKING, Callable

from compiler.ast.nodes import ArrayType, BaseType, Expr, SetType

if TYPE_CHECKING:
    from compiler.llvm.llvm import LLVMCompiler

BuiltinHandler = Callable[["LLVMCompiler", list[Expr]], str | None]


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
            n = compiler._unique()
            len64 = f"%len64_{n}"
            data = f"%data_{n}"
            len32 = f"%len32_{n}"
            compiler._block_top_level(
                f"{len64} = extractvalue {compiler._STRING_TYPE_NAME} {val}, 0"
            )
            compiler._block_top_level(
                f"{data}  = extractvalue {compiler._STRING_TYPE_NAME} {val}, 1"
            )
            compiler._block_top_level(f"{len32} = trunc i64 {len64} to i32")
            insn = f"call i32 (ptr, ...) @printf(ptr @fmt_str{suffix}, i32 {len32}, ptr {data})"
        case BaseType.BOOL:
            # branch on the i1 value to pick true/false format string
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


def _len_builtin(compiler: "LLVMCompiler", arg: Expr) -> str:
    val = compiler._expr(arg)
    t = compiler._types.get(arg)
    len_reg = compiler._reg()
    match t:
        case ArrayType() | SetType():
            llvm_t = compiler._ARR_TYPE_NAME
        case _:  # string
            llvm_t = compiler._STRING_TYPE_NAME
    compiler._block_top_level(f"{len_reg} = extractvalue {llvm_t} {val}, 0")
    return len_reg


def _range_builtin(compiler: "LLVMCompiler", args: list[Expr]) -> str:
    # range(n) [0 .. n-1], step=+1
    # range(start, end) [start .. end-1], step=+1
    # range(start, end, step) step-aware, supports negative step
    if len(args) == 1:
        start_val = "0"
        end_val = compiler._expr(args[0])
        step_val = "1"
    elif len(args) == 2:
        start_val = compiler._expr(args[0])
        end_val = compiler._expr(args[1])
        step_val = "1"
    else:
        start_val = compiler._expr(args[0])
        end_val = compiler._expr(args[1])
        step_val = compiler._expr(args[2])

    n = compiler._unique()
    # Allocate abs(end-start) slots - upper bound regardless of step
    diff = f"%range_diff_{n}"
    neg_diff = f"%range_ndiff_{n}"
    is_neg = f"%range_isneg_{n}"
    abs_diff = f"%range_abs_{n}"
    size = f"%range_size_{n}"
    buf = f"%range_buf_{n}"
    val_slot = f"%range_val_{n}.addr"  # current value (start + k*step)
    cnt_slot = f"%range_cnt_{n}.addr"  # element count written
    cond_lbl = f"range_cond_{n}"
    body_lbl = f"range_body_{n}"
    end_lbl = f"range_end_{n}"

    compiler._block_top_level(f"{diff} = sub i64 {end_val}, {start_val}")
    compiler._block_top_level(f"{neg_diff} = sub i64 0, {diff}")
    compiler._block_top_level(f"{is_neg} = icmp slt i64 {diff}, 0")
    compiler._block_top_level(
        f"{abs_diff} = select i1 {is_neg}, i64 {neg_diff}, i64 {diff}"
    )
    compiler._block_top_level(f"{size} = mul i64 {abs_diff}, 8")
    compiler._block_top_level(f"{buf} = call ptr @malloc(i64 {size})")

    compiler._block_top_level(f"{val_slot} = alloca i64, align 8")
    compiler._block_top_level(f"store i64 {start_val}, ptr {val_slot}, align 8")
    compiler._block_top_level(f"{cnt_slot} = alloca i64, align 8")
    compiler._block_top_level(f"store i64 0, ptr {cnt_slot}, align 8")
    compiler._block_top_level(f"br label %{cond_lbl}")

    # step>0 val<end or step<0 val>end
    compiler._label(cond_lbl)
    val_cur = f"%range_val_cur_{n}"
    cnt_cur = f"%range_cnt_cur_{n}"
    step_pos = f"%range_step_pos_{n}"
    cmp_fwd = f"%range_cmp_fwd_{n}"
    cmp_back = f"%range_cmp_back_{n}"
    go = f"%range_go_{n}"
    compiler._block_top_level(f"{val_cur} = load i64, ptr {val_slot}, align 8")
    compiler._block_top_level(f"{cnt_cur} = load i64, ptr {cnt_slot}, align 8")
    compiler._block_top_level(f"{step_pos} = icmp sgt i64 {step_val}, 0")
    compiler._block_top_level(f"{cmp_fwd} = icmp slt i64 {val_cur}, {end_val}")
    compiler._block_top_level(f"{cmp_back} = icmp sgt i64 {val_cur}, {end_val}")
    compiler._block_top_level(
        f"{go}       = select i1 {step_pos}, i1 {cmp_fwd}, i1 {cmp_back}"
    )
    compiler._block_top_level(f"br i1 {go}, label %{body_lbl}, label %{end_lbl}")

    compiler._label(body_lbl)
    elem_ptr = f"%range_eptr_{n}"
    val_next = f"%range_vnext_{n}"
    cnt_next = f"%range_cnext_{n}"
    compiler._block_top_level(
        f"{elem_ptr} = getelementptr i64, ptr {buf}, i64 {cnt_cur}"
    )
    compiler._block_top_level(f"store i64 {val_cur}, ptr {elem_ptr}, align 8")
    compiler._block_top_level(f"{val_next} = add i64 {val_cur}, {step_val}")
    compiler._block_top_level(f"store i64 {val_next}, ptr {val_slot}, align 8")
    compiler._block_top_level(f"{cnt_next} = add i64 {cnt_cur}, 1")
    compiler._block_top_level(f"store i64 {cnt_next}, ptr {cnt_slot}, align 8")
    compiler._block_top_level(f"br label %{cond_lbl}")

    compiler._label(end_lbl)
    final_cnt = f"%range_final_cnt_{n}"
    sized = f"%range_sized_{n}"
    result = f"%range_result_{n}"
    compiler._block_top_level(f"{final_cnt} = load i64, ptr {cnt_slot}, align 8")
    compiler._block_top_level(
        f"{sized}     = insertvalue %Arr undef, i64 {final_cnt}, 0"
    )
    compiler._block_top_level(f"{result} = insertvalue %Arr {sized}, ptr {buf}, 1")
    return result


BUILTINS: dict[str, BuiltinHandler] = {
    "println": lambda c, args: _print_handler(c, args, newline=True),
    "print": lambda c, args: _print_handler(c, args, newline=False),
    "len": lambda c, args: _len_builtin(c, args[0]),
    "range": lambda c, args: _range_builtin(c, args),
}
