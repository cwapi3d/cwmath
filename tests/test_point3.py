from __future__ import annotations

import math

import pytest

from cwmath.point3 import Point3
from cwmath.tolerance import ABS_TOL
from cwmath.vec3 import Vec3


def test_point3_plus_vec3_is_point3() -> None:
    result = Point3(1, 2, 3) + Vec3(4, 5, 6)
    assert isinstance(result, Point3)
    assert result == Point3(5, 7, 9)


def test_point3_minus_point3_is_vec3() -> None:
    result = Point3(5, 7, 9) - Point3(1, 2, 3)
    assert isinstance(result, Vec3)
    assert result == Vec3(4, 5, 6)


def test_point3_plus_point3_raises_typeerror() -> None:
    with pytest.raises(TypeError):
        _ = Point3(1, 2, 3) + Point3(4, 5, 6)  # type: ignore[operator]


def test_point3_minus_vec3_is_point3() -> None:
    result = Point3(5, 7, 9) - Vec3(4, 5, 6)
    assert result == Point3(1, 2, 3)


def test_affine_roundtrip() -> None:
    p = Point3(1, 2, 3)
    q = Point3(4, 6, 8)
    assert p + (q - p) == q


def test_point3_is_frozen() -> None:
    point = Point3(1, 2, 3)
    with pytest.raises(AttributeError):
        point.x = 9.0  # type: ignore[misc]


def test_point3_equality_is_exact() -> None:
    assert Point3(1, 2, 3) == Point3(1, 2, 3)
    assert Point3(1, 2, 3) != Point3(1, 2, 3 + 1e-12)
    assert Point3(1, 2, 3) != Vec3(1, 2, 3)


def test_point3_is_close() -> None:
    assert Point3(0, 0, 0).is_close(Point3(0, 0, ABS_TOL))
    assert not Point3(0, 0, 0).is_close(Point3(0, 0, ABS_TOL * 2))
    assert not Point3(1, 2, 3).is_close(Vec3(1, 2, 3))


def test_point3_from_tuple_helpers() -> None:
    point = Point3(1, 2, 3)
    assert point.as_tuple() == (1.0, 2.0, 3.0)
    assert point.with_x(9) == Point3(9, 2, 3)
    assert point.with_y(9) == Point3(1, 9, 3)
    assert point.with_z(9) == Point3(1, 2, 9)


def test_point3_distance_and_lerp() -> None:
    a = Point3(0, 0, 0)
    b = Point3(3, 4, 0)
    assert a.distance(b) == 5.0
    assert a.lerp(b, 0.5) == Point3(1.5, 2.0, 0.0)


def test_point3_indexing_and_iteration_are_read_only() -> None:
    point = Point3(1, 2, 3)
    assert point[0] == 1.0
    assert point[1] == 2.0
    assert point[2] == 3.0
    assert list(point) == [1.0, 2.0, 3.0]
    with pytest.raises(IndexError):
        _ = point[3]
    with pytest.raises(TypeError):
        point[0] = 9.0  # type: ignore[index]


def test_point3_distance_rejects_vec3() -> None:
    with pytest.raises(TypeError):
        Point3(0, 0, 0).distance(Vec3(1, 0, 0))  # type: ignore[arg-type]


def test_point3_lerp_endpoints() -> None:
    a = Point3(1, 2, 3)
    b = Point3(4, 6, 8)
    assert a.lerp(b, 0.0) == a
    assert a.lerp(b, 1.0) == b
    assert math.isclose(a.lerp(b, 0.25).x, 1.75, abs_tol=ABS_TOL)
