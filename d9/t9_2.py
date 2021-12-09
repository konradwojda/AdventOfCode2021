import fileinput


def get_neighbours(x: int, y: int, points: list) -> list:
    neighbours = [(x, y-1, points[y-1][x]), (x, y+1, points[y+1][x]),
                  (x-1, y, points[y][x-1]), (x+1, y, points[y][x+1])]
    return [(x1-1, y1-1, num) for x1, y1, num in neighbours if num is not None]


def get_risk_levels(points):
    lower_points = []
    for y, row in enumerate(points[1:-1]):
        for x, num in enumerate(row[1:-1]):
            if all(num < num1 for x1, y1, num1 in get_neighbours(x+1, y+1, points)):
                lower_points.append((x, y, num))
    return lower_points


def get_higher_neighbours(x, y, points):
    neighbours = get_neighbours(x+1, y+1, points)
    return [(x1, y1, num) for x1, y1, num in neighbours if num > points[y+1][x+1] and num != 9]


def get_basins_sizes(points):
    basins = []
    for x, y, num in get_risk_levels(points):
        basin = [(x, y, num)]
        basin_neighbours = get_higher_neighbours(x, y, points)
        basin.extend(basin_neighbours)
        while basin_neighbours:
            new_basin_neighbours = []
            for x1, y1, num1 in basin_neighbours:
                new_basin_neighbours.extend(
                    get_higher_neighbours(x1, y1, points))
            basin_neighbours = new_basin_neighbours
            basin.extend(basin_neighbours)
        basins.append(set(basin))
    return [len(basin) for basin in basins]


if __name__ == "__main__":
    input = [line.strip() for line in fileinput.input(files='./d9/input')]
    points = [[int(num) for num in line] for line in input]
    for line in points:
        line.append(None)
        line.insert(0, None)
    points.insert(0, [None]*len(points[0]))
    points.append([None]*len(points[0]))
    sizes = sorted(get_basins_sizes(points), reverse=True)
    print(sizes[0] * sizes[1] * sizes[2])
