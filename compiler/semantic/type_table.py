from __future__ import annotations
from typing import Optional
from compiler.ast.nodes import ASTNode, Type

class TypeTable:
    """Maps every Expr node to its resolved Type by object identity."""

    def __init__(self) -> None:
        self._table: dict[int, Type] = {}

    def set(self, node: ASTNode, t: Type) -> None:
        self._table[id(node)] = t

    def get(self, node: ASTNode) -> Optional[Type]:
        return self._table.get(id(node))

    def require(self, node: ASTNode) -> Type:
        t = self._table.get(id(node))
        assert t is not None, f"TypeTable.require: no type for {type(node).__name__}"
        return t
