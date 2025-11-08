from io import TextIOWrapper
from lib.quest import app
from typing import Self
from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class Tower:
    x: int
    y: int
    hp: int = 1

    def __add__(self, other: Self) -> Self:
        return Tower(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Self) -> Self:
        return Tower(self.x - other.x, self.y - other.y)


@app.parser(quest=12)
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


@app.solver(quest=12, part=1)
def part1(a: Tower, b: Tower, c: Tower, targets: set[Tower]):
    def throw(src: Tower, power: int, targets: set[Tower]) -> int:
        """
        return the index of the hit target, if any. else 0
        """
        for _ in range(power):
            src += Tower(1, 1)
        for _ in range(power):
            src += Tower(1, 0)
        while src.y > 0:
            src += Tower(1, -1)
            if src in targets:
                return src
        return None

    srcs = [a, b, c]
    power = 0
    ans = 0
    while targets:
        power += 1
        for rank, s in enumerate(srcs, start=1):
            hit = throw(s, power, targets)
            if hit:
                targets.remove(hit)
                ans += power * rank
                power -= 1
                break
    return ans


@app.solver(quest=12, part=2)
def part2(a: Tower, b: Tower, c: Tower, targets: set[Tower]):
    def throw(src: Tower, power: int, targets: set[Tower]) -> Tower:
        """
        return the index of the hit target, if any. else 0
        """
        for _ in range(power):
            src += Tower(1, 1)
            if src in targets:
                return src
            if Tower(src.x, src.y, 2) in targets:
                return Tower(src.x, src.y, 2)

        for _ in range(power):
            src += Tower(1, 0)
            if src in targets:
                return src
            if Tower(src.x, src.y, 2) in targets:
                return Tower(src.x, src.y, 2)

        while src.y > 0:
            src += Tower(1, -1)
            if src in targets:
                return src
            if Tower(src.x, src.y, 2) in targets:
                return Tower(src.x, src.y, 2)
        return None

    srcs = [a, b, c]
    power = 0
    ans = 0
    while targets:
        if len(targets) == 46:
            print(targets)
            break
        power += 1
        for rank, s in enumerate(srcs, start=1):
            hit = throw(s, power, targets)
            if hit:
                print(hit, power, '.ABC'[rank], f'({rank})')
                targets.remove(hit)
                ans += power * rank * hit.hp
                power = 1
                break
    return ans, 'not solved...'


@app.solver(quest=12, part=3)
def part3(notes):
    return 'not solved'
