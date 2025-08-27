from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True, eq=True)
class Tower:
    x: int
    y: int
    hp: int = 1

    def __add__(self, other: Self) -> Self:
        return Tower(self.x+other.x, self.y+other.y)


    def __sub__(self, other: Self) -> Self:
        return Tower(self.x-other.x, self.y-other.y)
