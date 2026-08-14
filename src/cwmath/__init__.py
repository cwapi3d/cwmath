"""Cadwork Math Utilities — frozen geometry types for plugin authors."""

from cwmath.cadwork import to_point_3d
from cwmath.frame3 import Frame3
from cwmath.line3 import Line3, project_point_on_line
from cwmath.plane3 import Plane3, project_point_on_plane
from cwmath.point2 import Point2
from cwmath.point3 import Point3
from cwmath.tolerance import ABS_TOL, REL_TOL, is_close
from cwmath.vec2 import Vec2
from cwmath.vec3 import Vec3

__all__ = [
    'ABS_TOL',
    'REL_TOL',
    'Frame3',
    'Line3',
    'Plane3',
    'Point2',
    'Point3',
    'Vec2',
    'Vec3',
    'is_close',
    'project_point_on_line',
    'project_point_on_plane',
    'to_point_3d',
]
