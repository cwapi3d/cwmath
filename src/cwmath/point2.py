"""Frozen 2D point. Affine: Point2 + Vec2 → Point2, Point2 − Point2 → Vec2."""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass
from typing import Protocol, Self

from cwmath.tolerance import ABS_TOL, REL_TOL
from cwmath.tolerance import is_close as close_scalars


class Xy(Protocol):
    """Read-only duck type for anything with ``.x`` / ``.y``."""

    @property
    def x(self) -> float: ...

    @property
    def y(self) -> float: ...


@dataclass(frozen=True, slots=True)
class Point2:
    """A frozen position in 2-space (millimetres, implicit)."""

    x: float
    y: float

    def __post_init__(self) -> None:
        object.__setattr__(self, "x", float(self.x))
        object.__setattr__(self, "y", float(self.y))

    @classmethod
    def from_xy(cls, value: Xy) -> Self:
        return cls(value.x, value.y)

    def as_tuple(self) -> tuple[float, float]:
        return (self.x, self.y)

    def is_close(
        self,
        other: object,
        *,
        abs_tol: float = ABS_TOL,
        rel_tol: float = REL_TOL,
    ) -> bool:
        if not isinstance(other, Point2):
            return False
        return close_scalars(
            self.x, other.x, abs_tol=abs_tol, rel_tol=rel_tol
        ) and close_scalars(self.y, other.y, abs_tol=abs_tol, rel_tol=rel_tol)

    def with_x(self, x: float) -> Point2:
        return Point2(x, self.y)

    def with_y(self, y: float) -> Point2:
        return Point2(self.x, y)

    def distance(self, other: Point2) -> float:
        if not isinstance(other, Point2):
            raise TypeError("distance expects a Point2")
        return (other - self).magnitude()

    def lerp(self, other: Point2, t: float) -> Point2:
        if not isinstance(other, Point2):
            raise TypeError("lerp expects a Point2")
        return self + (other - self) * t

    def __add__(self, other: object) -> Point2:
        from cwmath.vec2 import Vec2

        if isinstance(other, Vec2):
            return Point2(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other: object) -> Point2 | Vec2:
        from cwmath.vec2 import Vec2

        if isinstance(other, Point2):
            return Vec2(self.x - other.x, self.y - other.y)
        if isinstance(other, Vec2):
            return Point2(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __iter__(self) -> Iterator[float]:
        yield self.x
        yield self.y

    def __getitem__(self, index: int) -> float:
        try:
            return (self.x, self.y)[index]
        except IndexError:
            raise IndexError(index) from None
