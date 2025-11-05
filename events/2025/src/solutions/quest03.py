from io import TextIOWrapper
from lib.quest import app


@app.parser(quest=3)
def parse(file: TextIOWrapper):
    return list(map(int, file.read().strip().split(',')))


@app.solver(quest=3, part=1)
def part1(a: list[int]) -> int:
    return sum(set(sorted(a, reverse=True)))


@app.solver(quest=3, part=2)
def part2(a: list[int]) -> int:
    return sum(list(set(sorted(a)))[:20])


@app.solver(quest=3, part=3)
def part3(a: list[int]) -> int:
    s = sorted(a, reverse=True)
    count = 0
    while len(s) > 0:
        m = s[0]
        p = []
        i = 1
        while i < len(s):
            if s[i] >= m:
                p.append(s[i])
            else:
                m = s[i]
            i += 1
        count += 1
        s = p
    return count
