import pytest
from _pytest.python_api import approx

from cwmath import cwvector3d
from cwmath import cwplane3d


@pytest.fixture
def plane_1():
    vector_1 = cwvector3d.CwVector3d(-42.500000, 47.500000, 2480.000000)
    vector_2 = cwvector3d.CwVector3d(0.000000, 0.000000, -1.000000)
    return cwplane3d.CwPlane3d(vector_1, vector_2)


def test_call(plane_1):
    result = plane_1(-42.500000, 47.500000, 0.000000)
    assert result == approx(2480.0)


def test_str(plane_1):
    result = str(plane_1)
    assert result == "0.0x + 0.0y + -1.0z + 2480.0 = 0"


def test_repr(plane_1):
    result = repr(plane_1)
    assert result == "CwPlane3d(0.0, 0.0, -1.0, 2480.0)"


def test_eq(plane_1):
    vector_1 = cwvector3d.CwVector3d(-42.500000, 47.500000, 2480.000000)
    vector_2 = cwvector3d.CwVector3d(0.000000, 0.000000, -1.000000)
    plane_2 = cwplane3d.CwPlane3d(vector_1, vector_2)
    assert plane_1 == plane_2


def test_ne(plane_1):
    plane_2 = cwplane3d.CwPlane3d(cwvector3d.CwVector3d(-42.500000, 47.500000, 2480.000000), cwvector3d.CwVector3d(1.000000, 0.000000, -1.000000))
    assert plane_1 != plane_2


def test_iter(plane_1):
    result = list(plane_1)
    assert result == [0.0, 0.0, -1.0, 2480.0]


def test_getitem(plane_1):
    result = plane_1[2]
    assert result == -1.0


def test_setitem(plane_1):
    plane_1[2] = -2.0
    assert plane_1[2] == -2.0


def test_is_parallel(plane_1):
    plane_2 = cwplane3d.CwPlane3d(cwvector3d.CwVector3d(-42.500000, 47.500000, 2480.000000), cwvector3d.CwVector3d(0.000000, 0.000000, -1.000000))
    assert plane_1.is_parallel(plane_2)


def test_is_perpendicular(plane_1):
    plane_2 = cwplane3d.CwPlane3d(cwvector3d.CwVector3d(-42.500000, 47.500000, 2480.000000), cwvector3d.CwVector3d(1.000000, 0.000000, 0.000000))
    assert plane_1.is_perpendicular(plane_2)


def test_is_coplanar(plane_1):
    plane_2 = cwplane3d.CwPlane3d(cwvector3d.CwVector3d(-42.500000, 47.500000, 280.000000), cwvector3d.CwVector3d(0.000000, 0.000000, -1.000000))
    assert plane_1.is_coplanar(plane_2)


def test_is_point_on_plane(plane_1):
    point = cwvector3d.CwVector3d(-42.500000, 47.500000, 2480.000000)
    assert plane_1.is_point_on_plane(point)


def test_distance_to_point(plane_1):
    point = cwvector3d.CwVector3d(-42.500000, 47.500000, 0.000000)
    result = plane_1.distance_to_point(point)
    assert result == approx(2480.0)


def test_distance_to_plane(plane_1):
    plane2 = cwplane3d.CwPlane3d(cwvector3d.CwVector3d(-42.500000, 47.500000, 2480.000000), cwvector3d.CwVector3d(0.000000, 0.000000, -1.000000))
    result = plane_1.distance_to_plane(plane2)
    assert result == approx(0.0)
