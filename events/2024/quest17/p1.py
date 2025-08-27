from collections import deque, defaultdict
from .vec import Vec


def solve(notes: list[Vec]):
    dists = defaultdict(dict)
    for a in notes:
        for b in notes:
            if a == b:
                continue
            dists[a][b] = abs(a.r - b.r) + abs(a.c - b.c)
    curr = Vec(0, 0)
    visited = set()
    mp = []
    d = 0
    while len(mp) < len(notes):
        print(len(visited), visited)
        best = (float('inf'), None)
        for n in dists[curr]:
            if n in visited:
                continue
            if dists[curr][n] < best[0]:
                best = (dists[curr][n], n)
        mp.append(curr)
        visited.add(curr)
        if best[0] != float('inf'):
            d += best[0]
        curr = best[1]
    mp.append(curr)
    print(visited)
    print(mp)
    return d
