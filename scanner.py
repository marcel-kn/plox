from ltoken import Token, TokenType


class Scanner:

    tokens: list[Token] = []

    _start = 0
    _current = 0
    _line = 1

    def __init__(self, source: str):
        self.source: str = source

    def is_at_end(self) -> bool:
        return self._current >= len(self.source)

    def scan_tokens(self) -> list[Token]:
        while not self.is_at_end():
            # We are at the beginning of the next lexeme.
            self._start = self._current
            self.scan_token()

        self.tokens.append(Token(TokenType.EOF, "", None, self._line))
        return self.tokens

    def scan_token(self):
        pass


if __name__ == "__main__":
    s = Scanner("test")
    s.tokens.append(Token(TokenType.FALSE, "false", False, 2))
    print([t.__str__() for t in s.tokens])
