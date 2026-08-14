from __future__ import annotations

import sys

import pytest

from cwmath.cadwork import CadworkNotAvailableError, to_point_3d
from cwmath.point3 import Point3
from cwmath.vec3 import Vec3
from fakes import FakeCadwork, FakePoint3d


def test_from_xyz_point3() -> None:
    assert Point3.from_xyz(FakePoint3d(1, 2, 3)) == Point3(1, 2, 3)


def test_from_xyz_vec3() -> None:
    assert Vec3.from_xyz(FakePoint3d(1, 2, 3)) == Vec3(1, 2, 3)


def test_to_point_3d_with_factory_point3() -> None:
    result = to_point_3d(Point3(1, 2, 3), factory=FakeCadwork)
    assert isinstance(result, FakePoint3d)
    assert (result.x, result.y, result.z) == (1.0, 2.0, 3.0)


def test_to_point_3d_with_factory_vec3() -> None:
    result = to_point_3d(Vec3(4, 5, 6), factory=FakeCadwork())
    assert isinstance(result, FakePoint3d)
    assert (result.x, result.y, result.z) == (4.0, 5.0, 6.0)


def test_to_point_3d_not_available_without_host(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setitem(sys.modules, 'cadwork', None)
    with pytest.raises(CadworkNotAvailableError):
        to_point_3d(Point3(1, 2, 3))


def test_to_point_3d_rejects_raw_xyz() -> None:
    with pytest.raises(TypeError):
        to_point_3d(FakePoint3d(1, 2, 3))  # type: ignore[arg-type]
