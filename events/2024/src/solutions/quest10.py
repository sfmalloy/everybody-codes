from io import TextIOWrapper
from lib.quest import app


@app.parser(quest=10)
def parse(file: TextIOWrapper):
    return [[c for c in r.strip()] for r in file.readlines()]


@app.solver(quest=10, part=1)
def solve(grid: list[list[str]]):
    ans = ''
    for r in range(2, 6):
        row = set(filter(lambda char: char not in '.*', grid[r]))
        for c in range(2, 6):
            col = set(
                filter(
                    lambda char: char not in '.*',
                    [grid[rr][c] for rr in range(len(grid))],
                )
            )
            same = list(row & col)[0]
            grid[r][c] = same
            ans += same
    return ans


@app.solver(quest=10, part=2)
def part2(grid: list[list[str]]):
    ans = 0
    for r in range(7):
        for c in range(15):
            section = extract(grid, r, c)
            ans += solve_section(section)
    return ans


@app.solver(quest=10, part=3)
def part3(i):
    return 'not solved'


def extract(grid: list[list[str]], R: int, C: int):
    section = []
    for r in range(9 * R, 9 * R + 8):
        row = []
        for c in range(9 * C, 9 * C + 8):
            row.append(grid[r][c])
        section.append(row)
    return section


def solve_section(grid: list[list[str]]):
    ans = ''
    for r in range(2, 6):
        row = set(filter(lambda char: char not in '.*', grid[r]))
        for c in range(2, 6):
            col = set(
                filter(
                    lambda char: char not in '.*',
                    [grid[rr][c] for rr in range(len(grid))],
                )
            )
            same = list(row & col)[0]
            grid[r][c] = same
            ans += same
    return sum((ord(c) - ord('A') + 1) * i for i, c in enumerate(ans, start=1))
