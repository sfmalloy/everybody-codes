from io import TextIOWrapper
from lib.quest import app


@app.parser(quest=4)
def parse(file: TextIOWrapper):
    return list(map(int, file.readlines()))


@app.solver(quest=4, part=1)
def part1(nails: list[int]):
    return total_strikes(nails)


@app.solver(quest=4, part=2)
def part2(nails: list[int]):
    return total_strikes(nails)


def total_strikes(nails: list[int]):
    shortest = min(nails)
    return sum(abs(nail - shortest) for nail in nails)


@app.solver(quest=4, part=3)
def part3(nails: list[int]):
    best = (0, float('inf'))
    for src in nails:
        d = 0
        for dst in nails:
            d += abs(src - dst)
        if d < best[1]:
            best = (src, d)
    return best[1]
