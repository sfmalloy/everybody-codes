def solve(rules: dict[str, list[str]]):
    termites = ['Z']
    iters = 10
    for _ in range(iters):
        new = []
        for t in termites:
            new += rules[t]
        termites = new
    return len(termites)
