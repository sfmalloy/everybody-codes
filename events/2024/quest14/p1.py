from .model import Vec


def solve(notes: list[list[Vec]]):
    height = 0
    spot = Vec(0, 0)
    for d in notes[0]:
        spot += d
        height = max(spot.y, height)
    return height
