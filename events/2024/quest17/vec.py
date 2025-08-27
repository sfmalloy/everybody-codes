from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True, eq=True)
class Vec:
    r: int
    c: int

    def __add__(self, other: Self) -> Self:
        return Vec(self.r+other.r, self.c+other.c)


    def __sub__(self, other: Self) -> Self:
        return Vec(self.r-other.r, self.c-other.c)
