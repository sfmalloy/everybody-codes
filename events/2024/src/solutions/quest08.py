from io import TextIOWrapper
from lib.quest import app


@app.parser(quest=8)
def parse(file: TextIOWrapper):
    return int(file.read().strip())


@app.solver(quest=8, part=1)
def part1(blocks: int):
    l = 1
    T = 0
    while T < blocks:
        T += l
        l += 2
    l -= 2
    return (T - blocks) * l


@app.solver(quest=8, part=2)
def part2(nullpointers: int):
    acolytes = 1111
    blocks = 20240000

    h = 1
    w = 1
    T = 0
    while T < blocks:
        T += h * w
        h = (h * nullpointers) % acolytes
        w += 2
    w -= 2
    return (T - blocks) * w


@app.solver(quest=8, part=3)
def part3(nullpointers: int):
    acolytes = 10
    blocks = 202400000
    thickness = 1
    width = 1
    columns = []
    area = 0
    while area < blocks:
        columns.append(0)
        for c in range(len(columns)):
            columns[c] += thickness
        area += thickness * width
        thickness = ((thickness * nullpointers) % acolytes) + acolytes
        width += 2
    width -= 2
    columns.pop()
    columns += columns[1:]
    for c in columns:
        area -= (nullpointers * width * c) % acolytes
    return area - blocks
