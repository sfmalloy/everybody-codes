from io import TextIOWrapper
from . import p1, p2, p3
from .vec import Vec


def parse(file: TextIOWrapper):
    stars = []
    for r, row in enumerate(file.readlines()):
        for c, col in enumerate(row.strip()):
            if col == '*':
                stars.append(Vec(r, c))
    return stars


def solve(part: int, file: TextIOWrapper):
    match part:
        case 1: return p1.solve(parse(file))
        case 2: return p2.solve(parse(file))
        case 3: return p3.solve(parse(file))
