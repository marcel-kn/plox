import sys
from ltoken import Token, TokenType


class Lox():

    had_error = False

    def __init__(self):
        """
        When one file name as argument is provided, 
        run the interpreter on the file. 
        When no argument is provided, run in prompt mode.
        """
        if len(sys.argv) > 2:
            print("Usage: plox [script]")
            sys.exit(64)
        elif len(sys.argv) == 2:
            self.run_file(sys.argv[1])
        else:
            self.run_prompt()

    def run_file(self, path):
        """
        Open a provided file path and
        run the interpreter on it.
        """
        f = open(path, "r")
        print(f.read())
        self.run(f.read())

    def run_prompt(self):
        """
        Run a prompt mode (REPL)
        that runs the interpreter on every entered line.
        Stops on empty line.
        """
        while (True):
            print("> ", end="")
            line = input()
            if line == "":
                break
            self.run(line)

    def run(self, code: str):
        scanner = Scanner(code)
        tokens = scanner.scan_tokens()
        # for now just print the tokens
        for token in tokens:
            print(token)

    def error(self, line: int, message: str):
        self.report(line, "", message)

    def report(self, line: int, where: str, message: str):
        raise NameError("[line " + str(line) + "] Error" +
                        where + ": " + message)
        had_error = True


class Scanner:
    def __init__(self, code: str):
        pass

    def scan_tokens(self):
        return []


if __name__ == "__main__":
    lox = Lox()
    t = Token(TokenType.NUMBER, "5", 5, 1)
    print(t.__str__())
