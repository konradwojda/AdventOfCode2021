import fileinput

def simulation(population: list, days: int):
    for day in range(days):
        new_population = []
        for member in population:
            member -= 1
            if member == -1:
                new_population.append(6)
                new_population.append(8)
            else:
                new_population.append(member)
        population = new_population
    return len(population)



if __name__ == "__main__":
    input = [line.split(",") for line in fileinput.input(files='./d6/test')][0]
    input = [int(num) for num in input]
    # print(input)
    print(simulation(input, 256))