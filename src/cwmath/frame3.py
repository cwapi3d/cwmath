"""Right-handed rigid frame. Transforms Point3/Vec3 between local and world."""

from __future__ import annotations

from dataclasses import dataclass
from typing import overload

from cwmath.point3 import Point3
from cwmath.tolerance import is_close as close_scalars
from cwmath.vec3 import Vec3


def _require_point3(value: object, name: str) -> None:
    if not isinstance(value, Point3):
        raise TypeError(f'{name} must be a Point3')


def _require_vec3(value: object, name: str) -> None:
    if not isinstance(value, Vec3):
        raise TypeError(f'{name} must be a Vec3')


def _is_unit(axis: Vec3) -> bool:
    return close_scalars(axis.magnitude(), 1.0)


def _is_orthogonal(a: Vec3, b: Vec3) -> bool:
    return close_scalars(a.dot(b), 0.0)


def _require_orthonormal_right_handed(x: Vec3, y: Vec3, z: Vec3) -> None:
    if not (_is_unit(x) and _is_unit(y) and _is_unit(z)):
        raise ValueError('frame axes must be unit length')
    if not (_is_orthogonal(x, y) and _is_orthogonal(y, z) and _is_orthogonal(z, x)):
        raise ValueError('frame axes must be mutually orthogonal')
    if not x.cross(y).is_close(z):
        raise ValueError('frame axes must form a right-handed basis')


@dataclass(frozen=True, slots=True)
class Frame3:
    """A frozen origin plus a right-handed orthonormal basis."""

    origin: Point3
    x_axis: Vec3
    y_axis: Vec3
    z_axis: Vec3

    def __post_init__(self) -> None:
        _require_point3(self.origin, 'origin')
        _require_vec3(self.x_axis, 'x_axis')
        _require_vec3(self.y_axis, 'y_axis')
        _require_vec3(self.z_axis, 'z_axis')
        _require_orthonormal_right_handed(self.x_axis, self.y_axis, self.z_axis)

    @classmethod
    def from_origin_and_axes(cls, origin: Point3, x: Vec3, y: Vec3, z: Vec3) -> Frame3:
        """Build a frame from a known-good unit, orthogonal, right-handed basis."""
        return cls(origin=origin, x_axis=x, y_axis=y, z_axis=z)

    @classmethod
    def from_origin_xy(cls, origin: Point3, x: Vec3, y: Vec3) -> Frame3:
        """Build a right-handed frame from origin + xy, via Gram–Schmidt.

        ``z = x × y``; then orthonormalize x, then y, then z. A zero or
        parallel pair is degenerate and raises ``ValueError``.
        """
        _require_point3(origin, 'origin')
        _require_vec3(x, 'x')
        _require_vec3(y, 'y')

        z = x.cross(y)
        if z.is_close(Vec3.zero()):
            raise ValueError('from_origin_xy: x and y are degenerate')

        try:
            x_hat = x.normalized()
        except ValueError:
            raise ValueError('from_origin_xy: x and y are degenerate') from None

        y_proj = y - x_hat * y.dot(x_hat)
        try:
            y_hat = y_proj.normalized()
        except ValueError:
            raise ValueError('from_origin_xy: x and y are degenerate') from None

        z_proj = z - x_hat * z.dot(x_hat) - y_hat * z.dot(y_hat)
        try:
            z_hat = z_proj.normalized()
        except ValueError:
            raise ValueError('from_origin_xy: x and y are degenerate') from None

        return cls(origin=origin, x_axis=x_hat, y_axis=y_hat, z_axis=z_hat)

    @overload
    def to_world(self, value: Point3) -> Point3: ...

    @overload
    def to_world(self, value: Vec3) -> Vec3: ...

    def to_world(self, value: Point3 | Vec3) -> Point3 | Vec3:
        if isinstance(value, Point3):
            return self.origin + self.x_axis * value.x + self.y_axis * value.y + self.z_axis * value.z
        if isinstance(value, Vec3):
            return self.x_axis * value.x + self.y_axis * value.y + self.z_axis * value.z
        raise TypeError('to_world expects a Point3 or Vec3')

    @overload
    def to_local(self, value: Point3) -> Point3: ...

    @overload
    def to_local(self, value: Vec3) -> Vec3: ...

    def to_local(self, value: Point3 | Vec3) -> Point3 | Vec3:
        if isinstance(value, Point3):
            q = value - self.origin
            return Point3(q.dot(self.x_axis), q.dot(self.y_axis), q.dot(self.z_axis))
        if isinstance(value, Vec3):
            return Vec3(
                value.dot(self.x_axis),
                value.dot(self.y_axis),
                value.dot(self.z_axis),
            )
        raise TypeError('to_local expects a Point3 or Vec3')
