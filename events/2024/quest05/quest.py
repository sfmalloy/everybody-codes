from io import TextIOWrapper
from collections import deque

from . import p1, p2, p3


def parse(file: TextIOWrapper):
    grid: list[deque[int]] = []
    for line in file.readlines():
        row = list(map(int, line.strip().split()))
        for c, col in enumerate(row):
            if len(grid) < c+1:
                grid.append(deque())
            grid[c].append(col)
    return grid


def solve(part: int, file: TextIOWrapper):
    match part:
        case 1: return p1.solve(parse(file))
        case 2: return p2.solve(parse(file))
        case 3: return p3.solve(parse(file))
