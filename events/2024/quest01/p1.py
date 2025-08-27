def solve(ipt: str):
    vals = {
        'A': 0,
        'B': 1,
        'C': 3
    }
    total = 0
    for bug in ipt:
        total += vals[bug]
    return total
