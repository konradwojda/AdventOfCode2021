import fileinput


class Field:
    def __init__(self, number) -> None:
        self.number = number
        self.marked = False


class Board:
    def __init__(self, fields) -> None:
        self.fields: list[list[Field]] = fields

    def check_win(self):
        for row in self.fields:
            if all(field.marked for field in row):
                return True
        for id in range(5):
            column = [row[id] for row in self.fields]
            if all(field.marked for field in column):
                return True
        return False

    def check_score(self, number):
        unmarked_score = 0
        for row in self.fields:
            for field in row:
                if not field.marked:
                    unmarked_score += field.number
        return unmarked_score * number

    def mark(self, number):
        for row in self.fields:
            for field in row:
                if field.number == number:
                    field.marked = True


def create_board(lines):
    fields = []
    for line in lines:
        fields.append([Field(int(number)) for number in line])
    return Board(fields)


def solve_problem(numbers, boards):
    for number in numbers:
        for board in boards:
            board.mark(number)
            if board.check_win():
                return board.check_score(number)

if __name__ == "__main__":
    input = [line.split() for line in fileinput.input(files='./d4/input')]
    input = [i for i in input if i != []]
    numbers = [int(i) for i in input[0][0].split(",")]
    idx = 0
    lines = []
    boards = []
    for elem in input[1:]:
        lines.append(elem)
        idx += 1
        if(idx == 5):
            boards.append(create_board(lines))
            lines = []
            idx = 0
    print(solve_problem(numbers, boards))

