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
    for tri in batched(ipt, 3):
        x_count = tri.count('x')
        if x_count == 0:
            total += sum(vals[x] for x in tri) + 6
        elif x_count == 1:
            total += sum(vals[x] for x in tri) + 2
        else:
            total += sum(vals[x] for x in tri)
    return total
