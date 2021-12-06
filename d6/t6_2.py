import fileinput

def simulation(population: list, days: int):
    current_size = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for member in population:
        current_size[member] += 1
    for day in range(days):
        new_population = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for days_remaining, size in enumerate(current_size):
            if days_remaining == 0:
                new_population[6] += size
                new_population[8] += size
            else:
                new_population[days_remaining - 1] += size
        current_size = new_population
    return sum(current_size)



if __name__ == "__main__":
    input = [line.split(",") for line in fileinput.input(files='./d6/input')][0]
    input = [int(num) for num in input]
    # print(input)
    print(simulation(input, 256))