from collections import defaultdict

def solve(rules: dict[str, list[str]]):
    pops = set()
    iters = 20
    for start in rules.keys():
        termites = defaultdict(int)
        termites[start] = 1
        for _ in range(iters):
            new = defaultdict(int)
            for t in termites:
                for r in rules[t]:
                    new[r] += termites[t]
            termites = new
        pops.add(sum(termites.values()))
    return max(pops) - min(pops)
