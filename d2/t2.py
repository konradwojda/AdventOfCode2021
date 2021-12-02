import fileinput


def get_pos(samples):
    depth = 0
    hor = 0
    for sample in samples:
        if sample[0] == 'forward':
            hor += int(sample[1])
        elif sample[0] == 'up':
            depth -= int(sample[1])
        elif sample[0] == 'down':
            depth += int(sample[1])
    return hor * depth

if __name__ == "__main__":
    result = get_pos([line.split() for line in fileinput.input(files='./d2/input')])
    print(result)