from .model import Vec


def solve(notes: list[list[Vec]]):
    plant = set()
    for path in notes:
        curr = Vec(0, 0)
        for p in path:
            for _ in range(max(abs(p.x), abs(p.y))):
                curr += Vec(p.x // max(abs(p.x), 1), p.y // max(abs(p.y), 1))
                plant.add(curr)
    return len(plant)
