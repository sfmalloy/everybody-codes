from typing import Literal


def solve(dirs: str, grid: list[list[str]]):
    for line in rotate(1, 1, 'L', grid):
        print(''.join(line))
    return grid


def rotate(r: int, c: int, dir: Literal['L', 'R'], grid: list[list[str]]):
    subgrid = [grid[r-1][c-1:c+2], grid[r][c-1:c+2], grid[r+1][c-1:c+2]]
    for line in subgrid:
        print(''.join(line))
    print()
    if dir == 'L':
        subgrid = list(zip(*subgrid))
        subgrid[0], subgrid[2] = subgrid[2], subgrid[0]
    else:
        subgrid[0], subgrid[2] = subgrid[2], subgrid[0]
        subgrid = list(zip(*subgrid))
    return list(map(list, subgrid))
