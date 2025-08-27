from io import TextIOWrapper
from . import p1, p2, p3
from .vec import Tower


def parse(file: TextIOWrapper):
    lines = file.readlines()[1:-1]
    lines.reverse()
    a = Tower(lines[0].index('A'), 0)
    b = Tower(lines[1].index('B'), 1)
    c = Tower(lines[2].index('C'), 2)
    targets = set()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == 'T' or char == 'H':
                targets.add(Tower(x, y, 1 if char == 'T' else 2))
    return a, b, c, targets


def solve(part: int, file: TextIOWrapper):
    match part:
        case 1: return p1.solve(*parse(file))
        case 2: return p2.solve(*parse(file))
        case 3: return p3.solve(*parse(file))
