from io import TextIOWrapper
from . import p1, p2, p3
from .model import Vec


def parse(file: TextIOWrapper):
    start = Vec(0, 0)
    end = Vec(0, 0)
    grid = []
    symbols = {'S': 0, 'E': 0, '#': -1, ' ': -1}
    for r, row in enumerate(file.readlines()):
        grid_row = []
        for c, col in enumerate(row.strip()):
            if col in symbols:
                grid_row.append(symbols[col])
            else:
                grid_row.append(int(col))
            if col == 'S':
                start = Vec(r, c)
            elif col == 'E':
                end = Vec(r, c)
        grid.append(grid_row)
    return start, end, grid


def solve(part: int, file: TextIOWrapper):
    match part:
        case 1: return p1.solve(*parse(file))
        case 2: return p2.solve(*parse(file))
        case 3: return p3.solve(*parse(file))
