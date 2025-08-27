def solve(grid: list[list[str]]):
    ans = ''
    for r in range(2, 6):
        row = set(filter(lambda char:char not in '.*', grid[r]))
        for c in range(2, 6):
            col = set(filter(lambda char:char not in '.*', [grid[rr][c] for rr in range(len(grid))]))
            same = list(row & col)[0]
            grid[r][c] = same
            ans += same
    return ans
