from .vec import Tower

def solve(a: Tower, b: Tower, c: Tower, targets: set[Tower]):
    srcs = [a, b, c]
    power = 0
    ans = 0
    while targets:
        power += 1
        for rank, s in enumerate(srcs, start=1):
            hit = throw(s, power, targets)
            if hit:
                targets.remove(hit)
                ans += power * rank
                power -= 1
                break
    return ans


def throw(src: Tower, power: int, targets: set[Tower]) -> int:
    '''
    return the index of the hit target, if any. else 0
    '''
    for _ in range(power):
        src += Tower(1, 1)
    for _ in range(power):
        src += Tower(1, 0)
    while src.y > 0:
        src += Tower(1, -1)
        if src in targets:
            return src
    return None
