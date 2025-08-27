from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True, eq=True)
class Vec:
    x: int
    y: int

    def __add__(self, other: Self) -> Self:
        return Vec(self.x+other.x, self.y+other.y)


    def __sub__(self, other: Self) -> Self:
        return Vec(self.x-other.x, self.y-other.y)
