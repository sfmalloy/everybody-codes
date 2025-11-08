from io import TextIOWrapper
from itertools import batched

from lib.quest import app


@app.parser(quest=1)
def parse(file: TextIOWrapper):
    return file.read().strip()


@app.solver(quest=1, part=1)
def part1(ipt: str):
    vals = {'A': 0, 'B': 1, 'C': 3}
    total = 0
    for bug in ipt:
        total += vals[bug]
    return total


@app.solver(quest=1, part=2)
def part2(ipt: str):
    vals = {'x': 0, 'A': 0, 'B': 1, 'C': 3, 'D': 5}
    total = 0
    for a, b in batched(ipt, 2):
        if a == 'x' or b == 'x':
            total += vals[a] + vals[b]
        else:
            total += vals[a] + vals[b] + 2
    return total


@app.solver(quest=1, part=3)
def part3(ipt: str):
    vals = {'x': 0, 'A': 0, 'B': 1, 'C': 3, 'D': 5}
    total = 0
    for tri in batched(ipt, 3):
        x_count = tri.count('x')
        if x_count == 0:
            total += sum(vals[x] for x in tri) + 6
        elif x_count == 1:
            total += sum(vals[x] for x in tri) + 2
        else:
            total += sum(vals[x] for x in tri)
    return total
