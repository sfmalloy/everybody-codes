def solve(brightness: list[int]):
    parts = [10, 5, 3, 1]
    ans = 0
    for b in brightness:
        c = 0
        i = 0
        while b > 0 and i < len(parts):
            while b >= parts[i]:
                b -= parts[i]
                c += 1
            if b < 0:
                b += parts[i]
                c -= 1
            i += 1
        ans += c
    return ans
