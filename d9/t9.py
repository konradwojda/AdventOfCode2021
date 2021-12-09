import fileinput


def get_neighbours(x: int, y: int, points: list) -> list:
    neighbours = [points[y-1][x], points[y+1]
                  [x], points[y][x-1], points[y][x+1]]
    return [elem for elem in neighbours if elem is not None]


def get_risk_levels(points):
    lower_points = []
    for y, row in enumerate(points[1:-1]):
        for x, num in enumerate(row[1:-1]):
            if all(num < x for x in get_neighbours(x+1, y+1, points)):
                lower_points.append(num)
    return sum(lower_points) + len(lower_points)


if __name__ == "__main__":
    input = [line.strip() for line in fileinput.input(files='./d9/input')]
    points = [[int(num) for num in line] for line in input]
    for line in points:
        line.append(None)
        line.insert(0, None)
    points.insert(0, [None]*len(points[0]))
    points.append([None]*len(points[0]))
    print(get_risk_levels(points))
