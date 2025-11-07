from io import TextIOWrapper
from lib.quest import app


@app.parser(quest=4)
def parse(file: TextIOWrapper, part: int):
    if part != 3:
        return list(map(int, file.readlines()))
    pairs = [list(map(int, line.strip().split('|'))) for line in file.readlines()]
    return pairs


@app.solver(quest=4, part=1)
def part1(gears: list[int]) -> int:
    return int(2025 * gears[0] / gears[-1])


@app.solver(quest=4, part=2)
def part2(a):
    # not a clue if this is really the correct way of doing things but it kinda works
    if a[0] % a[-1] != 0:
        delta = a[-1] // (a[0] % a[-1])
    else:
        delta = 0
    return int(10000000000000 * a[-1] / a[0]) + delta


@app.solver(quest=4, part=3)
def part3(a):
    turns = 100
    for i in range(len(a) - 1):
        src = max(a[i])
        ratio = src / min(a[i + 1])
        turns *= ratio
    return int(turns)
