from io import TextIOWrapper

from . import p1
from . import p2
from . import p3


def parse(file: TextIOWrapper):
    tree = {}
    for line in file.readlines():
        k, v = line.strip().split(':')
        tree[k] = v.split(',')
    return tree


def solve(part: int, file: TextIOWrapper):
    match part:
        case 1: return p1.solve(parse(file))
        case 2: return p2.solve(parse(file))
        case 3: return p3.solve(parse(file))
