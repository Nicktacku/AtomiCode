from sys import argv
from lexer import Lexer


class AtomiCode:
    def __init__(self):
        self.had_error = False

    def run_file(self, path):
        f = open(path, "r")
        lexer = Lexer(f.read())
        print(lexer.to_token())

    def run_prompt(self):
        quit = False
        while not quit:
            prompt = input("> ")
            if prompt == "quit()": break
            lexer = Lexer(prompt)
            print(lexer.to_token())
            self.had_error = False

    def error(self, line, message):
        self.report(line, "", message)

    def report(self, line, where, message):
        print(f"[line {line}] Error {where}: {message}")
        self.had_error = True

atc = AtomiCode()

if len(argv) - 1 > 1:
    print("Usage: atomicode [script]")
elif len(argv) - 1 == 1:
    PATH = argv[1]
    atc.run_file(PATH)
else:
    atc.run_prompt()



