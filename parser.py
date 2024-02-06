from Tokens import *
from Errors import *

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
        
        assignment_operators = ["=", "+=", "-=", "*=", "/=", "%="]
        
        while self.index < len(self.tokens):
            
            # *digits
            # if self.current.token == "DIGIT" and isinstance(self.next_token(), Operator):
            #     self.move()
            #     self.move()

            #     print("CURRENT TOKEN: ",self.current.token)

            #     if self.current.token in ["DIGIT", "IDENTIFIER"]:
            #         self.move()

            #     else:
            #         self.errors.append(SyntaxError("invalid for operation", self.current.line))
            #         self.move()

            if isinstance(self.current, Operator) and not self.current.value in assignment_operators:
                self.parse_operator()
            elif self.current.value in assignment_operators:
                self.parse_assignment()
            elif self.current.token == "QUOTATIONMARK":
                self.parse_string()
            elif self.current.value == "def":
                self.parse_function()
            else:
                self.move()
                




            
            if isinstance(self.current, Eof):
                break
        print(self.errors)

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
        
        if self.prev.token in ["IDENTIFIER", "DIGIT"] and self.next.token in ["IDENTIFIER", "DIGIT"]:
            self.move()
            return True
        else:
            self.errors.append(SyntaxError("invalid for operation", self.current.line))
            self.move()
            return False
    
    def parse_assignment(self):
        is_string = False
        self.prev_token(True)
        self.next_token(True)

        print(self.next.token)
        if self.next.token == "QUOTATIONMARK":
            self.move()
            is_string = self.parse_string()
        
        if self.prev.token == "IDENTIFIER" and (self.next.token in ["IDENTIFIER", "DIGIT"] or is_string):
            self.move()
            return True
        else:
            self.errors.append(SyntaxError("invalid for operation (assignment)", self.current.line))
            self.move()
            return False

    def parse_string(self):
        if self.current.token == "QUOTATIONMARK":
            self.move()
        if self.current.token == "STRING":
            self.move()
        if self.current.token == "QUOTATIONMARK":
            self.move()
            return True
        else:
            self.errors.append(SyntaxError("Invalid string", self.current.line))
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
                        break
                    else:
                        self.move()
                        self.errors.append(SyntaxError("Invalid for parameter", self.current.line))
                else:
                    self.errors.append(SyntaxError("Invalid for parameter", self.current.line))
        if self.current.token == "LEFTCURLYBRACE":
            self.move()
            return True
        else:
            print("else", self.current)
            self.errors.append(SyntaxError("Invalid for function declaration", self.current.line))
            return False