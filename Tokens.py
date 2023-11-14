class Token:
    def __init__(self, value, token):
        self.value = value
        self.token = token

class Digit(Token):
    def __init__(self, value):
        super().__init__(value, "DIGIT")
    
    def __repr__(self):
        return self.token

class Float(Token):
    def __init__(self, value):
        super().__init__(value, "Float")
    
    def __repr__(self):
        return self.token

class Operator(Token):
    def __init__(self, value):
        super().__init__(value, "Operator")
    
    def __repr__(self):
        return self.token

class Invalid(Token):
    def __init__(self, value):
        super().__init__(value, "Invalid")
    
    def __repr__(self):
        return self.token
