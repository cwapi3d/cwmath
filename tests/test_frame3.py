from __future__ import annotations

import math

import pytest

from cwmath.frame3 import Frame3
from cwmath.point3 import Point3
from cwmath.tolerance import ABS_TOL
from cwmath.vec3 import Vec3


def _identity(origin: Point3 | None = None) -> Frame3:
    return Frame3.from_origin_and_axes(
        origin if origin is not None else Point3(0, 0, 0),
        Vec3(1, 0, 0),
        Vec3(0, 1, 0),
        Vec3(0, 0, 1),
    )


def _rotated_translated() -> Frame3:
    """90° about Z, origin at (10, 20, 30)."""
    return Frame3.from_origin_and_axes(
        Point3(10, 20, 30),
        Vec3(0, 1, 0),
        Vec3(-1, 0, 0),
        Vec3(0, 0, 1),
    )


def test_construct_identity_axes_are_unit() -> None:
    frame = _identity()
    assert frame.x_axis.is_close(Vec3(1, 0, 0))
    assert frame.y_axis.is_close(Vec3(0, 1, 0))
    assert frame.z_axis.is_close(Vec3(0, 0, 1))
    assert abs(frame.x_axis.magnitude() - 1.0) <= ABS_TOL
    assert abs(frame.y_axis.magnitude() - 1.0) <= ABS_TOL
    assert abs(frame.z_axis.magnitude() - 1.0) <= ABS_TOL


def test_construct_rotated_translated_frame() -> None:
    frame = _rotated_translated()
    assert frame.origin == Point3(10, 20, 30)
    assert abs(frame.x_axis.magnitude() - 1.0) <= ABS_TOL
    assert abs(frame.y_axis.magnitude() - 1.0) <= ABS_TOL
    assert abs(frame.z_axis.magnitude() - 1.0) <= ABS_TOL
    assert frame.x_axis.cross(frame.y_axis).is_close(frame.z_axis)


def test_construct_from_origin_xy_builds_right_handed_unit() -> None:
    frame = Frame3.from_origin_xy(
        Point3(1, 2, 3),
        Vec3(2, 0, 0),
        Vec3(1, 1, 0),
    )
    assert frame.origin == Point3(1, 2, 3)
    assert frame.x_axis.is_close(Vec3(1, 0, 0))
    assert frame.y_axis.is_close(Vec3(0, 1, 0))
    assert frame.z_axis.is_close(Vec3(0, 0, 1))
    assert frame.x_axis.cross(frame.y_axis).is_close(frame.z_axis)


def test_construct_bad_basis_non_unit_raises() -> None:
    with pytest.raises(ValueError):
        Frame3.from_origin_and_axes(
            Point3(0, 0, 0),
            Vec3(2, 0, 0),
            Vec3(0, 1, 0),
            Vec3(0, 0, 1),
        )


def test_construct_bad_basis_not_orthogonal_raises() -> None:
    diagonal = Vec3(1 / math.sqrt(2), 1 / math.sqrt(2), 0)
    with pytest.raises(ValueError):
        Frame3.from_origin_and_axes(
            Point3(0, 0, 0),
            Vec3(1, 0, 0),
            diagonal,
            Vec3(0, 0, 1),
        )


def test_construct_bad_basis_left_handed_raises() -> None:
    with pytest.raises(ValueError):
        Frame3.from_origin_and_axes(
            Point3(0, 0, 0),
            Vec3(1, 0, 0),
            Vec3(0, 1, 0),
            Vec3(0, 0, -1),
        )


def test_construct_from_origin_xy_degenerate_raises() -> None:
    origin = Point3(0, 0, 0)
    with pytest.raises(ValueError):
        Frame3.from_origin_xy(origin, Vec3(1, 0, 0), Vec3(2, 0, 0))
    with pytest.raises(ValueError):
        Frame3.from_origin_xy(origin, Vec3(0, 0, 0), Vec3(0, 1, 0))


def test_point_roundtrip_identity() -> None:
    frame = _identity()
    point = Point3(1, 2, 3)
    assert frame.to_world(point) == point
    assert frame.to_local(point) == point
    assert frame.to_local(frame.to_world(point)).is_close(point)


def test_point_roundtrip_translated_rotated() -> None:
    frame = _rotated_translated()
    point = Point3(1, 2, 3)
    world = frame.to_world(point)
    assert world.is_close(Point3(8, 21, 33))
    assert frame.to_local(world).is_close(point)
    assert frame.to_local(frame.to_world(point)).is_close(point)


def test_vec_roundtrip_ignores_origin() -> None:
    vector = Vec3(1, 2, 3)
    at_origin = _identity()
    shifted = _identity(Point3(100, -40, 7))
    assert at_origin.to_world(vector).is_close(shifted.to_world(vector))
    assert at_origin.to_world(vector).is_close(vector)
    assert shifted.to_world(vector).is_close(vector)
    assert isinstance(shifted.to_world(vector), Vec3)


def test_vec_roundtrip_translated_rotated() -> None:
    frame = _rotated_translated()
    vector = Vec3(1, 2, 3)
    world = frame.to_world(vector)
    assert world.is_close(Vec3(-2, 1, 3))
    assert isinstance(world, Vec3)
    assert frame.to_local(world).is_close(vector)
    assert frame.to_local(frame.to_world(vector)).is_close(vector)


def test_frame3_is_frozen() -> None:
    frame = _identity()
    with pytest.raises(AttributeError):
        frame.origin = Point3(1, 0, 0)  # type: ignore[misc]
