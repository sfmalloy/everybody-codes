from io import TextIOWrapper
from lib.quest import app
from collections import defaultdict


@app.parser(quest=11)
def parse(file: TextIOWrapper):
    rules = {}
    for line in file.readlines():
        key, vals = line.split(':')
        vals = vals.strip().split(',')
        rules[key] = vals
    return rules


@app.solver(quest=11, part=1)
def part1(rules: dict[str, list[str]]):
    termites = ['A']
    iters = 4
    for _ in range(iters):
        new = []
        for t in termites:
            new += rules[t]
        termites = new
    return len(termites)


@app.solver(quest=11, part=2)
def part2(rules: dict[str, list[str]]):
    termites = ['Z']
    iters = 10
    for _ in range(iters):
        new = []
        for t in termites:
            new += rules[t]
        termites = new
    return len(termites)


@app.solver(quest=11, part=3)
def part3(rules: dict[str, list[str]]):
    pops = set()
    iters = 20
    for start in rules.keys():
        termites = defaultdict(int)
        termites[start] = 1
        for _ in range(iters):
            new = defaultdict(int)
            for t in termites:
                for r in rules[t]:
                    new[r] += termites[t]
            termites = new
        pops.add(sum(termites.values()))
    return max(pops) - min(pops)
