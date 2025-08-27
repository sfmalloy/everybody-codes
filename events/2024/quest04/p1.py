def solve(nails: list[int]):
    shortest = min(nails)
    d = 0
    for nail in nails:
        d += abs(nail-shortest)
    return d
