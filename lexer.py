from constants import *
from Tokens import *

class Lexer:
    def __init__(self, inp):
        self.inp = inp
        self.index = 0
        self.current = self.inp[self.index]
        self.lexemes = []
        self.tokens = []

    def to_token(self):
        number_appeared = False
        while self.index < len(self.inp):
            count = self.current.count(" ")

            if self.current in spaces:
                self.move()

            if self.current == None:
                break

            not_comment = self.inp[self.index + 1] != "/" if len(self.inp) > self.index + 1 else True

            if (self.current == "-" or self.current == "+") and not number_appeared:
                number_appeared = True
                output = self.tokenize_digit()
                if output == None:
                    return Invalid(self.inp)
                if "." in output:
                    self.tokens.append(Float(output))
                else:
                    self.tokens.append(Digit(output))

            elif self.current in digits:
                number_appeared = True
                output = self.tokenize_digit()
                if output == None:
                    return Invalid(self.inp)
                    break
                if "." in output:
                    self.tokens.append(Float(output))
                else:
                    self.tokens.append(Digit(output))
            elif (self.current in operators or self.current in ["&", "|"]) and not_comment:
                number_appeared = False

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
                self.tokens.append(SpecialChar(output[0], output[1]))
            elif self.current == ".":
                    output = self.tokenize_digit()
                    if output == None:
                        return Invalid(self.inp)
                    self.tokens.append(Float(output))
        return self.tokens

    def move(self):
        self.index += 1
        if self.index < len(self.inp):
            self.current = self.inp[self.index]
        else:
            self.current = None

    def tokenize_digit(self):
        numbers = ""
        valid_digits = digits + "." + "-" + "+"
        
        while self.current not in spaces and self.current != None and self.current not in delimeters and self.current not in special_characters:
            if self.current not in valid_digits:
                return None

            numbers += self.current
            self.move()


        
        if numbers.count(".") > 1:
            return None

        return numbers

    def tokenize_operation(self):
        operator = ""
        while self.current != " " and self.current != None and self.current not in digits:
            operator += self.current
            self.move()
        return (operator, operators[operator])

    def tokenize_delimeter(self):
        delimeter = self.current
        self.move()
        return delimeter

    def tokenize_special_characters(self):
        special_character = ""
        quotes = ["'", '"']
        if self.current in quotes:
            value = ""
            value += self.current
            self.move()
            while self.current not in quotes and self.current != None:
                value += self.current
                self.move()
            value += self.current
            self.move()

            if value.endswith(("'", '"')):
                return (value, "STRING")
            else:
                return None
        elif self.current in comments:
            value = ""
            if self.current == "/":
                while self.current != "\n" and self.current != None:
                    value += self.current
                    self.move()
                if value.startswith("//"):
                    return (value, "COMMENT")
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
        elif self.current == "@":
            value = ""
            while self.current != None and self.current not in spaces and self.current not in operators:
                value += self.current
                self.move()

            if value in at_num:
                return (value, "ATOMICNUMBERLITERAL")
            elif value in alkali_list:
                return (value, "ALKALISYMBOLLITERAL")
            elif value in alkaline_earth_list:
                return (value, "ALKALINEEARTHSYMBOLLITERAL")
            elif value in icosagens_list:
                return (value, "ICOSAGENSSYMBOLLITERAL")
            elif value in crystal_list:
                return (value, "CRYSTALSYMBOLLITERAL")
            elif value in pnicto_list:
                return (value, "PNICTOSYMBOLLITERAL")
            elif value in chalco_list:
                return (value, "CHALCOSYMBOLLITERAL")
            elif value in halo_list:
                return (value, "HALOSYMBOLLITERAL")
            elif value in noble_list:
                return (value, "NOBLESYMBOLLITERAL")
            elif value in n_alkali_list:
                return (value, "ALKALINAMELITERAL")
            elif value in n_alkaline_earth_list:
                return (value, "ALKALINEEARTHNAMELITERAL")
            elif value in n_icosagens_list:
                return (value, "ICOSAGENSNAMELITERAL")
            elif value in n_crystal_list:
                return (value, "CRYSTALNAMELITERAL")
            elif value in n_pnicto_list:
                return (value, "PNICTONAMELITERAL")
            elif value in n_chalco_list:
                return (value, "CHALCONAMELITERAL")
            elif value in n_halo_list:
                return (value, "HALONAMELITERAL")
            elif value in n_noble_list:
                return (value, "NOBLENAMELITERAL")
            else:
                return None
        # elif self.current == ".":
        #     value = ""
        #     while self.current not in spaces and self.current != None and self.current not in delimeters and self.current not in special_characters and self.current not in operators:
        #         value += self.current
        #         self.move()
        #     return value
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
            return (lexeme, "KEYWORD")
        elif lexeme in booleans:
            return (lexeme, "BOOLEANLITERAL")
        elif lexeme in metals:
            return (lexeme, "METALSYMBOLLITERAL")
        elif lexeme in non_metals:
            return (lexeme, "NONMETALSYMBOLLITERAL")
        elif lexeme in metalloids:
            return (lexeme, "METALLOIDSSYMBOLLITERAL")
        elif lexeme in n_metals:
            return (lexeme, "METALNAMELITERAL")
        elif lexeme in n_non_metals:
            return (lexeme, "NONMETALNAMELITERAL")
        elif lexeme in n_metalloids:
            return (lexeme, "METALLOIDSNAMELITERAL")
        elif lexeme in constants:
            return (lexeme, "CONSTANT")
        elif identifier_valid:
            return (lexeme, "IDENTIFIER")



if __name__ == "__main__":
    lexer = Lexer('num1 = 2;')
    print(lexer.to_token())