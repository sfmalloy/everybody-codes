from itertools import batched

def solve(ipt: str):
    vals = {
        'x': 0,
        'A': 0,
        'B': 1,
        'C': 3,
        'D': 5
    }
    total = 0
    for a, b in batched(ipt, 2):
        if a == 'x' or b == 'x':
            total += vals[a] + vals[b]
        else:
            total += vals[a] + vals[b] + 2
    return total
