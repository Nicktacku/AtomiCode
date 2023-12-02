class Token:
    def __init__(self, value, token):
        self.value = value
        self.token = token

class Digit(Token):
    def __init__(self, value):
        super().__init__(value, "DIGIT")

    def __repr__(self):
        return self.token

    def __str__(self):
        return format(self.token, "<25") + self.value


class Float(Token):
    def __init__(self, value):
        super().__init__(value, "Float")

    def __repr__(self):
        return self.token

    def __str__(self):
        return format(self.token, "<25") + self.value


class Operator(Token):
    def __init__(self, value, token):
        super().__init__(value, token)

    def __repr__(self):
        return self.token

    def __str__(self):
        return format(self.token, "<25") + self.value


class Delimeter(Token):
    def __init__(self, value):
        super().__init__(value, "Delimeter")

    def __repr__(self):
        return self.token

    def __str__(self):
        return format(self.token, "<25") + self.value


class SpecialChar(Token):
    def __init__(self, value, token):
        super().__init__(value, token)

    def __repr__(self):
        return self.token

    def __str__(self):
        return format(self.token, "<25") + self.value


class Lexeme(Token):
    def __init__(self, value, token):
        super().__init__(value, token)

    def __repr__(self):
        return self.token

    def __str__(self):
        return format(self.token, "<25") + self.value


class Invalid(Token):
    def __init__(self, value):
        super().__init__(value, "Invalid")

    def __repr__(self):
        return self.token

    def __str__(self):
        return format(self.token, "<25") + self.value
