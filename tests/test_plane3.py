from __future__ import annotations

import pytest

from cwmath.plane3 import Plane3, project_point_on_plane
from cwmath.point3 import Point3
from cwmath.vec3 import Vec3


def test_plane3_construct_from_point_normal_stores_unit_normal() -> None:
    plane = Plane3.from_point_normal(Point3(1, 2, 3), Vec3(0, 0, 2))
    assert plane.point == Point3(1, 2, 3)
    assert plane.normal.is_close(Vec3(0, 0, 1))
    assert plane.normal.magnitude() == pytest.approx(1.0)


def test_plane3_construct_zero_normal_raises() -> None:
    with pytest.raises(ValueError):
        Plane3.from_point_normal(Point3(0, 0, 0), Vec3(0, 0, 0))


def test_plane3_distance_axis_aligned() -> None:
    plane = Plane3.from_point_normal(Point3(0, 0, 0), Vec3(0, 0, 1))
    above = Point3(0, 0, 5)
    below = Point3(0, 0, -3)
    assert plane.signed_distance(above) == 5.0
    assert plane.distance(above) == 5.0
    assert plane.signed_distance(below) == -3.0
    assert plane.distance(below) == 3.0


def test_plane3_contains_constructing_point() -> None:
    origin = Point3(1, 2, 3)
    plane = Plane3.from_point_normal(origin, Vec3(0, 0, 1))
    assert plane.contains(origin) is True
    assert plane.contains(Point3(4, 5, 3)) is True
    assert plane.contains(Point3(1, 2, 4)) is False


def test_plane3_project_onto_xy() -> None:
    plane = Plane3.from_point_normal(Point3(0, 0, 0), Vec3(0, 0, 1))
    foot = plane.project(Point3(0, 0, 5))
    assert foot.is_close(Point3(0, 0, 0))
    assert plane.contains(foot)


def test_plane3_project_stable_when_already_on_plane() -> None:
    plane = Plane3.from_point_normal(Point3(0, 0, 0), Vec3(0, 0, 1))
    on_plane = Point3(4, 5, 0)
    assert plane.project(on_plane).is_close(on_plane)
    assert plane.project(plane.point).is_close(plane.point)


def test_project_point_on_plane_matches_method() -> None:
    plane = Plane3.from_point_normal(Point3(0, 0, 0), Vec3(0, 0, 1))
    point = Point3(1, 2, 5)
    assert project_point_on_plane(point, plane) == plane.project(point)
