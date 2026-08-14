"""Frozen 3D point. Affine: Point3 + Vec3 → Point3, Point3 − Point3 → Vec3."""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass
from typing import Protocol, Self

from cwmath.tolerance import ABS_TOL, REL_TOL
from cwmath.tolerance import is_close as close_scalars


class Xyz(Protocol):
    """Read-only duck type for anything with ``.x`` / ``.y`` / ``.z``."""

    @property
    def x(self) -> float: ...

    @property
    def y(self) -> float: ...

    @property
    def z(self) -> float: ...


@dataclass(frozen=True, slots=True)
class Point3:
    """A frozen position in 3-space (millimetres, implicit)."""

    x: float
    y: float
    z: float

    def __post_init__(self) -> None:
        object.__setattr__(self, "x", float(self.x))
        object.__setattr__(self, "y", float(self.y))
        object.__setattr__(self, "z", float(self.z))

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
        if not isinstance(other, Point3):
            return False
        return (
            close_scalars(self.x, other.x, abs_tol=abs_tol, rel_tol=rel_tol)
            and close_scalars(self.y, other.y, abs_tol=abs_tol, rel_tol=rel_tol)
            and close_scalars(self.z, other.z, abs_tol=abs_tol, rel_tol=rel_tol)
        )

    def with_x(self, x: float) -> Point3:
        return Point3(x, self.y, self.z)

    def with_y(self, y: float) -> Point3:
        return Point3(self.x, y, self.z)

    def with_z(self, z: float) -> Point3:
        return Point3(self.x, self.y, z)

    def distance(self, other: Point3) -> float:
        if not isinstance(other, Point3):
            raise TypeError("distance expects a Point3")
        return (other - self).magnitude()

    def lerp(self, other: Point3, t: float) -> Point3:
        if not isinstance(other, Point3):
            raise TypeError("lerp expects a Point3")
        return self + (other - self) * t

    def __add__(self, other: object) -> Point3:
        from cwmath.vec3 import Vec3

        if isinstance(other, Vec3):
            return Point3(self.x + other.x, self.y + other.y, self.z + other.z)
        return NotImplemented

    def __sub__(self, other: object) -> Point3 | Vec3:
        from cwmath.vec3 import Vec3

        if isinstance(other, Point3):
            return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
        if isinstance(other, Vec3):
            return Point3(self.x - other.x, self.y - other.y, self.z - other.z)
        return NotImplemented

    def __iter__(self) -> Iterator[float]:
        yield self.x
        yield self.y
        yield self.z

    def __getitem__(self, index: int) -> float:
        try:
            return (self.x, self.y, self.z)[index]
        except IndexError:
            raise IndexError(index) from None
