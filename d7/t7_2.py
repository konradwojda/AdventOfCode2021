import fileinput

def fuel_needed(positions, target):
    return sum([sum(range(abs(position - target) + 1)) for position in positions])


def find_best_pos(positions):
    return min([fuel_needed(positions, tar) for tar in range(min(positions), max(positions) + 1)])


if __name__ == "__main__":
    input = [line.split(",") for line in fileinput.input(files='./d7/input')][0]
    input = [int(num) for num in input]
    print(find_best_pos(input))