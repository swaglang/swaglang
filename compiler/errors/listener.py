import re
from typing import ClassVar

from antlr4.error.ErrorListener import ErrorListener


class SwagError:
    kind: str
    filename: str
    line: int
    column: int
    message: str

    def __str__(self) -> str:
        return self.message


_PAT_MISMATCHED = re.compile(r"mismatched input '(.+)' expecting (.+)")
_PAT_EXTRANEOUS = re.compile(r"extraneous input '(.+)' expecting (.+)")
_PAT_NO_VIABLE = re.compile(r"no viable alternative at input '(.+)'")
_PAT_LEX_ERROR = re.compile(r"token recognition error at: '(.+)'", re.IGNORECASE)
_PAT_MISSING = re.compile(r"missing (.+) at '(.+)'")


class SwagErrorListener(ErrorListener):
    TOKEN_NAMES: ClassVar[dict[str, str]] = {
        # main
        "IDENT": "identifier",
        "INT": "integer",
        "FLOAT": "float",
        "STRING": "string literal",
        "BOOL": "boolean",
        "TYPE": "type",
        "ACCESS_MOD": "access modifier ('const' or 'let')",
        "IF": "'if'",
        "ELSE": "'else'",
        "ELIF": "'elif'",
        "WHILE": "'while'",
        "DO": "'do'",
        "FOR": "'for'",
        "IN": "'in'",
        "RETURN": "'return'",
        "BREAK": "'break'",
        "DEFER": "'defer'",
        "NULL": "'null'",
        # symbols
        "SEMI": "';'",
        "COLON": "':'",
        "COMMA": "','",
        "DOT": "'.'",
        "LCURLY": "'{'",
        "RCURLY": "'}'",
        "LPAREN": "'('",
        "RPAREN": "')'",
        "LBRACKET": "'['",
        "RBRACKET": "']'",
        # smooth operator...
        "ASSIGN": "'='",
        "ADD_ASSIGN": "'+='",
        "SUB_ASSIGN": "'-='",
        "MUL_ASSIGN": "'*='",
        "DIV_ASSIGN": "'/='",
        "MOD_ASSIGN": "'%='",
        "INC": "'++'",
        "DEC": "'--'",
        "QUESTION": "'?'",
        # other
        "EOF": "end of file",
        "NEWLINE": "newline",
    }

    _STMT_STARTERS: ClassVar[frozenset[str]] = frozenset({
        "IDENT", "LET", "CONST", "ACCESS_MOD",
        "IF", "WHILE", "DO", "FOR",
        "RETURN", "BREAK", "DEFER",
        "TYPE",
    })

    _MAX_ALTERNATIVES: ClassVar[int] = 4

    def __init__(self, filename: str = "<input>", extra_token_names: dict[str, str] | None = None) -> None:
        super().__init__()
        self.filename = filename
        self._token_names: dict[str, str] = {**self.TOKEN_NAMES, **(extra_token_names or {})}
        self.errors: list[SwagError] = []

    def syntaxError(self, recognizer, baddieSymbol, line, column, msg, e):
        """
        recognizer: parser
        baddieSymbol: Token (maybe None or a token object)
        line, column: int
        msg: raw ANTLR string
        e: RecognitionException or None
        """

        off_text = None
        expected_desc = None

        off_text = self.baddie_text_from_symbol(baddieSymbol)
