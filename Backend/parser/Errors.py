class Error:
    def __init__(self, error, detail, line, lexeme):
        self.error = error
        self.detail = detail
        self.line = line
        self.lexeme = lexeme

    def __str__(self):
        return f"{self.error}: {self.detail} in line {self.line}"

    def __repr__(self):
        return f"{self.error}: {self.detail} in line {self.line}"

class LexicalError(Error):
    def __init__(self, detail, line, lexeme):
        super().__init__("LexicalError", detail, line, lexeme)

class SyntaxError(Error):
    def __init__(self, detail, line, lexeme):
        super().__init__("SyntaxError", detail, line, lexeme)

class IllegalLexError(Error):
    def __init__(self, detail, line, lexeme):
        super().__init__("IllegalLexError", detail, line, lexeme)