from io import TextIOWrapper
from lib.quest import app
from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class Vec:
    x: int
    y: int

    def __add__(self, other: 'Vec') -> 'Vec':
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vec') -> 'Vec':
        return Vec(self.x - other.x, self.y - other.y)


@app.parser(quest=14)
def parse(file: TextIOWrapper):
    lines = []
    for line in file.readlines():
        dirs = []
        for d in line.strip().split(','):
            dir = d[0]
            dist = int(d[1:])
            match dir:
                case 'R':
                    dirs.append(Vec(dist, 0))
                case 'L':
                    dirs.append(Vec(-dist, 0))
                case 'U':
                    dirs.append(Vec(0, dist))
                case 'D':
                    dirs.append(Vec(0, -dist))
        lines.append(dirs)
    return lines


@app.solver(quest=14, part=1)
def solve(notes: list[list[Vec]]):
    height = 0
    spot = Vec(0, 0)
    for d in notes[0]:
        spot += d
        height = max(spot.y, height)
    return height


@app.solver(quest=14, part=2)
def part2(notes: list[list[Vec]]):
    plant = set()
    for path in notes:
        curr = Vec(0, 0)
        for p in path:
            for _ in range(max(abs(p.x), abs(p.y))):
                curr += Vec(p.x // max(abs(p.x), 1), p.y // max(abs(p.y), 1))
                plant.add(curr)
    return len(plant)


@app.solver(quest=14, part=3)
def part3(notes):
    return 'not solved'
