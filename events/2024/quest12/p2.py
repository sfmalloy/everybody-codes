from .vec import Tower

def solve(a: Tower, b: Tower, c: Tower, targets: set[Tower]):
    srcs = [a, b, c]
    power = 0
    ans = 0
    while targets:
        if len(targets) == 46:
            print(targets)
            break
        power += 1
        for rank, s in enumerate(srcs, start=1):
            hit = throw(s, power, targets)
            if hit:
                print(hit, power, '.ABC'[rank], f'({rank})')
                targets.remove(hit)
                ans += power * rank * hit.hp
                power = 1
                break
    return ans


def throw(src: Tower, power: int, targets: set[Tower]) -> Tower:
    '''
    return the index of the hit target, if any. else 0
    '''
    for _ in range(power):
        src += Tower(1, 1)
        if src in targets:
            return src
        if Tower(src.x, src.y, 2) in targets:
            return Tower(src.x, src.y, 2)

    for _ in range(power):
        src += Tower(1, 0)
        if src in targets:
            return src
        if Tower(src.x, src.y, 2) in targets:
            return Tower(src.x, src.y, 2)

    while src.y > 0:
        src += Tower(1, -1)
        if src in targets:
            return src
        if Tower(src.x, src.y, 2) in targets:
            return Tower(src.x, src.y, 2)
    return None
