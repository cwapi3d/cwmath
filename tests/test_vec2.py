from __future__ import annotations

import math

import pytest

from cwmath.point2 import Point2
from cwmath.tolerance import ABS_TOL
from cwmath.vec2 import Vec2


def test_vec2_plus_vec2_is_vec2() -> None:
    result = Vec2(1, 2) + Vec2(4, 5)
    assert isinstance(result, Vec2)
    assert result == Vec2(5, 7)


def test_vec2_plus_point2_raises_typeerror() -> None:
    with pytest.raises(TypeError):
        _ = Vec2(1, 2) + Point2(4, 5)  # type: ignore[operator]


def test_vec2_dot_exact_on_integers() -> None:
    assert Vec2(1, 2).dot(Vec2(4, 5)) == 14
    assert Vec2(1, 0).dot(Vec2(0, 1)) == 0


def test_vec2_cross_axis_pair_is_scalar() -> None:
    assert Vec2(1, 0).cross(Vec2(0, 1)) == 1.0
    assert Vec2(0, 1).cross(Vec2(1, 0)) == -1.0
    assert Vec2(2, 0).cross(Vec2(0, 3)) == 6.0
    assert Vec2(1, 0).cross(Vec2(1, 0)) == 0.0


def test_vec2_magnitude() -> None:
    assert Vec2(3, 4).magnitude() == 5.0
    assert Vec2.zero().magnitude() == 0.0
    assert abs(Vec2(1, 1).magnitude() - math.sqrt(2.0)) <= ABS_TOL


def test_vec2_normalized_unit_length() -> None:
    unit = Vec2(3, 4).normalized()
    assert abs(unit.magnitude() - 1.0) <= ABS_TOL
    assert unit.is_close(Vec2(0.6, 0.8))


def test_vec2_normalize_zero_raises() -> None:
    with pytest.raises(ValueError):
        Vec2(0, 0).normalized()


def test_vec2_angle_to_radians() -> None:
    angle = Vec2(1, 0).angle_to(Vec2(0, 1))
    assert abs(angle - math.pi / 2) <= ABS_TOL
    assert abs(Vec2(1, 0).angle_to(Vec2(1, 0))) <= ABS_TOL


def test_vec2_angle_to_zero_raises() -> None:
    with pytest.raises(ValueError):
        Vec2(1, 0).angle_to(Vec2.zero())


def test_vec2_scale_and_neg() -> None:
    assert Vec2(1, 2) * 2 == Vec2(2, 4)
    assert 2 * Vec2(1, 2) == Vec2(2, 4)
    assert Vec2(2, 4) / 2 == Vec2(1, 2)
    assert -Vec2(1, 2) == Vec2(-1, -2)


def test_vec2_is_frozen() -> None:
    vector = Vec2(1, 2)
    with pytest.raises(AttributeError):
        vector.x = 9.0  # type: ignore[misc]


def test_vec2_equality_is_exact() -> None:
    assert Vec2(1, 2) == Vec2(1, 2)
    assert Vec2(1, 2) != Vec2(1, 2 + 1e-12)


def test_vec2_is_close() -> None:
    assert Vec2(0, 0).is_close(Vec2(0, ABS_TOL))
    assert not Vec2(0, 0).is_close(Vec2(0, ABS_TOL * 2))


def test_vec2_indexing_and_iteration_are_read_only() -> None:
    vector = Vec2(1, 2)
    assert vector[0] == 1.0
    assert vector[1] == 2.0
    assert list(vector) == [1.0, 2.0]
    with pytest.raises(IndexError):
        _ = vector[2]
    with pytest.raises(TypeError):
        vector[0] = 9.0  # type: ignore[index]


def test_vec2_as_tuple_and_with() -> None:
    vector = Vec2(1, 2)
    assert vector.as_tuple() == (1.0, 2.0)
    assert vector.with_x(0) == Vec2(0, 2)
    assert vector.with_y(0) == Vec2(1, 0)


def test_vec2_from_xy() -> None:
    class _Xy:
        def __init__(self, x: float, y: float) -> None:
            self.x = x
            self.y = y

    assert Vec2.from_xy(_Xy(3, 4)) == Vec2(3, 4)
