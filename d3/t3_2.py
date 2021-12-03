import fileinput


def get_numbers(samples, bit, rating):
    occurances = 0
    considering_zero = []
    considering_one = []
    for sample in samples:
        if int(sample[0][bit]) == 1:
            occurances += 1
            considering_one.append(sample)
        else:
            considering_zero.append(sample)
    if (rating):
        if(occurances >= len(samples) - occurances):
            return considering_one
        else:
            return considering_zero
    else:
        if(occurances < len(samples) - occurances):
            return considering_one
        else:
            return considering_zero


def get_ratings(samples):
    oxygen_rate = samples.copy()
    co2rate = samples.copy()
    bit = 0
    while(len(oxygen_rate) > 1):
        oxygen_rate = get_numbers(oxygen_rate, bit, True)
        bit += 1
    bit = 0
    while(len(co2rate) > 1):
        co2rate = get_numbers(co2rate, bit, False)
        bit += 1
    return int(oxygen_rate[0][0], 2) * int(co2rate[0][0], 2)



if __name__ == "__main__":
    result = get_ratings([line.split() for line in fileinput.input(files='./d3/input')])
    print(result)