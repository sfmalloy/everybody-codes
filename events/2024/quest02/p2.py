def solve(words: str, inscriptions: list[str]):
    def total_runes(runes: str, line: str):
        indices = set()
        for rune in runes:
            index = line.find(rune)
            while index != -1:
                indices |= {i for i in range(index, index+len(rune))}
                index = line.find(rune, index+1)
        return indices

    total = 0
    for line in inscriptions:
        indices = total_runes(words, line) | total_runes([''.join(reversed(word)) for word in words], line)
        total += len(indices)
    return total
