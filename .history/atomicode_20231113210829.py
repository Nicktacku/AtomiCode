from sys import argv


class AtomiCode:
    def __init__(self):
        self.had_error = False

    def run_file(self, path):
        # if self.had_error:
        #     break
        print(path)

    def run_prompt(self):
        while True:
            prompt = input("> ")
            print(eval(prompt))
            self.had_error = False

    def error(self, line, message):
        self.report(line, "", message)

    def report(self, line, where, message):
        print(f"[line {line}] Error {where}: {message}")
        self.had_error = True

atc = AtomiCode()

print(len(argv))

if len(argv) - 1 > 1:
    print("Usage: jlox [script]")
elif len(argv) - 1 == 1:
    PATH = argv[1]
    atc.run_file(PATH)
else:
    atc.run_prompt()



