from sys import argv
from lexer import Lexer
from parser import Parser


class AtomiCode:
    def __init__(self):
        self.had_error = False

    def run_file(self, path):
        f = open(path, "r")
        lexer = Lexer(f.read())
        print(lexer.to_token())
        return lexer.to_token()

    def run_prompt(self):
        quit = False
        while not quit:
            prompt = input("> ")
            if prompt == "quit()": break
            lexer = Lexer(prompt)
            print(lexer.to_token())
            
            self.had_error = False
            return lexer.to_token()

    # def error(self, line, message):
    #     self.report(line, "", message)

    # def report(self, line, where, message):
    #     print(f"[line {line}] Error {where}: {message}")
    #     self.had_error = True

atc = AtomiCode()

print(len(argv))

if len(argv) - 1 > 1:
    print("Usage: atomicode [script]")
elif len(argv) == 2 and argv[1].endswith("atc"):
    PATH = argv[1]
    lexemes = atc.run_file(PATH)
elif len(argv) == 1:
    lexemes = atc.run_prompt()
elif not argv[1].endswith("atc"):
    print("wrong extention")

# tokens = []
# lexemes = []
parser = Parser(lexemes)

parser.parse()

new_lexemes = [str(i) for i in lexemes]
f = open("symbol_table.txt", "w")
f.write("-"*40 + "\n")
f.write("|" + "\t" + "Tokens" + "\t"*5 + "Lexemes" + " "*4 + "|" + "\n")
f.write("-"*40 + "\n")

for line in new_lexemes:
    f.write("\t" + line + "\n")

f.close()



