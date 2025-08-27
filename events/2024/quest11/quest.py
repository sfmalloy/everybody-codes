from io import TextIOWrapper
from . import p1, p2, p3


def parse(file: TextIOWrapper):
    rules = {}
    for line in file.readlines():
        key, vals = line.split(':')
        vals = vals.strip().split(',')
        rules[key] = vals
    return rules


def solve(part: int, file: TextIOWrapper):
    match part:
        case 1: return p1.solve(parse(file))
        case 2: return p2.solve(parse(file))
        case 3: return p3.solve(parse(file))
