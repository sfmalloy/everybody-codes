from collections import deque, defaultdict


def solve(grid: list[deque[int]]):
    round = 0
    seen = defaultdict(int)
    shout = ''
    # I could optimize this but I'm L A Z Y
    while True:
        front = grid[round % len(grid)].popleft()
        line = (round+1) % len(grid)
        L = len(grid[line])
        limit = 2*L
        index = (front-1) % limit
        if index < L:
            side = 'left'
        else:
            side = 'right'
        index %= L
        if side == 'left':
            grid[line].insert(index, front)
        else:
            grid[line].insert(L-index, front)
        round += 1
        shout = int(''.join([str(line[0]) for line in grid]))
        seen[shout] += 1
        if seen[shout] == 2024:
            return int(shout) * round
