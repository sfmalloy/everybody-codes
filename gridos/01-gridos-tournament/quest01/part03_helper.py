def place_states(n: int):
    if n == 0:
        print("PLACE(0) *** CHECK *** SSS")
        return
    print(f"PLACE({n}) *** PLACE({n - 1}) **P SSD")
    place_states(n - 1)


def place_pair_checks():
    bug = "ABCD"
    values = {"A": 0, "B": 1, "C": 3, "D": 5, "_": 0}
    max_val = 0
    for a in bug:
        for b in bug + "_":
            t = values[a] + values[b]
            if b != "_":
                t += 2
            max_val = max(max_val, t)
            print(f"CHECK {a}{b}* PLACE({t}) __* RRS")
    print("CHECK __* STOP *** SSS")
    return max_val


p = place_pair_checks()
place_states(p)
