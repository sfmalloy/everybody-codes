def solve(nails: list[int]):
    best = (0, float('inf'))
    for src in nails:
        d = 0
        for dst in nails:
            d += abs(src-dst)
        if d < best[1]:
            best = (src, d)
    return best[1]
