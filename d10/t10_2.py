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
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}


def check_syntax_err(input):
    errors = []
    line_copies = []
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
        if id not in errors:
            line_copies.append(line_copy)
    return errors, line_copies


if __name__ == "__main__":
    input = [line.strip() for line in fileinput.input(files='./d10/input')]
    errors, line_copies = check_syntax_err(input)
    print(line_copies)
    scores = []
    line_copies = [line[::-1] for line in line_copies]
    for line in line_copies:
        score = 0
        for char in line:
            score *= 5
            score += REWARDING[char]
        scores.append(score)
    scores.sort()
    print(scores[int(len(scores)/2)])
