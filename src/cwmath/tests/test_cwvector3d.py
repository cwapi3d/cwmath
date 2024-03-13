import pytest
from _pytest.python_api import approx

from cwmath import cwvector3d


@pytest.fixture
def vector_1():
    return cwvector3d.CwVector3d(1, 2, 3)


@pytest.fixture
def vector_2():
    return cwvector3d.CwVector3d(4, 5, 6)


def test_dot_product(vector_1, vector_2):
    result = vector_1.dot(vector_2)
    assert result == 32


def test_magnitude(vector_1):
    result = vector_1.magnitude()
    assert result == approx(3.7416573867739413)


def test_normalization(vector_1):
    result = vector_1.normalize()
    assert result == cwvector3d.CwVector3d(0.2672612419124244, 0.5345224838248488, 0.8017837257372732)


def test_normalization_magnitude(vector_1):
    result = vector_1.normalize().magnitude()
    assert result == approx(1.0)


def test_normalization_direction():
    start_pt = cwvector3d.CwVector3d(0, 0, 100)
    end_pt = cwvector3d.CwVector3d(0, 0, 0)
    result = (end_pt - start_pt).normalize()
    assert result == cwvector3d.CwVector3d(0, 0, -1)


def test_addition(vector_1, vector_2):
    result = vector_1 + vector_2
    assert result == cwvector3d.CwVector3d(5, 7, 9)


def test_subtraction(vector_1, vector_2):
    result = vector_1 - vector_2
    assert result == cwvector3d.CwVector3d(-3, -3, -3)


def test_scalar_multiplication(vector_1):
    result = vector_1 * 2
    assert result == cwvector3d.CwVector3d(2, 4, 6)


def test_scalar_division(vector_1):
    result = vector_1 / 2
    assert result == cwvector3d.CwVector3d(0.5, 1, 1.5)


def test_negation(vector_1):
    result = -vector_1
    assert result == cwvector3d.CwVector3d(-1, -2, -3)


def test_equality(vector_1, vector_2):
    assert vector_1 == cwvector3d.CwVector3d(1, 2, 3)
    assert vector_1 != vector_2


def test_string_representation(vector_1):
    result = str(vector_1)
    assert result, "(1, 2, 3)"


def test_indexing(vector_1):
    assert vector_1[0] == 1
    assert vector_1[1] == 2
    assert vector_1[2] == 3
    with pytest.raises(IndexError):
        vector_1[3] = 4
