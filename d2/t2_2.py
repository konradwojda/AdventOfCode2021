import fileinput


def get_pos(samples):
    depth = 0
    hor = 0
    aim = 0
    for sample in samples:
        if sample[0] == 'forward':
            hor += int(sample[1])
            depth += aim * int(sample[1])
        elif sample[0] == 'up':
            aim -= int(sample[1])
        elif sample[0] == 'down':
            aim += int(sample[1])
    return hor * depth

if __name__ == "__main__":
    result = get_pos([line.split() for line in fileinput.input(files='./d2/input')])
    print(result)