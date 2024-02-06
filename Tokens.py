class Token:
    def __init__(self, value, token, line):
        self.value = value
        self.token = token
        self.line = line

class Digit(Token):
    def __init__(self, value, line):
        super().__init__(value, "DIGIT", line)

    def __repr__(self):
        return self.token

    def __str__(self):
        return format(self.token, "<25") + self.value


class Float(Token):
    def __init__(self, value, line):
        super().__init__(value, "FLOAT", line)

    def __repr__(self):
        return self.token

    def __str__(self):
        return format(self.token, "<25") + self.value


class Operator(Token):
    def __init__(self, value, token, line):
        super().__init__(value, token, line)

    def __repr__(self):
        return self.token

    def __str__(self):
        return format(self.token, "<25") + self.value


class Delimeter(Token):
    def __init__(self, value, line):
        super().__init__(value, "DELIMETER", line)

    def __repr__(self):
        return self.token

    def __str__(self):
        return format(self.token, "<25") + self.value


class SpecialChar(Token):
    def __init__(self, value, token, line):
        super().__init__(value, token, line)

    def __repr__(self):
        return self.token

    def __str__(self):
        return format(self.token, "<25") + self.value


class Lexeme(Token):
    def __init__(self, value, token, line):
        super().__init__(value, token, line)

    def __repr__(self):
        return self.token

    def __str__(self):
        return format(self.token, "<25") + self.value


class Invalid(Token):
    def __init__(self, value, line):
        super().__init__(value, "INVALID", line)

    def __repr__(self):
        return self.token

    def __str__(self):
        print(self.value)
        return format(self.token, "<25") + self.value

class Eof(Token):
    def __init__(self, line):
        super().__init__("end of file", "EOF", line)

    def __repr__(self):
        return self.token

    def __str__(self):
        return format(self.token, "<25") + self.value
