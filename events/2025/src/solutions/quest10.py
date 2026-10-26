import itertools
from io import TextIOWrapper
from lib.quest import app
from dataclasses import dataclass


@dataclass
class Vec:
    r: int
    c: int

    def __add__(self, other: 'Vec') -> 'Vec':
        return Vec(self.r + other.r, self.c + other.c)

    def __sub__(self, other: 'Vec') -> 'Vec':
        return Vec(self.r - other.r, self.c - other.c)


@app.parser(quest=10)
def parse(file: TextIOWrapper) -> str:
    return [[c for c in r.strip()] for r in file.readlines()]


@app.solver(quest=10, part=1)
def part1(board: list[list[str]]) -> str:
    def find_dragon():
        for i, r in enumerate(board):
            for j, c in enumerate(r):
                if c == 'D':
                    return Vec(i, j)

    hit = [[0 for _ in range(len(board[r]))] for r in range(len(board))]

    def move(r, c, s=0):
        if 0 <= r < len(board) and 0 <= c < len(board[r]):
            hit[r][c] = board[r][c] == 'S'
        if s == 4:
            return
        for R in [-1, 1, -2, 2]:
            for C in [-1, 1, -2, 2]:
                nums = set([abs(R), abs(C)])
                if not (1 in nums and 2 in nums):
                    continue
                move(r + R, c + C, s + 1)

    dragon = find_dragon()
    move(dragon.r, dragon.c)
    return sum([sum([c for c in r]) for r in hit])


@app.solver(quest=10, part=2)
def part2(board: list[list[str]]) -> str:
    game_board = [[c if c != '#' else '.' for c in r] for r in board]
    hit = [[0 for _ in range(len(board[r]))] for r in range(len(board))]

    STEPS = [
        (x, y)
        for x, y in itertools.permutations([-1, 1, -2, 2], r=2)
        if abs(x) != abs(y)
    ]

    T = 10

    def move_dragon(r, c, s=0, skips=0):
        if hit[r][c] > s:
            return
        if 0 <= r < len(board) and 0 <= c < len(board[r]):
            hit[r][c] = min(hit[r][c], s)
        if s == T:
            return

        for R, C in STEPS:
            move_dragon(r + R, c + C, s + 1)
        return

    def step_sheep(B: list):
        B.pop()
        return [['.' for _ in range(len(B[0]))]] + B

    def find_dragon():
        for i, r in enumerate(board):
            for j, c in enumerate(r):
                if c == 'D':
                    return Vec(i, j)

    dragon = find_dragon()
    print('moving dragon')
    skips = move_dragon(dragon.r, dragon.c)
    [[print('#' if c else '.', end='') for c in row] for row in hit if not print()]
    print('done dragon')
    eaten = 0
    for s in range(1, 21):
        for i, r in enumerate(hit):
            for j, c in enumerate(r):
                if c <= s and game_board[i][j] == s:
                    game_board[i][j] = '.'
                    eaten += 1
        game_board = step_sheep(game_board)
    return eaten, skips


@app.solver(quest=10, part=3)
def part3(a) -> str:
    return


def normalize(f: float) -> float:
    return round(f, 6)
