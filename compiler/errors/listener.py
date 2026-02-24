import re
from dataclasses import dataclass
from typing import ClassVar

from antlr4.error.ErrorListener import ErrorListener


class SwagError:

    def __init__(self, kind: str, filename: str, line: int, column: int, message: str):
        self.kind = kind
        self.filename = filename
        self.line = line
        self.column = column
        self.message = message

    def __str__(self) -> str:
        return self.message.replace(
            f"[{self.kind}]",
            f"\033[1;31m[{self.kind}]\033[0m",
            1,
        )


_PAT_MISMATCHED = re.compile(r"mismatched input '(.+)' expecting (.+)")
_PAT_EXTRANEOUS = re.compile(r"extraneous input '(.+)' expecting (.+)")
_PAT_NO_VIABLE = re.compile(r"no viable alternative at input '(.+)'")
_PAT_LEX_ERROR = re.compile(r"token recognition error at: '(.+)'", re.IGNORECASE)
_PAT_MISSING = re.compile(r"missing (.+) at '(.+)'")


def _split_expectation(raw: str) -> list[str]:
    s = raw.strip()
    if s.startswith("{") and s.endswith("}"):
        s = s[1:-1].strip()

    parts: list[str] = []
    buf: list[str] = []
    in_quote = False

    for char in s:
        if char == "'" and not in_quote:
            in_quote = True
            buf.append(char)
        elif char == "'" and in_quote:
            in_quote = False
            buf.append(char)
        elif char == "," and not in_quote:
            token = "".join(buf).strip()
            if token:
                parts.append(token)
            buf = []
        else:
            buf.append(char)

    if buf:
        token = "".join(buf).strip()
        if token:
            parts.append(token)

    result: list[str] = []
    for p in parts:
        if p.startswith("'") and p.endswith("'") and len(p) > 2:
            result.append(p[1:-1])
        elif p.startswith('"') and p.endswith('"') and len(p) > 2:
            result.append(p[1:-1])
        else:
            result.append(p)

    return [r for r in result if r]


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
        "EOF": "end of file",
        "NEWLINE": "newline",
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
    }

    def _token_to_human(self, token: str, recognizer) -> str:
        if token in self._token_names:
            return self._token_names[token]

        if len(token) == 1 and not token.isalnum() and token != "_":
            return f"'{token}'"

        if token.isdigit():
            try:
                return recognizer.getVocabulary().getDisplayName(int(token))
            except Exception:
                pass

        return token.lower()

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
        self._reported_positions: set[tuple[int, int]] = set()

    @property
    def has_errors(self) -> bool:
        return bool(self.errors)

    def syntaxError(self, recognizer, baddieSymbol, line: int, column: int, msg: str, e) -> None:
        """
        recognizer: parser
        baddieSymbol: Token (maybe None or a token object)
        line, column: int
        msg: raw ANTLR string
        e: RecognitionException or None
        """
        if (line, column) in self._reported_positions:
            return

        if baddieSymbol and baddieSymbol.type == recognizer.EOF:
            return

        self._reported_positions.add((line, column))

        kind, text = self._classify(msg, recognizer, baddieSymbol)
        error = SwagError(
            kind,
            self.filename,
            line,
            column,
            f"[{kind}] {self.filename}:{line}:{column} - {text}")

        self.errors.append(error)
        print(error)

    def _classify(self, msg: str, recognizer, baddieSymbol=None) -> tuple[str, str]:
        m = _PAT_MISMATCHED.match(msg)
        if m:
            off = baddieSymbol.text if baddieSymbol else m.group(1)
            expect_raw = m.group(2)
            expected = self._humanize_expectation(expect_raw, recognizer)
            return "SyntaxError", f"unexpected '{off}', expected {expected}"

        m = _PAT_EXTRANEOUS.match(msg)
        if m:
            off, expect_raw = m.group(1), m.group(2)
            expected = self._humanize_expectation(expect_raw, recognizer)
            return "SyntaxError", f"extraneous '{off}', expected {expected}"

        m = _PAT_MISSING.match(msg)
        if m:
            what, where = m.group(1), m.group(2)
            expected = self._humanize_expectation(what, recognizer)
            return "SyntaxError", f"missing {expected} before '{where}'"

        m = _PAT_NO_VIABLE.match(msg)
        if m:
            return "SyntaxError", f"unexpected '{m.group(1)}'"

        m = _PAT_LEX_ERROR.match(msg)
        if m:
            return "LexError", f"invalid token '{m.group(1)}'"

        return "SyntaxError", msg

    def _humanize_expectation(self, expect_raw: str, recognizer) -> str:
        tokens = _split_expectation(expect_raw)
        if not tokens:
            return "something else ¯\_(ツ)_/¯ idk"

        upper = {t.upper() for t in tokens}

        if len(tokens) > 3 and upper & self._STMT_STARTERS:
            return "a statement ඞ"

        if len(tokens) == 1:
            return self._token_to_human(tokens[0], recognizer)

        seen: list[str] = []
        for tiktok in tokens:
            human = self._token_to_human(tiktok, recognizer)
            if human not in seen:
                seen.append(human)
            if len(seen) >= self._MAX_ALTERNATIVES:
                break

        return "one of: " + ", ".join(seen)
