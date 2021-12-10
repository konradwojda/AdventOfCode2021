import fileinput
from os import error

OPENING_BRACES = ["[", "{", "<", "("]

CLOSING_BRACES = ["]", "}", ">", ")"]

CLOSING_DICT = {
    "[": "]",
    "(": ")",
    "<": ">",
    "{": "}"
}

REWARDING = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

def check_syntax_err(input):
    errors = []
    for id, line in enumerate(input):
        line_copy = ""
        for char in line:
            line_copy += char
            if char in CLOSING_BRACES:
                if char == CLOSING_DICT[line_copy[-2]]:
                    line_copy = line_copy[:-2]
                else:
                    errors.append(id)
                    break
    return errors



if __name__ == "__main__":
    input = [line.strip() for line in fileinput.input(files='./d10/test')]
    errors = check_syntax_err(input)
    print(errors)
    print(input)
