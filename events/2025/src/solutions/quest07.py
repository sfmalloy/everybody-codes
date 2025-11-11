from io import TextIOWrapper
from lib.quest import app
from collections import defaultdict


@app.parser(quest=7)
def parse(file: TextIOWrapper) -> str:
    lines = [line.strip() for line in file.readlines()]
    rules = defaultdict(list)
    for line in lines[2:]:
        line = line.strip()
        key, vals = line.split(' > ')
        vals = vals.split(',')
        rules[key] = vals
    return lines[0].split(','), rules


@app.solver(quest=7, part=1)
def part1(names: list[str], rules: defaultdict[str, list[str]]) -> str:
    for name in names:
        if check(name, name[0], rules):
            return name


@app.solver(quest=7, part=2)
def part2(names: list[str], rules: defaultdict[str, list[str]]) -> int:
    total = 0
    for i, name in enumerate(names, start=1):
        if check(name, name[0], rules):
            total += i
    return total


@app.solver(quest=7, part=3)
def part3(names: list[str], rules: defaultdict[str, list[str]]) -> int:
    found = set()

    def combos(val: str, count: int = 0) -> int:
        if 7 <= len(val) <= 11 and val not in found:
            count += 1
        found.add(val)
        if len(val) == 11:
            return count
        if val[-1] not in rules:
            return count
        for rule in rules[val[-1]]:
            count = combos(val + rule, count)
        return count

    total = 0
    for name in names:
        if check(name, name[0], rules):
            total += combos(name)
    return total


def check(key: str, val: str, rules: defaultdict[str, list[str]]) -> bool:
    if val == key:
        return True
    if len(val) > len(key):
        return False
    for rule in rules[val[-1]]:
        if check(key, val + rule, rules):
            return True
    return False
