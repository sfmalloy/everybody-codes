def solve(grid: list[list[str]]):
    # pad grid with '.' on edges
    grid = [['.' for _ in grid[0]]] + grid + [['.' for _ in grid[0]]]
    grid = [['.'] + row + ['.'] for row in grid]

    blocks = 0
    # 1. count blocks
    # 2. flood fill copy to new grid, removing any blocks that have '.' as a neighbor
    found = True
    while found:
        found = False
        for row in grid:
            for col in row:
                if col == '#':
                    blocks += 1
        new_grid = [['.' for _ in line] for line in grid]
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if col == '#':
                    if (
                        r-1 >= 0 and grid[r-1][c] == '#'
                        and r+1 < len(grid) and grid[r+1][c] == '#'
                        and c-1 >= 0 and grid[r][c-1] == '#'
                        and c+1 < len(grid[r]) and grid[r][c+1] == '#'
                        and grid[r+1][c+1] == '#'
                        and grid[r+1][c-1] == '#'
                        and grid[r-1][c+1] == '#'
                        and grid[r-1][c-1] == '#'
                    ):
                        new_grid[r][c] = '#'
                        found = True
                else:
                    new_grid[r][c] = '.'
        grid = new_grid
    return blocks
