"""Frozen 2D vector. Affine: Vec2 + Vec2 → Vec2; Vec2 + Point2 is illegal."""

from __future__ import annotations

import math
import numbers
from collections.abc import Iterator
from dataclasses import dataclass
from typing import Self

from cwmath.point2 import Xy
from cwmath.tolerance import ABS_TOL, REL_TOL
from cwmath.tolerance import is_close as close_scalars


@dataclass(frozen=True, slots=True)
class Vec2:
    """A frozen displacement / direction in 2-space."""

    x: float
    y: float

    def __post_init__(self) -> None:
        object.__setattr__(self, "x", float(self.x))
        object.__setattr__(self, "y", float(self.y))

    @classmethod
    def zero(cls) -> Self:
        return cls(0.0, 0.0)

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
        if not isinstance(other, Vec2):
            return False
        return close_scalars(
            self.x, other.x, abs_tol=abs_tol, rel_tol=rel_tol
        ) and close_scalars(self.y, other.y, abs_tol=abs_tol, rel_tol=rel_tol)

    def with_x(self, x: float) -> Vec2:
        return Vec2(x, self.y)

    def with_y(self, y: float) -> Vec2:
        return Vec2(self.x, y)

    def dot(self, other: Vec2) -> float:
        if not isinstance(other, Vec2):
            raise TypeError("dot expects a Vec2")
        return self.x * other.x + self.y * other.y

    def cross(self, other: Vec2) -> float:
        """Signed parallelogram area of ``self`` × ``other``."""
        if not isinstance(other, Vec2):
            raise TypeError("cross expects a Vec2")
        return self.x * other.y - self.y * other.x

    def magnitude(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)

    def normalized(self) -> Vec2:
        mag = self.magnitude()
        if mag == 0.0:
            raise ValueError("cannot normalize a zero vector")
        return self / mag

    def angle_to(self, other: Vec2) -> float:
        if not isinstance(other, Vec2):
            raise TypeError("angle_to expects a Vec2")
        cosine = self.normalized().dot(other.normalized())
        return math.acos(max(-1.0, min(1.0, cosine)))

    def __add__(self, other: object) -> Vec2:
        if isinstance(other, Vec2):
            return Vec2(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other: object) -> Vec2:
        if isinstance(other, Vec2):
            return Vec2(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __neg__(self) -> Vec2:
        return Vec2(-self.x, -self.y)

    def __mul__(self, other: object) -> Vec2:
        if isinstance(other, bool) or not isinstance(other, numbers.Real):
            return NotImplemented
        scalar = float(other)
        return Vec2(self.x * scalar, self.y * scalar)

    def __rmul__(self, other: object) -> Vec2:
        return self.__mul__(other)

    def __truediv__(self, other: object) -> Vec2:
        if isinstance(other, bool) or not isinstance(other, numbers.Real):
            return NotImplemented
        scalar = float(other)
        return Vec2(self.x / scalar, self.y / scalar)

    def __iter__(self) -> Iterator[float]:
        yield self.x
        yield self.y

    def __getitem__(self, index: int) -> float:
        try:
            return (self.x, self.y)[index]
        except IndexError:
            raise IndexError(index) from None
