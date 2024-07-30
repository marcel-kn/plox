from ltoken import Token, TokenType
from interpreter import Lox


class Scanner:

    tokens: list[Token] = []

    _start = 0
    _current = 0
    _line = 1

    keywords = {"and": TokenType.AND,
                "class": TokenType.CLASS,
                "else": TokenType.ELSE,
                "false": TokenType.FALSE,
                "for": TokenType.FOR,
                "fun": TokenType.FUN,
                "if": TokenType.IF,
                "nil": TokenType.NIL,
                "or": TokenType.OR,
                "print": TokenType.PRINT,
                "return": TokenType.RETURN,
                "super": TokenType.SUPER,
                "this": TokenType.THIS,
                "true": TokenType.TRUE,
                "var": TokenType.VAR,
                "while": TokenType.WHILE
                }

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
            case "/":
                if self.match("/"):
                    # A comment goes until the end of the line
                    while self.peek() != "\n" and not self.is_at_end():
                        self.advance()
                else:
                    self.add_token(TokenType.SLASH)
            case " ":
                pass
            case "\r":
                pass
            case "\t":
                pass
            case "\n":
                self.line = self.line + 1
            case '"':
                self.string()
            case _:
                if self.is_digit(c):
                    self.number()
                elif self.is_alpha(c):
                    self.identifier()
                else:
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

    def peek(self):
        """
        Look ahead, but don't advance current index
        """
        if self.is_at_end():
            return "\0"
        return self.source[self._current]

    def peek_next(self):
        if self._current + 1 >= len(self.source):
            return "\0"
        return self.source[self._current + 1]

    def add_token(self, type: TokenType, literal=None):
        """
        Create Token from current lexeme
        """
        text = self.source[self._start:self._current]
        self.tokens.append(Token(type, text, literal, self._line))

    def string(self):
        while self.peek() != '"' and not self.is_at_end():
            if self.peek() == "\n":
                self.line = self.line + 1
                self.advance()

        if self.is_at_end():
            Lox.error(self.line, "Unterminated string.")
            return

        # The closing ".
        self.advance()

        # Trim the surrounding quotes.
        value = self.source[self._start + 1: self._current - 1]
        self.add_token(TokenType.STRING, value)

    def is_digit(self, c: str):
        return c >= "0" and c <= "9"

    def number(self):
        while self.is_digit(self.peek()):
            self.advance()

        # look at fractional part
        if (self.peek() == "." and self.is_digit(self.peek_next())):
            # Consume the "."
            self.advance()

            while (self.is_digit(self.peek())):
                self.advance()

        self.add_token(TokenType.NUMBER,
                       float(self.source[self._start:self._current]))

    def identifier(self):
        while self.is_alpha_numeric(self.peek()):
            self.advance()

        text = self.source[self._start:self._current]
        try:
            type = self.keywords[text]
        except:
            type = TokenType.IDENTIFIER

        self.add_token(type)

    def is_alpha(self, c: str):
        return (c >= "a" and c <= "z") or \
            (c >= "A" and c <= "Z") or c == "_"

    def is_alpha_numeric(self, c: str):
        return self.is_alpha(c) and self.is_digit(c)


if __name__ == "__main__":
    s = Scanner("test")
    s.tokens.append(Token(TokenType.FALSE, "false", False, 2))
    print([t.__str__() for t in s.tokens])
