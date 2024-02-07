from .Tokens import *
from .Errors import *
from .constants import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0
        self.prev = None
        self.current = self.tokens[self.index]
        self.next = None
        self.errors = []


    def show_contents(self):
        for i in self.tokens:
            print(isinstance(i, Operator))

    def parse(self):
        semicolon_appeared = False
        parenthesis_appeared = False
        curlybrace_appeared = False
        assuming_started = False

        assignment_operators = ["=", "+=", "-=", "*=", "/=", "%="]
        comments = ["SINGLINECOMMENT", "MULTILINECOMMENT"]
        builtin_functions = ["out", "inp"]

        while self.index < len(self.tokens):
            if self.current.token == "BACKSLASH":

                self.parse_balancing()
            
            if isinstance(self.current, Operator) and not self.current.value in assignment_operators:
                semicolon_appeared = False
                self.parse_operator()
                
            elif self.current.value in assignment_operators:
                semicolon_appeared = False
                self.parse_assignment()
                continue
                
            elif self.current.token == "QUOTATIONMARK":
                semicolon_appeared = False
                self.parse_string()
                
            elif self.current.value == "def":
                semicolon_appeared = False
                curlybrace_appeared = self.parse_function()
                

            if assuming_started:
                if self.current.token == "RIGHTCURLYBRACE":
                    if self.next_token().value not in ["unless", "than"]:
                        assuming_started = False

            if self.current.value == "assuming":
                semicolon_appeared = False
                assuming_started = True
                curlybrace_appeared = self.parse_control_flow()

            elif self.current.value in ["unless", "than"] and assuming_started:
                semicolon_appeared = False
                curlybrace_appeared = self.parse_control_flow()

            elif self.current.value in ["unless", "than"] and not assuming_started:
                self.errors.append(SyntaxError("Missing assuming statement", self.current.line, self.current.value))
                self.move()

            if self.current.value == "iter":
                semicolon_appeared = False
                curlybrace_appeared = self.parse_looping()
                

            if self.current.token == "RIGHTCURLYBRACE":
                curlybrace_appeared = False
                if self.next_token().value != ";" and (not self.next_token().value in ["unless", "than"] and not assuming_started):
                    self.errors.append(SyntaxError("Missing semicolon", self.current.line, self.current.value))

            if self.current.token in comments:
                self.parse_comment()

            if self.current.value in builtin_functions:
                semicolon_appeared = False
                self.parse_called_function()
            if self.current.token == "IDENTIFIERS" and self.next_token():
                self.parse_called_function()

            if self.current.token == "INVALID":
                self.errors.append(LexicalError("Invalid Value", self.current.line, self.current.value))
                self.move()
            if self.current.token == "ILLEGAL":
                self.errors.append(IllegalLexError("Illegal Character", self.current.line, self.current.value))
                self.move()

            self.move()

            if isinstance(self.current, Eof):
                if curlybrace_appeared:
                    self.errors.append(SyntaxError("Curlybrace not closed", self.current.line, self.current.value))
                break
        print(self.errors)
        return self.errors

    def move(self):
        self.index += 1
        if self.index < len(self.tokens):
            self.current = self.tokens[self.index]

    def next_token(self, set_next=False):
        if set_next:
            if self.index + 1 < len(self.tokens):
                self.next = self.tokens[self.index + 1]
        else:
            if self.index + 1 < len(self.tokens):
                return self.tokens[self.index + 1]

    def prev_token(self, set_prev=False):
        if set_prev:
            if self.index - 1 >= 0:
                self.prev = self.tokens[self.index - 1]
        else:
            if self.index - 1 >= 0:
                return self.tokens[self.index - 1]

    def parse_operator(self):
        self.prev_token(True)
        self.next_token(True)
        operator_valid = True
        semicolon_index = self.current.line


        # idagdag string
        while (self.current.token in ["IDENTIFIER", "DIGIT"] or isinstance(self.current, Operator) and self.current.value != ";"):

            if self.prev.token in ["IDENTIFIER", "DIGIT"] and self.next.token in ["IDENTIFIER", "DIGIT"]:
                semicolon_index = self.current.line
                self.move()
            else:
                operator_valid = False
                self.move()

        if self.current.value == ";":
            self.move()
        else:
            print("in operator error", self.current)
            self.errors.append(SyntaxError("semicolon not found", semicolon_index, self.current.value))

        if not operator_valid:
            self.errors.append(SyntaxError("invalid for operation", semicolon_index, self.current.value))
            self.move()
            return False

    def parse_assignment(self):
        is_string = False
        self.prev_token(True)
        self.next_token(True)
        semicolon_index = self.current.line

        if self.next.token == "QUOTATIONMARK":
            self.move()
            is_string = self.parse_string()
            print("in assignment", self.current)

        print(self.prev.token == "IDENTIFIER" and (self.next.token in ["IDENTIFIER", "DIGIT"] or is_string ))

        if self.prev.token == "IDENTIFIER" and (self.next.token in ["IDENTIFIER", "DIGIT", "CONSTANT"] or is_string or self.next.value == "inp"):
            if self.next.value == "inp":
                self.move()
                self.move()
                if self.current.token == "LEFTROUNDBRACKET":
                    self.move()
                if self.current.token == "QUOTATIONMARK":
                    self.parse_string(True)
                if self.current.token == "RIGHTROUNDBRACKET":
                    self.move()
                if self.current.value == ";":
                    self.move()
                else:
                    self.errors.append(SyntaxError("missing semicolon", self.current.line, self.current.value))
                return
            if is_string:
                return
            self.move()
            self.move()
            if self.current.value == ";":
                self.move()
            elif isinstance(self.current, Operator):
                self.parse_operator()
            else:
                print("assigment error")
                self.errors.append(SyntaxError("semicolon not found (assignment)", semicolon_index, self.current.value))
        else:
            self.errors.append(SyntaxError("invalid for operation (assignment)", self.current.line, self.current.value))
            self.move()
            return False

    def parse_string(self, in_parameter=False):
        
        semicolon_index = self.current.line
        if self.current.token == "QUOTATIONMARK":
            self.move()
            
        if self.current.token == "STRING":
            self.move()
            
        if self.current.token == "QUOTATIONMARK":
            self.move()
            
            if self.current.value == ";" or in_parameter:
                self.move()
            else:
                print("string error")
                self.errors.append(SyntaxError("semicolon not found", semicolon_index, self.current.value))

            return True
        else:
            self.errors.append(SyntaxError("Invalid string", self.current.line, self.current.value))
            self.move()
            return False

    def parse_function(self):
        if self.current.value == "def":
            self.move()
        if self.current.token == "IDENTIFIER":
            self.move()
        if self.current.token == "LEFTROUNDBRACKET":
            self.move()
            while self.current.token != "RIGHTROUNDBRACKET":
                if self.current.token == "IDENTIFIER":
                    self.move()
                    if self.current.value == ",":
                        self.move()
                    elif self.current.token == "RIGHTROUNDBRACKET":
                        self.move()
                        break
                    else:
                        self.move()
                        self.errors.append(SyntaxError("Invalid for parameter", self.current.line, self.current.value))
                else:
                    self.errors.append(SyntaxError("Invalid for parameter", self.current.line, self.current.value))
        if self.current.token == "LEFTCURLYBRACE":
            self.move()
            return True
        else:
            print("else", self.current)
            self.errors.append(SyntaxError("Invalid for function declaration", self.current.line, self.current.value))
            return False

    def parse_control_flow(self):
        unique_values = at_num + metals + non_metals + metalloids + n_metals + n_non_metals + n_metalloids + alkali_list + alkaline_earth_list + icosagens_list + crystal_list  + pnicto_list + chalco_list + halo_list + noble_list + n_alkali_list + n_alkaline_earth_list + n_icosagens_list + n_crystal_list + n_pnicto_list + n_chalco_list + n_halo_list + n_noble_list + pos_charges + neg_charges + at_charges
        if self.current.value == "assuming":
            self.move()
        if self.current.value == "unless":
            self.move()
        if self.current.token == "LEFTROUNDBRACKET":
            boolean_operators = ["==", "&&", "||", ">=", ">", "<", "<="]
            self.move()
            self.next_token(True)
            while self.current.token != "RIGHTROUNDBRACKET":
                if self.next.value in boolean_operators:
                    print("is boolean")
                    acceptables = ["IDENTIFIER", "BOOLEAN", "STRING", "DIGIT"]
                    self.move()
                    self.next_token(True)
                    self.prev_token(True)

                    if (self.prev.token in acceptables or self.prev.value in unique_values) and (self.next.token in acceptables or self.prev.value in unique_values):
                        self.move()
                        self.move()
                elif self.next.token in ["BOOLEANLITERALS", "IDENTIFIER"]:
                    self.move()
                else:
                    self.errors.append(SyntaxError("Invalid syntax for control flow statement", self.current.line, self.current.value))
                    self.move()
                    break
            if self.current.token == "RIGHTROUNDBRACKET":
                self.move()
        if self.current.value == "than":
            self.move()
            if self.current.token == "LEFTCURLYBRACE":
                self.move()
                return True
            else:
                self.errors.append(SyntaxError("invalid for control flow statement", self.current.line, self.current.value))
                return False
            self.move()
        if self.current.token == "LEFTCURLYBRACE":
            self.move()
            return True
        else:
            self.errors.append(SyntaxError("Invalid for control flow statement", self.current.line, self.current.value))
            return False

    def parse_looping(self):
        if self.current.value == "iter":
            self.move()
            # while self.current.token == "IDENTIFIER" or self.current.value == ",":
        if self.current.token == "IDENTIFIER":
            self.move()
        if self.current.value == "in":
            self.move()
        if self.current.token == "IDENTIFIER":
            self.move()
        if self.current.token == "LEFTCURLYBRACE":
            self.move()
            return True
        else:
            self.errors.append(SyntaxError("Invalid for looping statement", self.current.l, self.current.valueine))
            return False

    def parse_comment(self):
        print("in parse comment")
        if self.current.token == "SINGLELINECOMMENT":
            self.move()
            if self.current.token == "COMMENTLITERAL":
                self.move()
        elif self.current.token == "MULTILINECOMMENT":
            self.move()
            if self.current.token == "COMMENTLITERAL":
                self.move()
                print("comment literal")
            if self.current.token == "MULTILINECOMMENT":
                self.move()
            else:
                self.errors.append(SyntaxError("Unclosed comment", self.current.line, self.current.value))
                self.move()

    def parse_called_function(self):
        if self.current.value in ["boyle", "charles", "gay_lussac", "avogadro", "ideal_gas", "combined_gas"]:
            self.move()
        if self.current.token == "LEFTROUNDBRACKET":
            self.move()
            if self.current.token in ["DIGIT", "IDENTIFIER"]:
                self.move()
                if self.current.value == ",":
                    self.move()
                if self.current.token in ["DIGIT", "IDENTIFIER"]:
                    self.move()
                if self.current.value == ",":
                    self.move()
                if self.current.token in ["DIGIT", "IDENTIFIER"]:
                    self.move()
                if self.current.value == ",":
                    self.move()
                if self.current.token in ["DIGIT", "IDENTIFIER"]:
                    self.move()
                else:
                    self.errors.append(SyntaxError("Unexpected for built in function", self.curren, self.current.valuet.line))
            
            
        
        if self.current.token in ["KEYWORD", "IDENTIFIER"]:
            self.move()
        
        if self.current.token == "LEFTROUNDBRACKET":
            self.move()
            while self.current.token != "RIGHTROUNDBRACKET":
                if self.current.token in ["IDENTIFIER", "DIGIT", "QUOTATIONMARK"]:
                    self.move()
                    if self.current.value == ",":
                        self.move()
                    elif isinstance(self.current, Operator):
                        self.parse_operator()
                        print("add in parameter")
                    elif self.current.token == "STRING" and self.next_token().token == "QUOTATIONMARK":
                        self.move()
                        self.move()
                    elif self.current.token == "RIGHTROUNDBRACKET":
                        self.move()
                        break
                    else:
                        self.move()
                        self.errors.append(SyntaxError("Invalid for parameter", self.current.line, self.current.value))
                else:
                    print(self.current)
                    self.errors.append(SyntaxError("Invalid for parameter", self.current.line, self.current.value))
                    self.move()
                    break

    def parse_balancing(self):
        valid_value = metals + non_metals + metalloids

        if self.current.token in ["BACKSLASH", "QUESTIONMARK"]:
            self.move()

        if self.current.value in valid_value or self.current.token in ["IDENTIFIER", "EXPONENT", "DIGIT"]:

            while self.current.value in valid_value or self.current.token in ["IDENTIFIER", "EXPONENT", "DIGIT"] and self.current.token != "BALANCINGARROW":

                if self.current.value in valid_value or self.current.token == "IDENTIFIER":
                    self.move()

                    if self.current.token == "EXPONENT":

                        self.move()

                        if self.current.token in ["DIGIT", "IDENTIFIER"]:
                            self.move()

                    if self.current.token == "ADD":
                        if self.next_token().token == "BALANCINGARROW":
                            self.errors.append(SyntaxError("Missing value for balancing operation", self.c, self.current.valueurrent.line))
                        self.move()

        if self.current.token == "BALANCINGARROW":
            self.move()
            while self.current.value in valid_value or self.current.token in ["IDENTIFIER", "EXPONENT", "DIGIT"] and self.current.token != "BACKSLASH":
                if self.current.value in valid_value or self.current.token == "IDENTIFIER":
                    self.move()
                    if self.current.token == "EXPONENT":
                        self.move()
                        if self.current.token in ["DIGIT", "IDENTIFIER"]:
                            self.move()
                    if self.current.token == "ADD":
                        if self.next_token().token == "BALANCINGARROW":
                            self.errors.append(SyntaxError("Missing value for balancing operation", self.c, self.current.valueurrent.line))
                        self.move()
            self.move()
            if self.current.value == ";":
                self.move()
            else:
                print(self.current)
                self.errors.append(SyntaxError("Missing semicolon", self.current.line, self.current.value))
