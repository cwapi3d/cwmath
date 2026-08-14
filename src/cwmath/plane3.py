"""Frozen plane in 3-space: a point plus a unit normal."""

from __future__ import annotations

from dataclasses import dataclass

from cwmath.point3 import Point3
from cwmath.tolerance import is_close as close_scalars
from cwmath.vec3 import Vec3


def _require_point3(value: object, name: str) -> None:
    if not isinstance(value, Point3):
        raise TypeError(f"{name} must be a Point3")


def _require_vec3(value: object, name: str) -> None:
    if not isinstance(value, Vec3):
        raise TypeError(f"{name} must be a Vec3")


@dataclass(frozen=True, slots=True)
class Plane3:
    """A frozen plane defined by a point and a unit normal."""

    point: Point3
    normal: Vec3

    def __post_init__(self) -> None:
        _require_point3(self.point, "point")
        _require_vec3(self.normal, "normal")
        try:
            unit = self.normal.normalized()
        except ValueError:
            raise ValueError("plane normal must be non-zero") from None
        object.__setattr__(self, "normal", unit)

    @classmethod
    def from_point_normal(cls, point: Point3, normal: Vec3) -> Plane3:
        """Build a plane through ``point`` with a unit ``normal``."""
        return cls(point=point, normal=normal)

    def signed_distance(self, point: Point3) -> float:
        _require_point3(point, "point")
        return (point - self.point).dot(self.normal)

    def distance(self, point: Point3) -> float:
        return abs(self.signed_distance(point))

    def contains(self, point: Point3) -> bool:
        return close_scalars(self.signed_distance(point), 0.0)

    def project(self, point: Point3) -> Point3:
        """Return the foot of ``point`` on this plane."""
        _require_point3(point, "point")
        return point - self.normal * self.signed_distance(point)

    def as_abcd(self) -> tuple[float, float, float, float]:
        """Return the implicit coefficients ``ax + by + cz + d = 0``."""
        d = -(
            self.normal.x * self.point.x
            + self.normal.y * self.point.y
            + self.normal.z * self.point.z
        )
        return (self.normal.x, self.normal.y, self.normal.z, d)


def project_point_on_plane(point: Point3, plane: Plane3) -> Point3:
    """Return the foot of ``point`` on ``plane``."""
    return plane.project(point)
