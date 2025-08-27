from itertools import cycle

def solve(segments: dict[str, list[str]]):
    with open('quest07/track2.txt') as f:
        track = f.read().strip()
    lst = []
    for k, v in segments.items():
        lst.append((k, check_plan(v, track)))
    return ''.join(k[0] for k in sorted(lst, key=lambda p:-p[1]))


def check_plan(plan: str, track):
    it = cycle(plan)
    tot = 0
    val = 10
    # for _ in range(len(track)*10):
    for s, t in zip(it, track*10):
        if t == '-':
            s = -1
        elif t == '+':
            s = 1
        val += s
        tot += val
    return tot
