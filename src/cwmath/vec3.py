"""Frozen 3D vector. Affine: Vec3 + Vec3 → Vec3; Vec3 + Point3 is illegal."""

from __future__ import annotations

import math
import numbers
from collections.abc import Iterator
from dataclasses import dataclass
from typing import Self

from cwmath.point3 import Xyz
from cwmath.tolerance import ABS_TOL, REL_TOL
from cwmath.tolerance import is_close as close_scalars


@dataclass(frozen=True, slots=True)
class Vec3:
    """A frozen displacement / direction in 3-space."""

    x: float
    y: float
    z: float

    def __post_init__(self) -> None:
        object.__setattr__(self, "x", float(self.x))
        object.__setattr__(self, "y", float(self.y))
        object.__setattr__(self, "z", float(self.z))

    @classmethod
    def zero(cls) -> Self:
        return cls(0.0, 0.0, 0.0)

    @classmethod
    def from_xyz(cls, value: Xyz) -> Self:
        return cls(value.x, value.y, value.z)

    def as_tuple(self) -> tuple[float, float, float]:
        return (self.x, self.y, self.z)

    def is_close(
        self,
        other: object,
        *,
        abs_tol: float = ABS_TOL,
        rel_tol: float = REL_TOL,
    ) -> bool:
        if not isinstance(other, Vec3):
            return False
        return (
            close_scalars(self.x, other.x, abs_tol=abs_tol, rel_tol=rel_tol)
            and close_scalars(self.y, other.y, abs_tol=abs_tol, rel_tol=rel_tol)
            and close_scalars(self.z, other.z, abs_tol=abs_tol, rel_tol=rel_tol)
        )

    def with_x(self, x: float) -> Vec3:
        return Vec3(x, self.y, self.z)

    def with_y(self, y: float) -> Vec3:
        return Vec3(self.x, y, self.z)

    def with_z(self, z: float) -> Vec3:
        return Vec3(self.x, self.y, z)

    def dot(self, other: Vec3) -> float:
        if not isinstance(other, Vec3):
            raise TypeError("dot expects a Vec3")
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other: Vec3) -> Vec3:
        if not isinstance(other, Vec3):
            raise TypeError("cross expects a Vec3")
        return Vec3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )

    def magnitude(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def normalized(self) -> Vec3:
        mag = self.magnitude()
        if mag == 0.0:
            raise ValueError("cannot normalize a zero vector")
        return self / mag

    def angle_to(self, other: Vec3) -> float:
        if not isinstance(other, Vec3):
            raise TypeError("angle_to expects a Vec3")
        cosine = self.normalized().dot(other.normalized())
        return math.acos(max(-1.0, min(1.0, cosine)))

    def __add__(self, other: object) -> Vec3:
        if isinstance(other, Vec3):
            return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
        return NotImplemented

    def __sub__(self, other: object) -> Vec3:
        if isinstance(other, Vec3):
            return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
        return NotImplemented

    def __neg__(self) -> Vec3:
        return Vec3(-self.x, -self.y, -self.z)

    def __mul__(self, other: object) -> Vec3:
        if isinstance(other, bool) or not isinstance(other, numbers.Real):
            return NotImplemented
        scalar = float(other)
        return Vec3(self.x * scalar, self.y * scalar, self.z * scalar)

    def __rmul__(self, other: object) -> Vec3:
        return self.__mul__(other)

    def __truediv__(self, other: object) -> Vec3:
        if isinstance(other, bool) or not isinstance(other, numbers.Real):
            return NotImplemented
        scalar = float(other)
        return Vec3(self.x / scalar, self.y / scalar, self.z / scalar)

    def __iter__(self) -> Iterator[float]:
        yield self.x
        yield self.y
        yield self.z

    def __getitem__(self, index: int) -> float:
        try:
            return (self.x, self.y, self.z)[index]
        except IndexError:
            raise IndexError(index) from None
