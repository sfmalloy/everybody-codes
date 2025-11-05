from io import TextIOWrapper
from lib.quest import app

from dataclasses import dataclass
import re
from typing import Self


@dataclass
class ComplexNumber:
    x: int
    y: int

    def __add__(self, other: Self) -> Self:
        return ComplexNumber(self.x + other.x, self.y + other.y)

    def __truediv__(self, other: Self) -> Self:
        return ComplexNumber(int(self.x / other.x), int(self.y / other.y))

    def __mul__(self, other: Self) -> Self:
        return ComplexNumber(
            self.x * other.x - self.y * other.y, self.x * other.y + self.y * other.x
        )

    def __str__(self):
        return f'[{self.x},{self.y}]'

    def __repr__(self):
        return self.__str__()


@app.parser(quest=2)
def parse(file: TextIOWrapper) -> ComplexNumber:
    pair = re.match(r'A=\[(-?\d+),(-?\d+)\]', file.read())
    x, y = map(int, pair.groups())
    return ComplexNumber(x, y)


@app.solver(quest=2, part=1)
def part1(a: ComplexNumber) -> str:
    res = ComplexNumber(0, 0)
    for _ in range(3):
        res = res * res
        res = res / ComplexNumber(10, 10)
        res = res + a
    return str(res)


@app.solver(quest=2, part=2)
def part2(a: ComplexNumber) -> str:
    count = 0
    for y in range(0, 101):
        for x in range(0, 101):
            if engrave(ComplexNumber(a.x + 10 * x, a.y + 10 * y)):
                count += 1
    return count


@app.solver(quest=2, part=3)
def part3(a: ComplexNumber) -> str:
    count = 0
    for y in range(0, 1001):
        for x in range(0, 1001):
            if engrave(ComplexNumber(a.x + x, a.y + y)):
                count += 1
    return count


def engrave(point: ComplexNumber):
    res = ComplexNumber(0, 0)
    for _ in range(100):
        res = res * res
        res = res / ComplexNumber(100000, 100000)
        res = res + point
        if abs(res.x) > 1000000 or abs(res.y) > 1000000:
            return False
    return True
