from __future__ import annotations

import pytest

from fakes import FakeCadwork, FakePoint3d


def test_fake_point3d_xyz() -> None:
    point = FakePoint3d(1.0, 2.0, 3.0)
    assert point.x == 1.0
    assert point.y == 2.0
    assert point.z == 3.0


def test_fake_point3d_getitem() -> None:
    point = FakePoint3d(1.0, 2.0, 3.0)
    assert point[0] == 1.0
    assert point[1] == 2.0
    assert point[2] == 3.0
    with pytest.raises(IndexError):
        _ = point[3]


def test_fake_point3d_is_frozen() -> None:
    point = FakePoint3d(1.0, 2.0, 3.0)
    with pytest.raises(AttributeError):
        point.x = 9.0  # type: ignore[misc]


def test_fake_cadwork_point_3d() -> None:
    point = FakeCadwork.point_3d(4.0, 5.0, 6.0)
    assert isinstance(point, FakePoint3d)
    assert (point.x, point.y, point.z) == (4.0, 5.0, 6.0)
