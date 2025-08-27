def solve(nullpointers: int):
    acolytes = 10
    blocks = 202400000
    thickness = 1
    width = 1
    columns = []
    area = 0
    while area < blocks:
        columns.append(0)
        for c in range(len(columns)):
            columns[c] += thickness
        area += thickness * width
        thickness = ((thickness * nullpointers) % acolytes) + acolytes
        width += 2
    width -= 2
    columns.pop()
    columns += columns[1:]
    for c in columns:
        area -= (nullpointers * width * c) % acolytes
    return area - blocks
