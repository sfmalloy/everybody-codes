from io import TextIOWrapper
from lib.quest import app

from collections import defaultdict, deque


@app.parser(quest=6)
def parse(file: TextIOWrapper):
    tree = {}
    for line in file.readlines():
        k, v = line.strip().split(':')
        tree[k] = v.split(',')
    return tree


@app.solver(quest=6, part=1)
def part1(tree: dict[str, list[str]]):
    q = deque([('RR', '')])
    paths = defaultdict(list)
    while len(q) > 0:
        key, path = q.popleft()
        if key == '@':
            path += '@'
            paths[len(path)].append(path)
            continue
        if key in tree:
            for v in tree[key]:
                q.append((v, path + key))
    for v in paths.values():
        if len(v) == 1:
            return v[0]


@app.solver(quest=6, part=2)
def part2(tree: dict[str, list[str]]):
    q = deque([('RR', [])])
    paths = defaultdict(list)
    while len(q) > 0:
        key, path = q.popleft()
        if key == '@':
            path.append('@')
            paths[len(path)].append(path)
            continue
        if key in tree:
            for v in tree[key]:
                q.append((v, path + [key]))
    for v in paths.values():
        if len(v) == 1:
            return ''.join([p[0] for p in v[0]])


@app.solver(quest=6, part=3)
def part3(tree: dict[str, list[str]]):
    q = deque([('RR', [], False, False)])
    paths = defaultdict(list)
    while len(q) > 0:
        key, path, ant, bug = q.popleft()
        if key == 'ANT':
            if ant:
                continue
            ant = True
        elif key == 'BUG':
            if bug:
                continue
            bug = True
        elif key == '@':
            path.append('@')
            paths[len(path)].append(path)
            continue
        if key in tree:
            for v in tree[key]:
                q.append((v, path + [key], ant, bug))
    for v in paths.values():
        if len(v) == 1:
            return ''.join([p[0] for p in v[0]])
