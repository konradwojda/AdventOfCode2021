import fileinput

def increases_count(samples: list) -> int:
    i = 0
    for id, value in enumerate(samples[:-1]):
        if value < samples[id+1]:
            i += 1
    return i

def get_windows(samples: list) -> list:
    windows = [(value, samples[id+1], samples[id+2]) for id, value in enumerate(samples[:-2])]
    return [sum(window) for window in windows]

if __name__ == "__main__":
    result = increases_count(get_windows([int(line) for line in fileinput.input(files='./d1/input')]))
    print(result)