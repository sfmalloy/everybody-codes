from io import TextIOWrapper
from lib.quest import app
from collections import defaultdict


@app.parser(quest=6)
def parse(file: TextIOWrapper) -> str:
    return file.read().strip()


@app.solver(quest=6, part=1)
def part1(notes: str) -> int:
    notes = ''.join(reversed(notes))
    pairs = 0
    for i, a in enumerate(notes):
        for b in notes[i + 1 :]:
            if a == 'a' and a.islower() and b.isupper() and a.upper() == b.upper():
                pairs += 1
    return pairs


@app.solver(quest=6, part=2)
def part2(notes: str) -> int:
    notes = ''.join(reversed(notes))
    pairs = 0
    for i, a in enumerate(notes):
        for b in notes[i + 1 :]:
            if a.islower() and b.isupper() and a.upper() == b.upper():
                pairs += 1
    return pairs


@app.solver(quest=6, part=3)
def part3(notes: str) -> int:
    L = len(notes)
    notes *= 3
    tents: defaultdict[str, list[int]] = defaultdict(list)
    middle_novices = []
    end_novices = []
    for i, person in enumerate(notes):
        if person.isupper():
            tents[person].append(i)
        elif L <= i < 2 * L:
            middle_novices.append(i)
        else:
            end_novices.append(i)
    end_pairs = pair_tents(notes, tents, end_novices)
    middle_pairs = pair_tents(notes, tents, middle_novices)
    return end_pairs + 998 * middle_pairs


def pair_tents(
    notes: str, tents: defaultdict[str, list[int]], novices: list[int]
) -> int:
    pairs = 0
    for i in novices:
        for j in tents[notes[i].upper()]:
            if abs(j - i) <= 1000:
                pairs += 1
            if j - i > 1000:
                break
    return pairs
