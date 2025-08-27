def solve(nullpointers: int):
    acolytes = 1111
    blocks = 20240000

    h = 1
    w = 1
    T = 0
    while T < blocks:
        T += h * w
        h = (h * nullpointers) % acolytes
        w += 2
    w -= 2
    return (T-blocks)*w
