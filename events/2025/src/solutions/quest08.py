from io import TextIOWrapper
from lib.quest import app
from collections import defaultdict, deque
from functools import cache
from itertools import pairwise
import math
from decimal import Decimal


@app.parser(quest=8)
def parse(file: TextIOWrapper) -> str:
    return [int(x) for x in file.read().strip().split(',')]


@app.solver(quest=8, part=1)
def part1(a) -> str:
    c = 0
    for x, y in pairwise(a):
        if abs(y - x) == 16:
            c += 1
    return c


@app.solver(quest=8, part=2)
def part2(notes) -> str:
    def cross(u, v):
        return u[0] * v[1] - v[0] * u[1]

    angle = (2 * math.pi) / max(notes)
    coords = {
        nail: (round(math.cos(angle * nail), 7), round(math.sin(angle * nail), 7))
        for nail in range(1, max(notes) + 1)
    }
    vectors: list[tuple[float, float, float]] = []
    for a, b in pairwise(notes):
        u = coords[a]
        v = coords[b]
        vec = (*u, *v)
        vectors.append(vec)
        # print(vec)

    knots = 0
    for i, (ax, ay, bx, by) in enumerate(vectors):
        k = 0
        for j in range(i - 1, -1, -1):
            (cx, cy, dx, dy) = vectors[j]
            if (
                (ax, ay) == (cx, cy)
                or (ax, ay) == (dx, dy)
                or (bx, by) == (cx, cy)
                or (bx, by) == (dx, dy)
            ):
                continue
            if bx - dx != 0:
                t = (cx - ax) / (bx - dx)
                y0 = ay + by * t
                y1 = cy + dy * t
                if y0 == y1:
                    print(i + 1, j + 1, y0, cx + dx * t)
                    knots += 1
                    k += 1
            else:
                t = (cx - bx) / (ax - dx)
                y0 = by + ay * t
                y1 = cy + dy * t
                if y0 == y1:
                    print(i + 1, j + 1, y0, cx + dx * t)
                    knots += 1
                    k += 1
        # print(i + 1, k)
    return knots


@app.solver(quest=8, part=3)
def part3(a) -> str:
    return


def normalize(f: float) -> float:
    return round(f, 6)


# vectors = []
# count = 0
# for i, j in pairwise(notes):
#     k = 0
#     u = coords[i]
#     v = coords[j]
#     vectors.append((u[0], u[1], v[0], v[1]))
#     x3, y3, x4, y4 = vectors[-1]
#     for x1, y1, x2, y2 in vectors[:-1]:
#         b = ((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4))
#         ax = ((x1 * y2 - y1 * x2) * (x3 - x4)) - ((x1 - x2) * (x3 * y4 - y3 * x4))
#         ay = ((x1 * y2 - y1 * x2) * (y3 - y4)) - ((y1 - y2) * (x3 * y4 - y3 * x4))
#         if abs(b) > 0:
#             x = ax / b
#             y = ay / b
#             if -1 < x < 1 and -1 < y < 1:
#                 print(x, y)
#                 count += 1
#                 k += 1
#     print(k)
