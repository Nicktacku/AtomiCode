from constants import *
from Tokens import *

class Lexer:
    def __init__(self, inp):
        self.inp = inp
        self.index = 0
        self.line = 1
        self.current = self.inp[self.index]
        self.lexemes = []
        self.tokens = []


    def to_token(self):
        is_string = False
        number_appeared = False
        while self.index < len(self.inp) and self.current != None:
            print("starting ", self.current)
            # skips out spaces
            if self.current in spaces:
                print("space moved ", self.current)
                print("semicolon ", )


                self.move()

                if self.current is None:
                    print("in none ", self.current)
                    
                    break

                    print("nag move na pre")

            # defines if its a comment or divide
            not_comment = self.inp[self.index + 1] != "/" if len(self.inp) > self.index + 1 else True

            # *NUMBER WITH SIGN
            if 1 < len(self.inp):
                if (self.current == "-" or self.current == "+") and not number_appeared and self.inp[self.index + 1] in digits:
                    print("detected digit 1", self.current)
                    
                    number_appeared = True
                    operator_appeared = False

                    output = self.tokenize_digit()
                    if "INVALID" in output:
                        self.tokens.append(Invalid(output[0], self.line))
                    elif "." in output:
                        self.tokens.append(Float(output, self.line))
                    else:
                        self.tokens.append(Digit(output, self.line))

            # *DIGITS
            if self.current in digits:
                print("detected digit 2 ", self.current)
                number_appeared = True
                operator_appeared = False

                output = self.tokenize_digit()
                if "INVALID" in output:
                    self.tokens.append(Invalid(output[0], self.line))
                elif "." in output:
                    self.tokens.append(Float(output, self.line))
                else:
                    self.tokens.append(Digit(output, self.line))

            # *OPERATORS
            elif (self.current in operators or self.current in ["&", "|"]) and not_comment:
                print("operators ", self.current)
                operator_appeared = True
                number_appeared = False
                output = self.tokenize_operation()

                if "INVALID" in output:
                    self.tokens.append(Invalid(output[0], self.line))
                else:
                    self.tokens.append(Operator(output[0], output[1], self.line))

            # *DELIMETERS
            elif self.current in delimeters:
                print("delimeters ", self.current)
                output = self.tokenize_delimeter()

                if "INVALID" in output:
                    self.tokens.append(Invalid(output[0], self.line))
                else:
                    self.tokens.append(Delimeter(output, self.line))

            # *ALPHABET*
            elif self.current in alphabet:
                print("alphabet ", self.current)

                output = self.tokenize_lexeme(is_string)

                if "INVALID" in output:
                    self.tokens.append(Invalid(output[0], self.line))
                else:
                    self.tokens.append(Lexeme(output[0], output[1], self.line))

            # *SPECIAL CHARACTERS
            elif self.current in special_characters:
                quotations = ["'", '"']
                comments = ["/", "#"]
                print("special characters ", self.current)


                if self.current in quotations:
                    output = self.tokenize_string()
                    if "INVALID" in output:
                        self.tokens.append(Invalid(output[0], self.line))
                    else:
                        self.tokens.append(SpecialChar(output[0], output[1], self.line))

                    output = self.tokenize_string()
                    if "INVALID" in output:
                        self.tokens.append(Invalid(output[0], self.line))
                    else:
                        self.tokens.append(Lexeme(output[0], output[1], self.line))

                    output = self.tokenize_string()
                    if "INVALID" in output:
                        self.tokens.append(Invalid(output[0], self.line))
                    else:
                        self.tokens.append(SpecialChar(output[0], output[1], self.line))
                    continue
                elif self.current in comments:
                    if self.current == "/":
                        output = self.tokenize_comment()
                        self.tokens.append(SpecialChar(output[0], output[1], self.line))

                        output = self.tokenize_comment()
                        self.tokens.append(Lexeme(output[0], output[1], self.line))
                        continue

                    elif self.current == "#":
                        output = self.tokenize_comment()
                        self.tokens.append(SpecialChar(output[0], output[1], self.line))

                        output = self.tokenize_comment()
                        self.tokens.append(Lexeme(output[0], output[1], self.line))

                        output = self.tokenize_comment()
                        if output is not None:
                            self.tokens.append(SpecialChar(output[0], output[1], self.line))
                        continue
                elif self.current == "_":
                    output = self.tokenize_lexeme()
                else:
                    output = self.tokenize_special_characters()

                if "INVALID" in output:
                    self.tokens.append(Invalid(output[0], self.line))
                else:
                    print("else of special chars", self.current)
                    self.tokens.append(SpecialChar(output[0], output[1], self.line))

            # *FLOAT
            elif self.current == ".":

                print("float", self.current)
                output = self.tokenize_digit()
                if output == None:
                    return Invalid(self.current)
                else:
                    self.tokens.append(Float(output, self.line))

            else:
                print("else checker ", self.current)
                if self.current in spaces:
                    self.move()
                else:
                    illegal = ""
                    while self.current not in spaces and self.current is not None:
                        illegal += self.current
                        self.move()
                    self.tokens.append(Illegal(illegal, self.line))

                if self.current is None:
                    print("currently non")
                    break
        print("end current", self.current)
        print("total lines: ", self.line)
        
        self.tokens.append(Eof(self.line))
        return self.tokens

    def move(self):
        self.index += 1
        if self.index < len(self.inp):
            self.current = self.inp[self.index]
            if "\n" in self.current:
                self.line += 1
        else:
            self.current = None

    def tokenize_digit(self):
        numbers = ""
        unary_signs = ["-", "+"]
        valid_digits = digits + "." + "-" + "+"
        not_digit = False

        while self.current not in spaces and self.current != None and self.current not in delimeters and self.current != ")":
            numbers += self.current
            print("here in number")
            if self.current not in valid_digits:
                not_digit = True
                while self.current not in spaces and self.current != None:
                    numbers += self.current
                    self.move()
            else:
                self.move()
                if self.current in ["+", "-"]:
                    break

        if not_digit:
            return (numbers, "INVALID")

        if numbers.count(".") > 1:
            return (numbers, "INVALID")

        return numbers

    def tokenize_operation(self):
        operator = ""
        while self.current != " " and self.current != None and self.current not in digits and self.current not in delimeters:
            operator += self.current
            self.move()
        if operator in operators:
            return (operator, operators[operator])
        else:
            return (operator, "INVALID")

    def tokenize_delimeter(self):
        delimeter = self.current
        self.move()
        if delimeter in delimeters:
            return delimeter
        else:
            return (delimeter, "INVALID")

    def tokenize_special_characters(self):
        # for at atomic data types
        if self.current == "@":
            value = ""
            value += self.current
            self.move()
            while self.current != None and self.current not in spaces and self.current not in operators and self.current not in special_characters:
                value += self.current
                self.move()

                if self.current in upper_alphabet:
                    if self.inp[self.index + 1] in upper_alphabet:
                        break


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
                return (value, "INVALID")


        # for comments

        
        special_character = self.current
        self.move()
        return (special_character, special_characters[special_character])


    def tokenize_lexeme(self, is_string):
        lexeme = ""
        valid_identifier = alphabet + "_" + digits
        identifier_valid = True

        while self.current not in spaces and self.current != None and self.current in valid_identifier:
            lexeme_accepted = self.current in digits or self.current in alphabet or self.current == "_"

            if self.current not in valid_identifier:
                identifier_valid = False

            lexeme += self.current

            self.move()
        if is_string:
            return(lexeme, "STRING")
        elif lexeme in keywords:
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
        
    def tokenize_string(self):
        print("entered")
        value = ""
        quotations = ["'", '"']
        
        if self.current in quotations:
            value += self.current
            self.move()
            return (value, special_characters[value])
        else:
            while self.current != None and self.current not in quotations:
                value += self.current
                self.move()
            return (value, "STRING")

    def tokenize_comment(self):
        output = ""
        if self.current == "/" and self.inp[self.index + 1] == "/":
            self.move()
            self.move()
            return ("//", "SINGLELINECOMMENT")
        else:
            print("IN SINGLELINE COMMENT: ", self.current)
            while self.current is not None and not "\n" in self.current:
                print("IN SINGLELINE COMMENT: ", self.current)
                output += self.current
                self.move()
            return (output, "COMMENTLITERAL")

        if self.current == "#":
            self.move()
            return ("#", "MULTILINECOMMENT")
        elif self.inp[self.index - 1] == "#":
            while self.current is not None and self.current != "#":
                output += self.current
                self.move()
            return (output, "COMMENTLITERAL")



if __name__ == "__main__":
    f = open("sample.atc", "r")
    lexer = Lexer(f.read())
    print(lexer.to_token())