from __future__ import annotations

import math

import pytest

from cwmath.point3 import Point3
from cwmath.tolerance import ABS_TOL
from cwmath.vec3 import Vec3


def test_vec3_plus_vec3_is_vec3() -> None:
    result = Vec3(1, 2, 3) + Vec3(4, 5, 6)
    assert isinstance(result, Vec3)
    assert result == Vec3(5, 7, 9)


def test_vec3_plus_point3_raises_typeerror() -> None:
    with pytest.raises(TypeError):
        _ = Vec3(1, 2, 3) + Point3(4, 5, 6)  # type: ignore[operator]


def test_vec3_dot_exact_on_integers() -> None:
    assert Vec3(1, 2, 3).dot(Vec3(4, 5, 6)) == 32
    assert Vec3(1, 0, 0).dot(Vec3(0, 1, 0)) == 0


def test_vec3_cross_axis_triple_is_orthogonal() -> None:
    i = Vec3(1, 0, 0)
    j = Vec3(0, 1, 0)
    k = i.cross(j)
    assert k == Vec3(0, 0, 1)
    assert k.dot(i) == 0
    assert k.dot(j) == 0


def test_vec3_magnitude() -> None:
    assert Vec3(3, 4, 0).magnitude() == 5.0
    assert Vec3.zero().magnitude() == 0.0
    assert abs(Vec3(1, 1, 1).magnitude() - math.sqrt(3.0)) <= ABS_TOL


def test_vec3_normalized_unit_length() -> None:
    unit = Vec3(3, 4, 0).normalized()
    assert abs(unit.magnitude() - 1.0) <= ABS_TOL
    assert unit.is_close(Vec3(0.6, 0.8, 0.0))


def test_vec3_normalize_zero_raises() -> None:
    with pytest.raises(ValueError):
        Vec3(0, 0, 0).normalized()


def test_vec3_angle_to_radians() -> None:
    angle = Vec3(1, 0, 0).angle_to(Vec3(0, 1, 0))
    assert abs(angle - math.pi / 2) <= ABS_TOL
    assert abs(Vec3(1, 0, 0).angle_to(Vec3(1, 0, 0))) <= ABS_TOL


def test_vec3_angle_to_zero_raises() -> None:
    with pytest.raises(ValueError):
        Vec3(1, 0, 0).angle_to(Vec3.zero())


def test_vec3_scale_and_neg() -> None:
    assert Vec3(1, 2, 3) * 2 == Vec3(2, 4, 6)
    assert 2 * Vec3(1, 2, 3) == Vec3(2, 4, 6)
    assert Vec3(2, 4, 6) / 2 == Vec3(1, 2, 3)
    assert -Vec3(1, 2, 3) == Vec3(-1, -2, -3)


def test_vec3_is_frozen() -> None:
    vector = Vec3(1, 2, 3)
    with pytest.raises(AttributeError):
        vector.x = 9.0  # type: ignore[misc]


def test_vec3_equality_is_exact() -> None:
    assert Vec3(1, 2, 3) == Vec3(1, 2, 3)
    assert Vec3(1, 2, 3) != Vec3(1, 2, 3 + 1e-12)


def test_vec3_is_close() -> None:
    assert Vec3(0, 0, 0).is_close(Vec3(0, 0, ABS_TOL))
    assert not Vec3(0, 0, 0).is_close(Vec3(0, 0, ABS_TOL * 2))


def test_vec3_indexing_and_iteration_are_read_only() -> None:
    vector = Vec3(1, 2, 3)
    assert vector[0] == 1.0
    assert list(vector) == [1.0, 2.0, 3.0]
    with pytest.raises(IndexError):
        _ = vector[3]
    with pytest.raises(TypeError):
        vector[0] = 9.0  # type: ignore[index]


def test_vec3_as_tuple_and_with() -> None:
    vector = Vec3(1, 2, 3)
    assert vector.as_tuple() == (1.0, 2.0, 3.0)
    assert vector.with_x(0) == Vec3(0, 2, 3)
