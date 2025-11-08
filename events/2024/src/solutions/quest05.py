from io import TextIOWrapper
from lib.quest import app

from collections import deque, defaultdict


@app.parser(quest=5)
def parse(file: TextIOWrapper):
    grid: list[deque[int]] = []
    for line in file.readlines():
        row = list(map(int, line.strip().split()))
        for c, col in enumerate(row):
            if len(grid) < c + 1:
                grid.append(deque())
            grid[c].append(col)
    return grid


@app.solver(quest=5, part=1)
def part1(grid: list[deque[int]]):
    round = 0
    while round < 10:
        front = grid[round % len(grid)].popleft()
        line = (round + 1) % len(grid)
        index = front % (2 * len(grid[line]))
        grid[line].insert(index - 1, front)
        round += 1
    return ''.join([str(line[0]) for line in grid])


@app.solver(quest=5, part=2)
def part2(grid: list[deque[int]]):
    round = 0
    seen = defaultdict(int)
    shout = ''
    # I could optimize this but I'm L A Z Y
    while True:
        front = grid[round % len(grid)].popleft()
        line = (round + 1) % len(grid)
        L = len(grid[line])
        limit = 2 * L
        index = (front - 1) % limit
        if index < L:
            side = 'left'
        else:
            side = 'right'
        index %= L
        if side == 'left':
            grid[line].insert(index, front)
        else:
            grid[line].insert(L - index, front)
        round += 1
        shout = int(''.join([str(line[0]) for line in grid]))
        seen[shout] += 1
        if seen[shout] == 2024:
            return int(shout) * round


@app.solver(quest=5, part=3)
def part3(grid: list[deque[int]]):
    round = 0
    seen = set()
    while True:
        front = grid[round % len(grid)].popleft()
        line = (round + 1) % len(grid)
        L = len(grid[line])
        limit = 2 * L
        index = (front - 1) % limit
        if index < L:
            side = 'left'
        else:
            side = 'right'
        index %= L
        if side == 'left':
            grid[line].insert(index, front)
        else:
            grid[line].insert(L - index, front)
        round += 1
        shout = int(''.join([str(line[0]) for line in grid]))
        if (shout, line) in seen:
            break
        seen.add((shout, line))
    return max([p[0] for p in seen])
