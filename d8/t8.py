import fileinput

def check_easy_digits(input):
    digits = [elem[1].split() for elem in input]
    counter = 0
    for elem in digits:
        for digit in elem:
            if len(digit) == 2 or len(digit) == 4 or len(digit) == 3 or len(digit) == 7:
                counter += 1
    return counter


if __name__ == "__main__":
    input = [line.strip().split(" | ") for line in fileinput.input(files='./d8/input')]
    print(check_easy_digits(input))