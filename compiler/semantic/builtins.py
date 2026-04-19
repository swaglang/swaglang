from compiler.ast.nodes import (
    BaseType, CodeBlock, FuncDecl, ParamDecl,
    SingleReturnType, VoidReturnType,
)
from compiler.semantic.symbols import Symbol, SymbolKind


def _make_decl(name: str, params: list[ParamDecl], return_type) -> FuncDecl:
    return FuncDecl(
        return_type=return_type,
        name=name,
        params=params,
        body=CodeBlock(func_stmts=[]),
    )


def _void(name: str, params: list[ParamDecl]) -> FuncDecl:
    return _make_decl(name, params, VoidReturnType())


def _ret(name: str, params: list[ParamDecl], t: BaseType) -> FuncDecl:
    return _make_decl(name, params, SingleReturnType(type_ann=t))


_POLYMORPHIC: set[str] = {"println", "print"}

_TYPED: dict[str, FuncDecl] = {
    "len": _ret("len", [ParamDecl(name="s", type_ann=BaseType.STRING)], BaseType.INT),
}


def builtin_symbols() -> list[Symbol]:
    syms: list[Symbol] = []
    for name in _POLYMORPHIC:
        syms.append(Symbol(
            name=name,
            kind=SymbolKind.FUNCTION,
            type=None,
            is_mutable=False,
            decl_node=None,
        ))
    for name, decl in _TYPED.items():
        syms.append(Symbol(
            name=name,
            kind=SymbolKind.FUNCTION,
            type=None,
            is_mutable=False,
            decl_node=decl,
        ))
    return syms
