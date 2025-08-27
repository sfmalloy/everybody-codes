from collections import deque
from .model import Vec

def solve(grid: list[str]):
    q = deque([(Vec(0, len(grid[0])//2), 0, 0)])
    visited = set()
    while True:
        pos, steps, dir = q.popleft()
        if (pos, dir) in visited:
            continue
        visited.add((pos, dir))
        if grid[pos.r][pos.c] == 'H':
            return steps * 2

        steps += 1
        if pos.r > 0:
            new = Vec(pos.r - 1, pos.c)
            if validate_pos(grid, new):
                q.append((new, steps, 0))
        if pos.c > 0:
            new = Vec(pos.r, pos.c - 1)
            if validate_pos(grid, new):
                q.append((new, steps, 1))
        if pos.r + 1 < len(grid):
            new = Vec(pos.r + 1, pos.c)
            if validate_pos(grid, new):
                q.append((new, steps, 2))
        if pos.c + 1 < len(grid[pos.r]):
            new = Vec(pos.r, pos.c + 1)
            if validate_pos(grid, new):
                q.append((new, steps, 3))


def validate_pos(grid, pos):
    return grid[pos.r][pos.c] != '#'
