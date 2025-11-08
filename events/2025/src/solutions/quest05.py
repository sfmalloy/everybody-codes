from io import TextIOWrapper
from dataclasses import dataclass

from lib.quest import app


@app.parser(quest=5)
def parse(file: TextIOWrapper, part: int):
    if part == 1:
        a, b = file.read().strip().split(':')
        return list(map(int, b.split(',')))
    elif part == 2:
        lines = []
        for line in file.readlines():
            a, b = line.strip().split(':')
            lines.append(list(map(int, b.split(','))))
        return lines
    else:
        lines = []
        for line in file.readlines():
            a, b = line.strip().split(':')
            lines.append((int(a), list(map(int, b.split(',')))))
        return lines


@app.solver(quest=5, part=1)
def part1(notes: list[int]):
    return get_strength(notes)


@app.solver(quest=5, part=2)
def part2(notes: list[list[int]]):
    swords = [get_strength(sword) for sword in notes]
    return max(swords) - min(swords)


def get_strength(line: list[int]):
    sword = [[0, 0, 0] for _ in range(len(line))]
    sword[0][1] = line[0]
    for i in line[1:]:
        for fragment in sword:
            if not fragment[1]:
                fragment[1] = i
                break
            elif not fragment[0] and i < fragment[1]:
                fragment[0] = i
                break
            elif not fragment[2] and i > fragment[1]:
                fragment[2] = i
                break
    middle = []
    for fragment in sword:
        middle.append(fragment[1])
    while middle[-1] == 0:
        middle.pop()
    return int(''.join([str(digit) for digit in middle]))


@dataclass
class Sword:
    quality: int
    rows: list[int]
    id: int

    def __lt__(self, other: 'Sword'):
        if self.quality < other.quality:
            return True
        if self.quality > other.quality:
            return False
        for a, b in zip(self.rows, other.rows):
            if a < b:
                return True
            if a > b:
                return False
        return self.id < other.id

    def __str__(self):
        s = ''
        for row in self.rows:
            s += str(row) + '\n'
        return s


@app.solver(quest=5, part=3)
def part3(instructions: list[tuple[int, list[int]]]):
    swords: list[Sword] = []
    for id, line in instructions:
        sword = [[0, 0, 0] for _ in range(len(line))]
        sword[0][1] = line[0]
        for i in line[1:]:
            for fragment in sword:
                if not fragment[1]:
                    fragment[1] = i
                    break
                elif not fragment[0] and i < fragment[1]:
                    fragment[0] = i
                    break
                elif not fragment[2] and i > fragment[1]:
                    fragment[2] = i
                    break

        middle = []
        rows = []
        for fragment in sword:
            middle.append(fragment[1])
            row = ''.join([str(x if x != 0 else '') for x in fragment])
            if row:
                rows.append(int(row))
        while middle[-1] == 0:
            middle.pop()
        quality = int(''.join([str(digit) for digit in middle]))
        swords.append(Sword(quality, rows, id))

    return sum(
        i * sword.id for i, sword in enumerate(sorted(swords, reverse=True), start=1)
    )
