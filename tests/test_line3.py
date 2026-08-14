from __future__ import annotations

import pytest

from cwmath.line3 import Line3, project_point_on_line
from cwmath.point3 import Point3
from cwmath.vec3 import Vec3


def test_line3_construct_from_origin_direction_stores_unit_direction() -> None:
    line = Line3.from_origin_direction(Point3(1, 2, 3), Vec3(2, 0, 0))
    assert line.origin == Point3(1, 2, 3)
    assert line.direction.is_close(Vec3(1, 0, 0))
    assert line.direction.magnitude() == pytest.approx(1.0)


def test_line3_construct_zero_direction_raises() -> None:
    with pytest.raises(ValueError):
        Line3.from_origin_direction(Point3(0, 0, 0), Vec3(0, 0, 0))


def test_line3_construct_from_points() -> None:
    line = Line3.from_points(Point3(0, 0, 0), Point3(0, 4, 0))
    assert line.origin == Point3(0, 0, 0)
    assert line.direction.is_close(Vec3(0, 1, 0))


def test_line3_construct_from_points_coincident_raises() -> None:
    with pytest.raises(ValueError):
        Line3.from_points(Point3(1, 2, 3), Point3(1, 2, 3))


def test_line3_project_onto_x_axis() -> None:
    line = Line3.from_origin_direction(Point3(0, 0, 0), Vec3(1, 0, 0))
    foot = line.project(Point3(1, 1, 0))
    assert foot.is_close(Point3(1, 0, 0))
    assert line.parameter(Point3(1, 1, 0)) == pytest.approx(1.0)


def test_line3_project_stable_when_already_on_line() -> None:
    line = Line3.from_origin_direction(Point3(0, 0, 0), Vec3(1, 0, 0))
    on_line = Point3(3, 0, 0)
    assert line.project(on_line).is_close(on_line)
    assert line.project(line.origin).is_close(line.origin)


def test_project_point_on_line_matches_method() -> None:
    line = Line3.from_origin_direction(Point3(0, 0, 0), Vec3(1, 0, 0))
    point = Point3(1, 1, 0)
    assert project_point_on_line(point, line) == line.project(point)
