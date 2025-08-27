from itertools import cycle


def solve(segments: dict[str, list[str]]):
    lst = []
    for k, v in segments.items():
        tot = 0
        val = 10
        for s, _ in zip(cycle(v), range(10)):
            val += s
            tot += val
        lst.append((k, tot))
    return ''.join(k[0] for k in sorted(lst, key=lambda p:-p[1]))
