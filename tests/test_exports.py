from __future__ import annotations

import importlib.metadata

import cwmath

EXPECTED_EXPORTS = {
    "ABS_TOL",
    "REL_TOL",
    "Frame3",
    "Line3",
    "Plane3",
    "Point2",
    "Point3",
    "Vec2",
    "Vec3",
    "is_close",
    "project_point_on_line",
    "project_point_on_plane",
    "to_point_3d",
}

LEGACY_NAMES = ("CwVector3d", "CwPlane3d", "cwexamples")


def test_top_level_import_list() -> None:
    from cwmath import (
        ABS_TOL,
        REL_TOL,
        Frame3,
        Line3,
        Plane3,
        Point2,
        Point3,
        Vec2,
        Vec3,
        is_close,
        project_point_on_line,
        project_point_on_plane,
        to_point_3d,
    )

    assert Point3 is cwmath.Point3
    assert Vec3 is cwmath.Vec3
    assert Point2 is cwmath.Point2
    assert Vec2 is cwmath.Vec2
    assert Frame3 is cwmath.Frame3
    assert Plane3 is cwmath.Plane3
    assert Line3 is cwmath.Line3
    assert to_point_3d is cwmath.to_point_3d
    assert project_point_on_line is cwmath.project_point_on_line
    assert project_point_on_plane is cwmath.project_point_on_plane
    assert is_close is cwmath.is_close
    assert ABS_TOL is cwmath.ABS_TOL
    assert REL_TOL is cwmath.REL_TOL
    assert set(cwmath.__all__) == EXPECTED_EXPORTS


def test_no_legacy_names_or_version() -> None:
    for name in LEGACY_NAMES:
        assert not hasattr(cwmath, name)
        assert name not in cwmath.__all__
    assert importlib.metadata.version("cwmath") == "1.0.1"
