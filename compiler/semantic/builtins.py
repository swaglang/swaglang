from typing import Callable, Optional
from compiler.ast.nodes import (
    ArrayType,
    BaseType,
    FuncDecl,
    MapType,
    SetType,
    Type,
)
from compiler.semantic.symbols import Symbol, SymbolKind


# Arg predicate helpers
def _sizeable(t: Optional[Type]) -> bool:
    return t == BaseType.STRING or isinstance(t, (ArrayType, SetType, MapType))


def _any(_: Optional[Type]) -> bool:
    return True


def _int(t: Optional[Type]) -> bool:
    return t == BaseType.INT


# Builtin signatures: name -> ([arg_predicate, ...], return_type | None)
# arg_predicate: callable(Type) -> bool, one entry per accepted positional arg
# return_type None means void
BUILTIN_SIGS: dict[str, tuple[list[Callable], Optional[Type]]] = {
    "println": ([_any], None),
    "print": ([_any], None),
    "len": ([_sizeable], BaseType.INT),
    # range(n), range(start, end), range(start, end, step)
    "range": ([_int, _int, _int], ArrayType(BaseType.INT)),
    # input() or input("prompt") -> string
    "input": ([_any], BaseType.STRING),
}

_TYPED: dict[str, FuncDecl] = {}


def builtin_symbols() -> list[Symbol]:
    syms = [
        Symbol(
            name=name,
            kind=SymbolKind.FUNCTION,
            type=None,
            is_mutable=False,
            decl_node=None,
        )
        for name in BUILTIN_SIGS
    ]
    for name, decl in _TYPED.items():
        syms.append(
            Symbol(
                name=name,
                kind=SymbolKind.FUNCTION,
                type=None,
                is_mutable=False,
                decl_node=decl,
            )
        )
    return syms
