def solve(words: str, inscriptions: list[str]):
    def find_word(rune: str, line: str, wrap: bool):
        L = len(line)
        if wrap:
            line += line[0:len(rune)-1]

        index = line.find(rune)
        indices = set()
        while index != -1:
            s = {i for i in range(index, index+len(rune))}
            indices |= {i%L for i in range(index, index+len(rune))}
            index = line.find(rune, index+1)
        return indices

    coords = set()
    for r, line in enumerate(inscriptions):
        for word in words:
            coords |= {(r, c) for c in find_word(word, line, True)}
            coords |= {(r, c) for c in find_word(''.join(reversed(word)), line, True)}
    
    for c, line in enumerate(list(''.join(l) for l in [*zip(*inscriptions)])):
        for word in words:
            coords |= {(r, c) for r in find_word(word, line, False)}
            coords |= {(r, c) for r in find_word(''.join(reversed(word)), line, False)}
    return len(coords)
