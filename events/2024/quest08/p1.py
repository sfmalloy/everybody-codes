def solve(blocks: int):
    l = 1
    T = 0
    while T < blocks:
        T += l
        l += 2
    l -= 2
    return (T-blocks)*l
