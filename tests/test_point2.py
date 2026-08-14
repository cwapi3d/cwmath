from __future__ import annotations

import math

import pytest

from cwmath.point2 import Point2
from cwmath.tolerance import ABS_TOL
from cwmath.vec2 import Vec2


def test_point2_plus_vec2_is_point2() -> None:
    result = Point2(1, 2) + Vec2(4, 5)
    assert isinstance(result, Point2)
    assert result == Point2(5, 7)


def test_point2_minus_point2_is_vec2() -> None:
    result = Point2(5, 7) - Point2(1, 2)
    assert isinstance(result, Vec2)
    assert result == Vec2(4, 5)


def test_point2_plus_point2_raises_typeerror() -> None:
    with pytest.raises(TypeError):
        _ = Point2(1, 2) + Point2(4, 5)  # type: ignore[operator]


def test_point2_minus_vec2_is_point2() -> None:
    result = Point2(5, 7) - Vec2(4, 5)
    assert result == Point2(1, 2)


def test_affine_roundtrip() -> None:
    p = Point2(1, 2)
    q = Point2(4, 6)
    assert p + (q - p) == q


def test_point2_is_frozen() -> None:
    point = Point2(1, 2)
    with pytest.raises(AttributeError):
        point.x = 9.0  # type: ignore[misc]


def test_point2_equality_is_exact() -> None:
    assert Point2(1, 2) == Point2(1, 2)
    assert Point2(1, 2) != Point2(1, 2 + 1e-12)
    assert Point2(1, 2) != Vec2(1, 2)


def test_point2_is_close() -> None:
    assert Point2(0, 0).is_close(Point2(0, ABS_TOL))
    assert not Point2(0, 0).is_close(Point2(0, ABS_TOL * 2))
    assert not Point2(1, 2).is_close(Vec2(1, 2))


def test_point2_from_tuple_helpers() -> None:
    point = Point2(1, 2)
    assert point.as_tuple() == (1.0, 2.0)
    assert point.with_x(9) == Point2(9, 2)
    assert point.with_y(9) == Point2(1, 9)


def test_point2_from_xy() -> None:
    class _Xy:
        def __init__(self, x: float, y: float) -> None:
            self.x = x
            self.y = y

    assert Point2.from_xy(_Xy(3, 4)) == Point2(3, 4)


def test_point2_distance_and_lerp() -> None:
    a = Point2(0, 0)
    b = Point2(3, 4)
    assert a.distance(b) == 5.0
    assert a.lerp(b, 0.5) == Point2(1.5, 2.0)


def test_point2_indexing_and_iteration_are_read_only() -> None:
    point = Point2(1, 2)
    assert point[0] == 1.0
    assert point[1] == 2.0
    assert list(point) == [1.0, 2.0]
    with pytest.raises(IndexError):
        _ = point[2]
    with pytest.raises(TypeError):
        point[0] = 9.0  # type: ignore[index]


def test_point2_distance_rejects_vec2() -> None:
    with pytest.raises(TypeError):
        Point2(0, 0).distance(Vec2(1, 0))  # type: ignore[arg-type]


def test_point2_lerp_endpoints() -> None:
    a = Point2(1, 2)
    b = Point2(4, 6)
    assert a.lerp(b, 0.0) == a
    assert a.lerp(b, 1.0) == b
    assert math.isclose(a.lerp(b, 0.25).x, 1.75, abs_tol=ABS_TOL)
