from dataclasses import dataclass


@dataclass
class SemanticError:
    kind: str       # "NameError" | "TypeError" | "ControlFlowError" | "InterfaceError" | "RedefinitionError"
    filename: str
    line: int       # 0 until AST nodes carry source positions
    column: int     # 0 until AST nodes carry source positions
    message: str

    def __str__(self) -> str:
        return self.message.replace(
            f"[{self.kind}]",
            f"\033[1;31m[{self.kind}]\033[0m",
            1,
        )
