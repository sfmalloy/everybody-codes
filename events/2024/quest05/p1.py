from collections import deque


def solve(grid: list[deque[int]]):
    round = 0
    while round < 10:
        front = grid[round % len(grid)].popleft()
        line = (round+1) % len(grid)
        index = front % (2*len(grid[line]))
        grid[line].insert(index-1, front)
        round += 1
    return ''.join([str(line[0]) for line in grid])
