import fileinput


def get_occurance(samples):
    occurances = [0] * len(samples[0][0])
    gamma_rate = ''
    epsilon_rate = ''
    for sample in samples:
        for id, number in enumerate(sample[0]):
            if int(number) == 1:
                occurances[id] += 1
    for occur in occurances:
        if (occur > len(samples)-occur):
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'
    return int(gamma_rate, 2) * int(epsilon_rate, 2)




if __name__ == "__main__":
    result = get_occurance([line.split() for line in fileinput.input(files='./d3/input')])
    print(result)