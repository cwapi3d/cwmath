"""Lazy ``cadwork.point_3d`` adapter. Domain types never import the host."""

from __future__ import annotations

from typing import Protocol

from cwmath.point3 import Point3, Xyz
from cwmath.vec3 import Vec3


class CadworkNotAvailableError(RuntimeError):
    """Raised when ``to_point_3d`` has neither a factory nor a host module."""


class Point3dFactory(Protocol):
    """Callable host / fake that builds an ``Xyz`` from three coordinates."""

    def point_3d(self, x: float, y: float, z: float) -> Xyz: ...


def to_point_3d(
    value: Point3 | Vec3,
    *,
    factory: Point3dFactory | None = None,
) -> Xyz:
    """Convert a ``Point3`` or ``Vec3`` to a host (or fake) ``point_3d``.

    ``factory`` is the test seam (architecture §5). When omitted, ``cadwork``
    is imported only at this call site.
    """
    if not isinstance(value, (Point3, Vec3)):
        raise TypeError("to_point_3d expects a Point3 or Vec3")
    if factory is None:
        try:
            import cadwork as host
        except ImportError as exc:
            raise CadworkNotAvailableError(
                "cadwork is not available; pass factory= to construct "
                "a point_3d outside the cadwork host"
            ) from exc
        factory = host
    return factory.point_3d(value.x, value.y, value.z)
