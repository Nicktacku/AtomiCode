from constants import *
from Tokens import *

class Lexer:
    def __init__(self, inp):
        self.inp = inp
        self.index = 0
        self.current = self.inp[self.index]
        self.tokens = []

    def to_token(self):
        while self.index < len(self.inp):
        
            
            
            count = self.current.count(" ")
            

            if self.current in spaces:
                self.move()

            if self.current == None:
                break
            
            not_comment = self.inp[self.index + 1] != "/" if len(self.inp) > self.index + 1 else True
            is_multiplication = self.inp[self.index + 1] == " " if (len(self.inp) > self.index + 1 and self.current == "*") else True
            
            if self.current in digits:
                output = self.tokenize_digit()
                if output == None:
                    return Invalid(self.inp)
                    break
                if "." in output:
                    self.tokens.append(Float(output))
                else:
                    self.tokens.append(Digit(output))
            elif (self.current in operators or self.current in ["&", "|"]) and not_comment and is_multiplication:
                output = self.tokenize_operation()
                
                if output == None:
                    return Invalid(self.inp)
                    break
                self.tokens.append(Operator(output[0], output[1]))
            elif self.current in delimeters:
                output = self.tokenize_delimeter()
                if output == None:
                    return Invalid(self.inp)
                    break
                self.tokens.append(Delimeter(output))
            elif self.current in alphabet:
                output = self.tokenize_lexeme()
                if output == None:
                    return Invalid(self.inp)
                    break
                self.tokens.append(Lexeme(output[0], output[1]))
            elif self.current in special_characters:
                output = self.tokenize_special_characters()
                if output == None:
                    return Invalid(self.inp)
                    break
                self.tokens.append(SpecialChar(output[0], output[1]))
        return self.tokens

    def move(self):
        self.index += 1
        if self.index < len(self.inp):
            self.current = self.inp[self.index]
        else:
            self.current = None

    def tokenize_digit(self):
        numbers = ""
        valid_digits = digits + "."
        while self.current not in spaces and self.current != None and self.current not in delimeters and self.current not in special_characters and self.current not in special_characters:
            if self.current not in valid_digits:
                return None

            numbers += self.current
            self.move()

        if numbers.count(".") > 1:
            return None
        
        return numbers

    def tokenize_operation(self):
        operator = ""
        while self.current != " " and self.current != None:
            operator += self.current
            self.move()
        return (operator, operators[operator])

    def tokenize_delimeter(self):
        delimeter = delimeters[self.current]
        self.move()
        return delimeter

    def tokenize_special_characters(self):
        special_character = ""
        quotes = ["'", '"']
        if self.current in quotes:
            value = ""
            special_character = self.current
            while self.current != " " and self.current != None and (self.current in quotes or self.current in alphabet):
                value += self.current
                self.move()
            if value.endswith(("'", '"')):
                return (value, "String")
            else:
                return None
        elif self.current in comments:
            value = ""
            if self.current == "/":
                while self.current != "\n" and self.current != None:
                    value += self.current
                    self.move()
                if value.startswith("//"):
                    return (value, "Comment")
                else:
                    return None
            elif self.current == "#":
                value += self.current
                self.move()
                while self.current != "#" and self.current != None:
                    value += self.current
                    self.move()
                value += self.current
                self.move()
                if value.startswith("#") and value.endswith("#"):
                    return (value, "MULTILINECOMMENT")
                else:
                    return None
        elif self.current == "*":
            value = ""
            while self.current not in spaces and self.current != None:
                value += self.current
                self.move()
            
            if value in atomic_number:
                return (value, "ATOMICNUMBERLITERAL")
            elif value in atomic_symbol:
                return (value, "ATOMICSYMBOLLITERAL")
            elif value in positive_charge:
                return (value, "POSITIVECHARGELITERAL")
            elif value in negative_charge:
                return (value, "NEGATIVECHARGELITERAL")
            elif value in boyle:
                return (value, "BOYLELITERAL")
            elif value in charles:
                return (value, "CHARLESLITERAL")
            elif value in avogadro:
                return (value, "AVOGADROLITERAL")
            elif value in ideal_gas:
                return (value, "IDEALGASLITERAL")
            elif value in combined_gas:
                return (value, "COMBINEDGASLITERAL")
            else:
                return None
        else:
            special_character += self.current
            self.move()
        return (special_character, special_characters[special_character])

    def tokenize_lexeme(self):
        lexeme = ""
        identifier_valid = True

        while self.current not in spaces and self.current != None and self.current not in special_characters and self.current not in delimeters:
            lexeme_accepted = self.current in digits or self.current in alphabet or self.current == "_"
            if not lexeme_accepted:
                identifier_valid = False
            lexeme += self.current
            self.move()

        if lexeme in keywords:
            return (lexeme, "Keyword")
        elif lexeme in atomic_name:
            return (lexeme, "Atomic_Name")
        elif lexeme in molecular_formula:
            return (lexeme, "Molecular_Formula")
        elif lexeme in booleans:
            return (lexeme, "BOOLEANLITERAL")
        elif lexeme in constants:
            return (lexeme, "CONSTANT")

        if len(self.inp) > self.index + 1:
            if self.inp[self.index + 1] in alphabet:
                lexeme += self.current
                self.move()
                while self.current not in spaces and self.current != None:
                    print(self.current)
                    lexeme += self.current
                    self.move()
                if lexeme in compound_name:
                    return (lexeme, "Compound_Name")
            elif identifier_valid:
                return (lexeme, "Identifier")
        elif identifier_valid:
            return (lexeme, "Identifier")
        


if __name__ == "__main__":
    lexer = Lexer('num1 = 2;')
    print(lexer.to_token())