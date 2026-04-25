from __future__ import annotations
from typing import Optional
from compiler.ast.nodes import (
    ArrayType, BaseType, BinaryOp, MapType, SetType, Type, UnaryOp, UserType,
)

_NUMERIC   = frozenset({BaseType.INT, BaseType.FLOAT})
_PRIMITIVE = frozenset({BaseType.INT, BaseType.FLOAT, BaseType.STRING, BaseType.BOOL, BaseType.ERROR})

def is_numeric(t: Type) -> bool:
    return t in _NUMERIC

def is_comparable(t: Type) -> bool:
    return t in _PRIMITIVE

def common_type(a: Type, b: Type) -> Optional[Type]:
    """Widening: INT+INT→INT, INT+FLOAT→FLOAT, FLOAT+FLOAT→FLOAT, else None."""
    if a == b:
        return a
    if a in _NUMERIC and b in _NUMERIC:
        return BaseType.FLOAT
    return None

def binary_result_type(op: BinaryOp, left: Type, right: Type) -> Optional[Type]:
    match op:
        case BinaryOp.ADD:
            if left == BaseType.STRING and right == BaseType.STRING:
                return BaseType.STRING
            return common_type(left, right) if is_numeric(left) and is_numeric(right) else None
        case BinaryOp.MUL:
            if left == BaseType.STRING and right == BaseType.INT:
                return BaseType.STRING # "abc" * 3  →  "abcabcabc"
            return common_type(left, right) if is_numeric(left) and is_numeric(right) else None
        case BinaryOp.SUB | BinaryOp.DIV | BinaryOp.MOD | BinaryOp.EXP:
            return common_type(left, right) if is_numeric(left) and is_numeric(right) else None
        case BinaryOp.EQ | BinaryOp.NEQ:
            if left == right:
                return BaseType.BOOL
            if is_numeric(left) and is_numeric(right):
                return BaseType.BOOL
            return None
        case BinaryOp.LT | BinaryOp.GT | BinaryOp.LTE | BinaryOp.GTE:
            if is_numeric(left) and is_numeric(right):
                return BaseType.BOOL
            if left == BaseType.STRING and right == BaseType.STRING:
                return BaseType.BOOL
            return None
        case BinaryOp.AND | BinaryOp.OR:
            return BaseType.BOOL if left == BaseType.BOOL and right == BaseType.BOOL else None
        case _:
            return None

def is_truthy(t: Type) -> bool:
    """Types usable in boolean context (if/while/! operator)."""
    return t in (BaseType.BOOL, BaseType.INT, BaseType.FLOAT, BaseType.STRING) \
        or isinstance(t, (ArrayType, SetType))

def unary_result_type(op: UnaryOp, operand: Type) -> Optional[Type]:
    match op:
        case UnaryOp.NOT:
            return BaseType.BOOL if is_truthy(operand) else None
        case UnaryOp.NEG:
            return operand if is_numeric(operand) else None
        case _:
            return None

def is_assignable(target: Type, source: Type) -> bool:
    if source == BaseType.ERROR:
        return target == BaseType.ERROR or isinstance(target, UserType)
    if target == BaseType.ERROR and source == BaseType.STRING:
        return True
    if target == BaseType.FLOAT and source == BaseType.INT:
        return True  # implicit widening; CastExpr inserted by ASTTransformer
    return target == source

def element_type(t: Type) -> Optional[Type]:
    """Array or set element type; None for anything else."""
    match t:
        case ArrayType(element=e):
            return e
        case SetType(element=e):
            return e
        case _:
            return None

def key_value_types(t: Type) -> Optional[tuple[Type, Type]]:
    """Map key and value types; None for anything else."""
    match t:
        case MapType(key=k, value=v):
            return (k, v)
        case _:
            return None

def fmt_type(t: Type) -> str:
    """Human-readable type string for error messages."""
    match t:
        case BaseType():
            return t.value
        case UserType(name=n):
            return n
        case ArrayType(element=e):
            return f"{fmt_type(e)}[]"
        case MapType(key=k, value=v):
            return f"map<{fmt_type(k)}, {fmt_type(v)}>"
        case SetType(element=e):
            return f"set<{fmt_type(e)}>"
        case _:
            return "?"
