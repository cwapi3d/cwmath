"""Frozen infinite line in 3-space: an origin plus a unit direction."""

from __future__ import annotations

from dataclasses import dataclass

from cwmath.point3 import Point3
from cwmath.vec3 import Vec3


def _require_point3(value: object, name: str) -> None:
    if not isinstance(value, Point3):
        raise TypeError(f"{name} must be a Point3")


def _require_vec3(value: object, name: str) -> None:
    if not isinstance(value, Vec3):
        raise TypeError(f"{name} must be a Vec3")


@dataclass(frozen=True, slots=True)
class Line3:
    """A frozen infinite line defined by an origin and a unit direction."""

    origin: Point3
    direction: Vec3

    def __post_init__(self) -> None:
        _require_point3(self.origin, "origin")
        _require_vec3(self.direction, "direction")
        try:
            unit = self.direction.normalized()
        except ValueError:
            raise ValueError("line direction must be non-zero") from None
        object.__setattr__(self, "direction", unit)

    @classmethod
    def from_origin_direction(cls, origin: Point3, direction: Vec3) -> Line3:
        """Build a line through ``origin`` with a unit ``direction``."""
        return cls(origin=origin, direction=direction)

    @classmethod
    def from_points(cls, a: Point3, b: Point3) -> Line3:
        """Build a line through two distinct points, directed ``a → b``."""
        _require_point3(a, "a")
        _require_point3(b, "b")
        try:
            direction = (b - a).normalized()
        except ValueError:
            raise ValueError("from_points: points are coincident") from None
        return cls(origin=a, direction=direction)

    def parameter(self, point: Point3) -> float:
        """Return ``t`` such that ``origin + t * direction`` is the foot of ``point``."""
        _require_point3(point, "point")
        return (point - self.origin).dot(self.direction)

    def point_at(self, t: float) -> Point3:
        return self.origin + self.direction * t

    def project(self, point: Point3) -> Point3:
        """Return the closest point on this line to ``point``."""
        return self.point_at(self.parameter(point))


def project_point_on_line(point: Point3, line: Line3) -> Point3:
    """Return the closest point on ``line`` to ``point``."""
    return line.project(point)
