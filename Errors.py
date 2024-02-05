class Error:
    def __init__(self, error, detail, line):
        self.error = error
        self.detail = detail
        self.line = line

    def __str__(self):
        return f"{self.error}: {self.detail} in line {self.line}"

    def __repr__(self):
        return f"{self.error}: {self.detail} in line {self.line}"

class LexicalError(Error):
    def __init__(self, detail, line):
        super().__init__("LexicalError", detail, line)

class SyntaxError(Error):
    def __init__(self, detail, line):
        super().__init__("SyntaxError", detail, line)

class IllegalLexError(Error):
    def __init__(self, detail, line):
        super().__init__("IllegalLexError", detail, line)