from io import TextIOWrapper
from . import p1, p2, p3
from .model import Vec


def parse(file: TextIOWrapper):
    lines = []
    for line in file.readlines():
        dirs = []
        for d in line.strip().split(','):
            dir = d[0]
            dist = int(d[1:])
            match dir:
                case 'R': dirs.append(Vec(dist, 0))
                case 'L': dirs.append(Vec(-dist, 0))
                case 'U': dirs.append(Vec(0, dist))
                case 'D': dirs.append(Vec(0, -dist))
        lines.append(dirs)
    return lines


def solve(part: int, file: TextIOWrapper):
    match part:
        case 1: return p1.solve(parse(file))
        case 2: return p2.solve(parse(file))
        case 3: return p3.solve(parse(file))
