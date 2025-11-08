from io import TextIOWrapper
from lib.quest import app


@app.parser(quest=2)
def parse(file: TextIOWrapper):
    lines = file.readlines()
    return lines[0][6:].strip().split(','), [line.strip() for line in lines[2:]]


@app.solver(quest=2, part=1)
def part1(words: str, inscriptions: list[str]):
    runes = {word: 0 for word in words}
    for word in inscriptions[0].split():
        for rune in runes.keys():
            if rune in word:
                runes[rune] += 1
    return sum(runes.values())


@app.solver(quest=2, part=2)
def part2(words: str, inscriptions: list[str]):
    def total_runes(runes: str, line: str):
        indices = set()
        for rune in runes:
            index = line.find(rune)
            while index != -1:
                indices |= {i for i in range(index, index + len(rune))}
                index = line.find(rune, index + 1)
        return indices

    total = 0
    for line in inscriptions:
        indices = total_runes(words, line) | total_runes(
            [''.join(reversed(word)) for word in words], line
        )
        total += len(indices)
    return total


@app.solver(quest=2, part=3)
def part3(words: str, inscriptions: list[str]):
    def find_word(rune: str, line: str, wrap: bool):
        L = len(line)
        if wrap:
            line += line[0 : len(rune) - 1]

        index = line.find(rune)
        indices = set()
        while index != -1:
            indices |= {i % L for i in range(index, index + len(rune))}
            index = line.find(rune, index + 1)
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
