import fileinput
from typing import Counter

def check_all_digits(input):
    output = []
    for line in input:
        digits = line[0].split()

        # get obvious ones first
        one = [num for num in digits if len(num) == 2][0]
        four = [num for num in digits if len(num) == 4][0]
        seven = [num for num in digits if len(num) == 3][0]
        eight = [num for num in digits if len(num) == 7][0]

        all_digits = "".join(digits)
        count = Counter(all_digits)

        # only b appears 6 times in all 10 numbers
        b = [key for key, value in count.items() if value == 6][0]

        # only f appears 9 times in all 10 numbers
        f = [key for key, value in count.items() if value == 9][0]

        # only e appears 4 times in all 10 numbers
        e = [key for key, value in count.items() if value == 4][0]

        # a is the only difference between one and seven so it will be the least common
        a = Counter("".join([one, seven])).most_common()[-1][0]

        # d is the only difference between one (plus b) and four
        d = Counter("".join([four, one+b])).most_common()[-1][0]

        #c and f appears in one, but i already have f
        c = [n for n in one if n != f][0]

        #g appears in eight and i have all other digits
        g = [n for n in eight if n not in [a, b, c, d, e, f]][0]

        code = {
            "".join(sorted(a+b+c+e+f+g)): '0',
            "".join(sorted(c+f)): '1',
            "".join(sorted(a+c+d+e+g)): '2',
            "".join(sorted(a+c+d+f+g)): '3',
            "".join(sorted(b+c+d+f)): '4',
            "".join(sorted(a+b+d+f+g)): '5',
            "".join(sorted(a+b+d+e+f+g)): '6',
            "".join(sorted(a+c+f)): '7',
            "".join(sorted(a+b+c+d+e+f+g)): '8',
            "".join(sorted(a+b+c+d+f+g)): '9'
        }
        final_number = ""
        for number in line[1].split(" "):
            final_number += code["".join(sorted(number))]
        output.append(int(final_number))
    return sum(output)


if __name__ == "__main__":
    input = [line.strip().split(" | ") for line in fileinput.input(files='./d8/input')]
    print(check_all_digits(input))