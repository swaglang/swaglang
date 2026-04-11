from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from compiler.ast.nodes import ASTNode, Type

class SymbolKind(Enum):
    VARIABLE  = "variable"
    FUNCTION  = "function"
    INTERFACE = "interface"
    PARAMETER = "parameter"

@dataclass
class Symbol:
    name: str
    kind: SymbolKind
    type: Optional[Type] # None for FUNCTION and INTERFACE
    is_mutable: bool
    decl_node: Optional[ASTNode] # None only for built-ins
    defined_at: tuple[int, int] = field(default_factory=lambda: (0, 0))

class Scope:
    def __init__(self) -> None:
        self._symbols: dict[str, Symbol] = {}

    def define(self, symbol: Symbol) -> bool:
        """Returns False if the name is already defined in this scope."""
        if symbol.name in self._symbols:
            return False
        self._symbols[symbol.name] = symbol
        return True

    def get(self, name: str) -> Optional[Symbol]:
        return self._symbols.get(name)

class SymbolTable:
    def __init__(self) -> None:
        self._scopes: list[Scope] = [Scope()] # index 0 = global scope

    def enter_scope(self) -> None:
        self._scopes.append(Scope())

    def exit_scope(self) -> None:
        if len(self._scopes) > 1:
            self._scopes.pop()

    def define(self, symbol: Symbol) -> bool:
        """Define in current scope. Returns False on redefinition."""
        return self._scopes[-1].define(symbol)

    def lookup(self, name: str) -> Optional[Symbol]:
        """Walk the scope stack from innermost to outermost."""
        for scope in reversed(self._scopes):
            sym = scope.get(name)
            if sym is not None:
                return sym
        return None

    def lookup_at(self, line: int, col: int) -> Optional[Symbol]:
        """LSP hook — returns None until AST nodes carry source positions."""
        return None
