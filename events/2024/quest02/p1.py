def solve(words: str, inscriptions: list[str]):
    runes = {word:0 for word in words}
    for word in inscriptions[0].split():
        for rune in runes.keys():
            if rune in word:
                runes[rune] += 1
    return sum(runes.values())
