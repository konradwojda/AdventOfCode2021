import fileinput

BOARD_SIZE = 10

def get_neighbours(x, y):
    return [(x2, y2) for x2 in range(x-1, x+2) for y2 in range(y-1, y+2) if -1 < x <= BOARD_SIZE-1 and -1 <
            y <= BOARD_SIZE-1 and (x != x2 or y != y2) and (0 <= x2 <= BOARD_SIZE-1) and (0 <= y2 <= BOARD_SIZE-1)]

def get_flash_points(points, flashed):
    points_to_flash = []
    for y, row in enumerate(points):
        for x, num in enumerate(row):
            if num > 9 and (x, y) not in flashed:
                points_to_flash.append((x,y))
    return points_to_flash

def simulate(points, steps):
    flashes_num = 0
    for _ in range(steps):
        flashed = []
        points = [[point+1 for point in line] for line in points]
        points_to_flash = get_flash_points(points, flashed)
        while points_to_flash:
            for x, y in points_to_flash:
                flashed.append((x, y))
                neighbours = get_neighbours(x, y)
                for xn, yn in neighbours:
                    points[yn][xn] += 1
            points_to_flash = get_flash_points(points, flashed)
        for xf, yf in flashed:
            points[yf][xf] = 0
        flashes_num += len(flashed)
    return flashes_num



if __name__ == "__main__":
    input = [line.strip() for line in fileinput.input(files='./d11/input')]
    points = [[int(num) for num in line] for line in input]
    print(simulate(points, 100))
