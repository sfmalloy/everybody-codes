from io import TextIOWrapper
from lib.quest import app


@app.parser(quest=6)
def parse(file: TextIOWrapper, part: int) -> str:
    if part == 3:
        return file.read().strip()
    return ''.join(reversed(file.read().strip()))


@app.solver(quest=6, part=1)
def part1(notes: str) -> int:
    pairs = 0
    for i, a in enumerate(notes):
        for b in notes[i + 1 :]:
            if a == 'a' and a.islower() and b.isupper() and a.upper() == b.upper():
                pairs += 1
    return pairs


@app.solver(quest=6, part=2)
def part2(notes: str) -> int:
    pairs = 0
    for i, a in enumerate(notes):
        for b in notes[i + 1 :]:
            if a.islower() and b.isupper() and a.upper() == b.upper():
                pairs += 1
    return pairs


@app.solver(quest=6, part=3)
def part3(notes: str) -> int:
    middle = 0
    sides = 0
    L = len(notes)
    for i, tent in enumerate(notes):
        if not tent.isupper():
            continue
        t = tent.lower()
        for j in range(i - 1000, i + 1001):
            k = j % L
            if notes[k].isupper() or t != notes[k]:
                continue
            middle += 1
            if j < L:
                sides += 1
            if j >= 0:
                sides += 1
    return sides + 998 * middle
