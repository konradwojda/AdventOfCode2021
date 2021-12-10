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
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

def check_syntax_err(input):
    errors = []
    for line in input:
        line_copy = ""
        for char in line:
            line_copy += char
            if char in CLOSING_BRACES:
                if char == CLOSING_DICT[line_copy[-2]]:
                    line_copy = line_copy[:-2]
                else:
                    errors.append(char)
                    break
    return errors



if __name__ == "__main__":
    input = [line.strip() for line in fileinput.input(files='./d10/input')]
    errors = check_syntax_err(input)
    print(sum(REWARDING[err] for err in errors))