import fileinput

population_size = {
    0:0,
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
    7:0,
    8:0
}

def simulation(population: list, days: int):
    current_size = population_size.copy()
    for member in population:
        current_size[member] += 1
    for day in range(days):
        new_population = population_size.copy()
        for days_remaining, size in current_size.items():
            if days_remaining == 0:
                new_population[6] += size
                new_population[8] += size
            else:
                new_population[days_remaining - 1] += size
        current_size = new_population
    return sum(current_size.values())



if __name__ == "__main__":
    input = [line.split(",") for line in fileinput.input(files='./d6/input')][0]
    input = [int(num) for num in input]
    # print(input)
    print(simulation(input, 256))