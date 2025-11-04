from io import TextIOWrapper
from ..lib.quest import app


@app.parser(quest=1)
def parse(file: TextIOWrapper):
    lines = [line.strip() for line in file.readlines()]
    return lines[0].split(','), [
        (-1 if step.startswith('L') else 1) * int(step[1:])
        for step in lines[2].split(',')
    ]


@app.solver(quest=1, part=1)
def part1(names: list[str], dirs: list[int]) -> int:
    i = 0
    for d in dirs:
        i = max(0, min(i + d, len(names) - 1))
    return names[i]


@app.solver(quest=1, part=2)
def part2(names: list[str], dirs: list[int]) -> int:
    return names[sum(dirs) % len(names)]


@app.solver(quest=1, part=3)
def part3(names: list[str], dirs: list[int]) -> int:
    for d in dirs:
        i = d % len(names)
        names[0], names[i] = names[i], names[0]
    return names[0]
