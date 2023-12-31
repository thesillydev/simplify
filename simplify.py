import re


class OpenFile:
    def __new__(cls, code):
        self = super().__new__(cls)
        self.code = code
        if self.code.endswith(".simp"):
            with open(self.code, "r") as f:
                fil = f.read()
            return fil
        else:
            return "Invalid File! The extension must ends with .simp!"


class Interpreter:
    def __new__(cls, code):
        self = super().__new__(cls)
        self.code = code
        tokens = {"\\": "\n", "|": " ", " ": "\t", "^": "**",
                  "&": "and", "@": "or", "#": "reversed", "~": "not",
                  "b": "break", "d": "def", "e": "else", "f": "for",
                  "i": "if", "p": "print", "s": "input", "t": "f", "w": "while",
                  "F": "False", "T": "True", "n": "in", "?": "range", "r": "return"}

        # Ignore all newlines, so it means you could break the code infintely
        # and still would only convert into a single line of actual code
        code = re.sub("\n", "", code)
        # remove comments, which all starts and ends with *, no matter how many lines they have
        code = re.sub(r'\*.*?\*', "", code, flags=re.DOTALL)
        # convert every token of code into actual python tokens
        strings = re.findall('".*?"', code, flags=re.DOTALL)
        code = "".join([tokens[char] if char in list(tokens.keys()) else char for char in ".".join(code).split(".")])
        strings1 = re.findall('".*?"', code, flags=re.DOTALL)
        for i in range(len(strings1)):
            code = code.replace(strings1[i], strings[i])
        code = code.replace("else if", "elif")

        # adds spaces in the values between = operator
        code = re.sub(r'(\w)([+=<>!]+)(\w)', r'\1 \2 \3', code)
        exec(code, locals())
