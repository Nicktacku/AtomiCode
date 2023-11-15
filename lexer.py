from constants import digits, operations
from Tokens import Digit, Float, Operator, Invalid

class Lexer:
    def __init__(self, inp):
        self.inp = inp
        self.index = 0
        self.current = self.inp[self.index]
        self.tokens = []

    def to_token(self):
        while self.index < len(self.inp):
            if self.current == " ":
                self.move()

            if self.current in digits:
                output = self.tokenize_digit()
                if output == None:
                    return Invalid(self.inp)
                    break
                if "." in output:
                    self.tokens.append(Float(output))
                else:
                    self.tokens.append(Digit(output))
            elif self.current in operations:
                output = self.tokenize_operation()
                if output == None:
                    return Invalid(self.inp)
                    break
                self.tokens.append(Operator(output))
        return self.tokens

    def move(self):
        self.index += 1
        if self.index < len(self.inp):
            self.current = self.inp[self.index]
        else:
            self.current = None

    def tokenize_digit(self):
        numbers = ""
        while self.current != " " and self.current != None:
            if self.current not in digits and self.current != ".":
                return None

            numbers += self.current
            self.move()
        return numbers

    def tokenize_operation(self):
        operator = ""
        while self.current != " " and self.current != None:
            operator += self.current
            self.move()
        return operator

if __name__ == "__main__":
    lexer = Lexer("1.2 * 1")
    print(lexer.to_token())