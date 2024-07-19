from ltoken import Token, TokenType
from interpreter import Lox


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
        c = self.advance()
        match c:
            case "(":
                self.add_token(TokenType.LEFT_PAREN)
            case ")":
                self.add_token(TokenType.RIGHT_PAREN)
            case "{":
                self.add_token(TokenType.LEFT_BRACE)
            case "}":
                self.add_token(TokenType.RIGHT_BRACE)
            case ",":
                self.add_token(TokenType.COMMA)
            case ".":
                self.add_token(TokenType.DOT)
            case "-":
                self.add_token(TokenType.MINUS)
            case "+":
                self.add_token(TokenType.PLUS)
            case ";":
                self.add_token(TokenType.SEMICOLON)
            case "*":
                self.add_token(TokenType.STAR)
            case "!":
                self.add_token(TokenType.BANG_EQUAL
                               if self.match("=")
                               else TokenType.BANG)
            case "=":
                self.add_token(TokenType.EQUAL_EQUAL
                               if self.match("=")
                               else TokenType.EQUAL)
            case "<":
                self.add_token(TokenType.LESS_EQUAL
                               if self.match("=")
                               else TokenType.LESS)
            case ">":
                self.add_token(TokenType.GREATER_EQUAL
                               if self.match("=")
                               else TokenType.GREATER)
            case _:
                Lox.error(self._line, "Unexpected character.")

    def match(self, expected: str) -> bool:
        """
        Check if next character is a specific character
        """
        if self.is_at_end():
            return False
        if not self.source[self._current] == expected:
            return False

        self._current += 1
        return True

    def advance(self) -> str:
        """
        Consume next character in the source code and return it
        """
        looking_at = self.source[self._current]
        self._current += 1
        return looking_at

    def add_token(self, type: TokenType, literal=None):
        """
        Create Token from current lexeme
        """
        text = self.source[self._start:self._current]
        self.tokens.append(Token(type, text, literal, self._line))


if __name__ == "__main__":
    s = Scanner("test")
    s.tokens.append(Token(TokenType.FALSE, "false", False, 2))
    print([t.__str__() for t in s.tokens])
