from io import TextIOWrapper
from lib.quest import app
from functools import lru_cache
from math import ceil


@app.parser(quest=9)
def parse(file: TextIOWrapper):
    return [int(x) for x in file.readlines()]


@app.solver(quest=9, part=1)
def solve(brightness: list[int]):
    parts = [10, 5, 3, 1]
    ans = 0
    for b in brightness:
        c = 0
        i = 0
        while b > 0 and i < len(parts):
            while b >= parts[i]:
                b -= parts[i]
                c += 1
            if b < 0:
                b += parts[i]
                c -= 1
            i += 1
        ans += c
    return ans


@app.solver(quest=9, part=2)
def part2(brightness: list[int]):
    ans = 0
    for b in brightness:
        ans += search(b, (30, 25, 24, 20, 16, 15, 10, 5, 3, 1))
    return ans


@app.solver(quest=9, part=3)
def part3(brightness: list[int]):
    ans = 0
    parts = (101, 100, 75, 74, 50, 49, 38, 37, 30, 25, 24, 20, 16, 15, 10, 5, 3, 1)
    for target in brightness:
        a = target // 2
        b = ceil(target / 2)
        best = float('inf')
        while b - a <= 100:
            ta = search(a, parts)
            tb = search(b, parts)
            t = ta + tb
            best = min(t, best)
            a -= 1
            b += 1
        ans += best
    return ans


@lru_cache(maxsize=None)
def search(b: int, parts: tuple[int]):
    if b < 0:
        return float('inf')
    elif b == 0:
        return 0
    best = float('inf')
    for p in parts:
        best = min(best, 1 + search(b - p, parts))
    return best
