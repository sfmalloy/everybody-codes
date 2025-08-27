from functools import lru_cache


def solve(brightness: list[int]):
    ans = 0
    for b in brightness:
        ans += search(b, (30, 25, 24, 20, 16, 15, 10, 5, 3, 1))
    return ans


@lru_cache(maxsize=None)
def search(b: int, parts: tuple[int]):
    if b < 0:
        return float('inf')
    elif b == 0:
        return 0
    best = float('inf')
    for p in parts:
        best = min(best, 1 + search(b-p, parts))
    return best
