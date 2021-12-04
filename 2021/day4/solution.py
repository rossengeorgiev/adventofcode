
import re

class BingoNumber(object):
    all_numbers = dict()

    def using(number):
       BingoNumber.all_numbers[number] = number = BingoNumber.all_numbers.get(number, BingoNumber(number))
       return number

    marked = False

    def __init__(self, number):
        self.number = number

    def __repr__(self):
        if self.marked:
            return f"[{self.number: >2}]"
        else:
            return f"{self.number: >3} "

    def __int__(self):
        return self. number

    def mark(self):
        self.marked = True

    def __bool__(self):
        return self.marked

class BingoBoard(object):
    def __init__(self):
        self.numbers = []
        self.rows = [[], [], [], [], []]
        self.columns = [[], [], [], [], []]

    def __repr__(self):
        text = ("-" * 30) + "\n"
        for row in self.rows:
            text += repr(row) + "\n"
        text += ("-" * 30)
        return text

    def set_number(self, row, column, number):
        number = BingoNumber.using(number)
        self.numbers.append(number)
        self.rows[row].append(number)
        self.columns[column].append(number)

    def got_bingo(self):
        for row in self.rows:
            if all(row):
                return True
        for column in self.columns:
            if all(column):
                return True
        return False

    def get_sum_unmarked(self):
        return sum(map(int, filter(lambda n: not n.marked, self.numbers)))


def load_bingo(fp):
    draw = list(map(int, fp.readline().strip().split(',')))

    boards = []
    board = None
    row = 0

    for line in fp:
        line = line.strip()

        # empty line before every board
        if not line:
            board = BingoBoard()
            boards.append(board)
            row = 0
            continue

        # load row of numbers
        for column, number in enumerate(map(int, re.split(' +', line))):
            board.set_number(row, column, number)

        row += 1

    return draw, boards

def play_bingo(draw, boards):
    part1 = None

    boards_in_play = set(range(len(boards)))

    for i, number in enumerate(draw):
        BingoNumber.using(number).mark()

        for ii, board in enumerate(boards):
            if board.got_bingo():
                if len(boards_in_play) == 1 and ii in boards_in_play:
                    part2 = number * board.get_sum_unmarked()
                    return part1, (board, part2)

                boards_in_play -= {ii}

                if not part1:
                    part1 = board, number * board.get_sum_unmarked()


    return part1, part2


fp = open('input.txt')
draw, boards = load_bingo(fp)

(first_board, part1), (last_board, part2) = play_bingo(draw, boards)

print(first_board)
print("Part1:", part1)
print(last_board)
print("Part2:", part2)


