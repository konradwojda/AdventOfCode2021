import fileinput
from collections import Counter


def get_tuple_list(input):
    points = []
    for elem in input:
        f_point = int(elem[0].split(",")[0]), int(elem[0].split(",")[1])
        s_point = int(elem[2].split(",")[0]), int(elem[2].split(",")[1])
        points.append([f_point, s_point])
    return points


def filter_lines(points):
    filtered = []
    for elem in points:
        if (elem[0][0] == elem[1][0] or elem[0][1] == elem[1][1]):
            filtered.append(elem)
        elif (elem[0][1] - elem[1][1]) / (elem[0][0] - elem[1][0]) == 1 or (elem[0][1] - elem[1][1]) / (elem[0][0] - elem[1][0]) == -1:
            filtered.append(elem)
    return filtered


def get_line_points(points):
    if points[0][0] == points[1][0]:
        start = points[0][1] if points[0][1] < points[1][1] else points[1][1]
        end = points[0][1] if points[0][1] > points[1][1] else points[1][1]
        coverage = [(points[0][0], y) for y in range(start, end + 1)]
    elif points[0][1] == points[1][1]:
        start = points[0][0] if points[0][0] < points[1][0] else points[1][0]
        end = points[0][0] if points[0][0] > points[1][0] else points[1][0]
        coverage = [(x, points[0][1]) for x in range(start, end + 1)]
    elif(points[0][1] - points[1][1]) / (points[0][0] - points[1][0]) == 1 or (points[0][1] - points[1][1]) / (points[0][0] - points[1][0]) == -1:
        a = int((points[0][1] - points[1][1]) / (points[0][0] - points[1][0]))
        x_start = points[0][0] if points[0][0] < points[1][0] else points[1][0]
        x_end = points[0][0] if points[0][0] > points[1][0] else points[1][0]
        y_start = points[0][1] if points[0][1] < points[1][1] else points[1][1]
        y_end = points[0][1] if points[0][1] > points[1][1] else points[1][1]
        if a < 0:
            y_start, y_end = y_end, y_start
        x_list = [x for x in range(x_start, x_end + 1)]
        y_list = [y for y in range(y_start, y_end + a, a)]
        coverage = list(zip(x_list, y_list))
    return coverage


def count_points(counter):
    overlaps = 0
    for count in counter.values():
        if count >= 2:
            overlaps += 1
    return overlaps


if __name__ == "__main__":
    input = [line.split() for line in fileinput.input(files='./d5/input')]

    lines = filter_lines(get_tuple_list(input))
    all_points = []
    for points in lines:
        all_points.extend(get_line_points(points))
    print(count_points(Counter(all_points)))
