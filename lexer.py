from constants import *
from Tokens import *
from Errors import *

class Lexer:
    def __init__(self, inp):
        self.inp = inp
        self.index = 0
        self.line = 1
        self.current = self.inp[self.index]
        self.lexemes = []
        self.tokens = []
        self.errors = []


    def to_token(self):

        while self.index < len(self.inp) and self.current != None:
            print("starting ", self.current)
            # skips out spaces
            if self.current in spaces:
                print("space moved ", self.current)
                print("semicolon ", semicolon_appeared)

                if ("\n" in self.current) and not semicolon_appeared:
                    print("semicolon not found")
                    current_index = self.line
                    self.errors.append(SyntaxError("missing semicolon", current_index - 1))
                elif "\n" in self.current:
                    semicolon_appeared = False

                self.move(semicolon_appeared)

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

                    has_error = function_appeared or identifier_appeared or number_appeared or (parenthesis_appeared and function_appeared)

                    if parenthesis_appeared and function_appeared:
                        self.errors.append(SyntaxError("invalid after function keyword", self.line))
                    elif identifier_appeared:
                        self.errors.append(SyntaxError("invalid after an identifier", self.line))
                    elif number_appeared:
                        self.errors.append(SyntaxError("invalid after an number", self.line))
                    elif function_appeared:
                        self.errors.append(SyntaxError("invalid parameter for function", self.line))

                    number_appeared = True
                    operator_appeared = False


                    output = self.tokenize_digit()
                    if "INVALID" in output:
                        self.tokens.append(Invalid(output[0]))
                    elif "." in output:
                        self.tokens.append(Float(output))
                    else:
                        self.tokens.append(Digit(output))

            # *DIGITS
            if self.current in digits:
                print("detected digit 2 ", self.current)

                if (parenthesis_appeared and function_appeared):
                    self.errors.append(SyntaxError("digit invalid as parameter", self.line))
                elif function_appeared:
                    self.errors.append(SyntaxError("digit invalid after function keyword", self.line))
                elif identifier_appeared:
                    self.errors.append(SyntaxError("digit invalid after identifier keyword", self.line))
                elif number_appeared:
                    self.errors.append(SyntaxError("digit invalid after another digit", self.line))

                number_appeared = True
                operator_appeared = False

                output = self.tokenize_digit()
                if "INVALID" in output:
                    self.tokens.append(Invalid(output[0]))
                elif "." in output:
                    self.tokens.append(Float(output))
                else:
                    self.tokens.append(Digit(output))

            # *OPERATORS
            elif (self.current in operators or self.current in ["&", "|"]) and not_comment:
                print("operators ", self.current)
                output = self.tokenize_operation()

                if not number_appeared and not identifier_appeared:
                    print("NOT VALID")
                    print(not number_appeared and not identifier_appeared)
                    self.errors.append(SyntaxError("invalid for operation", self.line))

                if output[0] in assignments:
                    has_error = not identifier_appeared
                    if not identifier_appeared:
                        self.errors.append(SyntaxError("expecting identifier", self.line))

                    identifier_appeared = False
                    operator_appeared = True
                    number_appeared = False

                if "INVALID" in output:
                    self.tokens.append(Invalid(output[0]))
                else:
                    self.tokens.append(Operator(output[0], output[1]))

            # *DELIMETERS
            elif self.current in delimeters:
                print("delimeters ", self.current)

                before_parenthesis = parenthesis_appeared and not (number_appeared or identifier_appeared or string_appeared)

                if operator_appeared:
                    self.errors.append(SyntaxError("operator invalid as parameter", self.line))
                elif before_parenthesis:
                    self.errors.append(SyntaxError("missing parameter", self.line))
                elif (function_appeared and not identifier_appeared):
                    self.errors.append(SyntaxError("missing name for function", self.line))
                print(operator_appeared)

                number_appeared = False
                identifier_appeared = False
                string_appeared = False


                output = self.tokenize_delimeter()
                
                if output == ";":
                    print("HELLO")
                    semicolon_appeared = True
                    number_appeared = False
                    operator_appeared = False
                    string_appeared = False
                    opening_appeared = False
                    function_appeared = False
                    parenthesis_appeared = False
                    identifier_appeared = False
                    keyword_appeared = False
                    conditional_appeared = False
                    loop_appeared = False
                    semicolon_appeared = False

                if "INVALID" in output:
                    self.tokens.append(Invalid(output[0]))
                else:
                    self.tokens.append(Delimeter(output))

            # *ALPHABET*
            elif self.current in alphabet:
                print("alphabet ", self.current)

                output = self.tokenize_lexeme(is_string)

                if output[1] == "IDENTIFIER" and function_appeared:
                    identifier_appeared = True
                    has_error = operator_appeared or number_appeared

                    if operator_appeared or number_appeared:
                        self.errors.append(SyntaxError("identifier expected after function declaration", self.line))

                elif output[1] == "IDENTIFIER":
                    if number_appeared:
                        self.errors.append(SyntaxError("digit invalid before identifier", self.line))
                    elif identifier_appeared:
                        self.errors.append(SyntaxError("cannot have another identifier", self.line))
                    print(number_appeared)
                    identifier_appeared = True
                    operator_appeared = False

                elif output[0] == "def":
                    has_error = operator_appeared or number_appeared or function_appeared or parenthesis_appeared
                    if has_error:
                        self.errors.append(SyntaxError("invalid before function", self.line))
                    function_appeared = True
                elif output[0] == "iter":
                    has_error = operator_appeared or number_appeared or function_appeared or parenthesis_appeared # lagay lahat

                    if has_error:
                        self.errors.append(SyntaxError("invalid before iter", self.line))

                    loop_appeared = True
                elif output[0] == "in":
                    if loop_appeared and not identifier_appeared:
                        self.errors.append(SyntaxError("missing identifier before in", self.line))
                    identifier_appeared = False
                    number_appeared = False
                elif operator_appeared:
                    self.errors.append(SyntaxError("cannot do operation on keywords"), self.line)
                else:
                    has_error = keyword_appeared
                    if keyword_appeared:
                        self.errors.append(SyntaxError("cannot have another keyword"), self.line)
                    keyword_appeared = True
                    print("AKO ANG LUMITAW")

                if "INVALID" in output:
                    self.tokens.append(Invalid(output[0]))
                else:
                    self.tokens.append(Lexeme(output[0], output[1]))

            # *SPECIAL CHARACTERS
            elif self.current in special_characters:
                quotations = ["'", '"']
                print("special characters ", self.current)
                has_error = function_appeared or identifier_appeared

                if operator_appeared:
                    self.errors.append(SyntaxError("cannot have operator before special character"), self.line)
                elif number_appeared:
                    self.errors.append(SyntaxError("cannot have digit before special character", self.line))
                elif function_appeared:
                    self.errors.append(SyntaxError("cannot have digit before special character", self.line))

                if self.current in quotations:
                    output = self.tokenize_string()
                    if "INVALID" in output:
                        self.tokens.append(Invalid(output[0]))
                    else:
                        self.tokens.append(SpecialChar(output[0], output[1]))

                    output = self.tokenize_string()
                    if "INVALID" in output:
                        self.tokens.append(Invalid(output[0]))
                    else:
                        self.tokens.append(Lexeme(output[0], output[1]))

                    output = self.tokenize_string()
                    if "INVALID" in output:
                        self.tokens.append(Invalid(output[0]))
                    else:
                        self.tokens.append(SpecialChar(output[0], output[1]))
                    continue
                elif self.current == "_":
                    output = self.tokenize_lexeme()
                else:
                    output = self.tokenize_special_characters()

                if output[0] == "(":
                    has_error = operator_appeared or (number_appeared and not identifier_appeared) or (function_appeared and not identifier_appeared) or parenthesis_appeared
                    print(number_appeared and not identifier_appeared)
                    identifier_appeared = False
                    parenthesis_appeared = True
                elif output[0] == "{":
                    has_error = operator_appeared or (identifier_appeared and not loop_appeared) or (function_appeared and not parenthesis_closed) or number_appeared
                    print(number_appeared)
                    function_appeared = False
                    identifier_appeared = False
                    semicolon_appeared = True

                if output[0] in [")"] and (number_appeared or identifier_appeared):
                    parenthesis_appeared = False
                    parenthesis_closed = True
                    identifier_appeared = False
                    number_appeared = False
                    keyword_appeared = False
                    self.tokens.append(SpecialChar(output[0], output[1]))
                elif output[0] in ["}"] and (number_appeared or identifier_appeared or semicolon_appeared):
                    curly_braces_appeared = False
                    print("HELLO MY PREND")

                    self.tokens.append(SpecialChar(output[0], output[1]))
                elif "INVALID" in output:
                    self.tokens.append(Invalid(output[0]))
                else:
                    print(self.current)
                    self.tokens.append(SpecialChar(output[0], output[1]))

            # *FLOAT
            elif self.current == ".":
                number_appeared = True
                operator_appeared = False

                has_error = function_appeared or identifier_appeared or (parenthesis_appeared and function_appeared)

                print("float", self.current)
                output = self.tokenize_digit()
                if output == None or has_error:
                    return Invalid(self.current)
                else:
                    self.tokens.append(Float(output))

            else:
                print("else checker ", self.current)
                if self.current in spaces:
                    self.move(semicolon_appeared)
                else:
                    invalid = ""
                    while self.current not in spaces and self.current is not None:
                        invalid += self.current
                        self.move(semicolon_appeared)
                    self.tokens.append(Invalid(invalid))

                if self.current is None:
                    break
        print("total lines: ",self.line)
        print("errors", self.errors)
        return self.tokens

    def move(self, semicolon_appeared):
        self.index += 1
        if self.index < len(self.inp):
            self.current = self.inp[self.index]
            if "\n" in self.current:
                self.line += 1
        else:
            self.current = None
            print("semicolon: ", semicolon_appeared)

    def tokenize_digit(self):
        numbers = ""
        unary_signs = ["-", "+"]
        valid_digits = digits + "." + "-" + "+"
        not_digit = False

        while self.current not in spaces and self.current != None and self.current in valid_digits:
            numbers += self.current
            print("here in number")
            if self.current not in valid_digits:
                not_digit = True
                while self.current not in spaces and self.current != None:
                    numbers += self.current
                    self.move(semicolon_appeared)
            else:
                self.move(semicolon_appeared)
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
            self.move(semicolon_appeared)
        if operator in operators:
            return (operator, operators[operator])
        else:
            return (operator, "INVALID")

    def tokenize_delimeter(self):
        delimeter = self.current
        self.move(semicolon_appeared)
        if delimeter in delimeters:
            return delimeter
        else:
            return (delimeter, "INVALID")

    def tokenize_special_characters(self):
        # for at atomic data types
        if self.current == "@":
            value = ""
            value += self.current
            self.move(semicolon_appeared)
            while self.current != None and self.current not in spaces and self.current not in operators and self.current not in special_characters:
                value += self.current
                self.move(semicolon_appeared)

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
        if self.current == "/" and self.inp[self.index] == "/":
            self.move(semicolon_appeared)
            self.move(semicolon_appeared)
            return ("//", "SINGLELINECOMMENT")

        
        special_character = self.current
        self.move(semicolon_appeared)
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

            self.move(semicolon_appeared)
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
            self.move(semicolon_appeared)
            return (value, special_characters[value])
        else:
            while self.current != None and self.current not in quotations:
                value += self.current
                self.move(semicolon_appeared)
            return (value, "STRING")



if __name__ == "__main__":
    f = open("sample.atc", "r")
    lexer = Lexer(f.read())
    print(lexer.to_token())