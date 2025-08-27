from pathlib import Path
from io import TextIOWrapper

from . import p1
from . import p2
from . import p3


def parse(file: TextIOWrapper):
    ipt = file.readlines()
    segments = {}
    mp = {
        '+': 1,
        '-': -1,
        '=': 0
    }
    for line in ipt:
        key, vals = line.strip().split(':')
        vals = vals.split(',')
        segments[key] = [mp[v] for v in vals]
    return segments


def solve(part: int, file: TextIOWrapper):
    match part:
        case 1: return p1.solve(parse(file))
        case 2: return p2.solve(parse(file))
        case 3: return p3.solve(parse(file))
