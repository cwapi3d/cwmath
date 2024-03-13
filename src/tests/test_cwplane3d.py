import unittest

from cwmath import cwvector3d
from cwmath import cwplane3d


class TestCwPlane3d(unittest.TestCase):

    def setUp(self):
        self.plane = cwplane3d.CwPlane3d(cwvector3d.CwVector3d(-42.500000, 47.500000, 2480.000000), cwvector3d.CwVector3d(0.000000, 0.000000, -1.000000))

    def test_call(self):
        result = self.plane(-42.500000, 47.500000, 0.000000)
        self.assertEqual(result, 2480.0)

    def test_str(self):
        result = str(self.plane)
        self.assertEqual(result, "0.0x + 0.0y + -1.0z + 2480.0 = 0")

    def test_repr(self):
        result = repr(self.plane)
        self.assertEqual(result, "CwPlane3d(0.0, 0.0, -1.0, 2480.0)")

    def test_eq(self):
        plane2 = cwplane3d.CwPlane3d(cwvector3d.CwVector3d(-42.500000, 47.500000, 2480.000000), cwvector3d.CwVector3d(0.000000, 0.000000, -1.000000))
        self.assertEqual(self.plane, plane2)

    def test_ne(self):
        plane2 = cwplane3d.CwPlane3d(cwvector3d.CwVector3d(-42.500000, 47.500000, 2480.000000), cwvector3d.CwVector3d(1.000000, 0.000000, -1.000000))
        self.assertNotEqual(self.plane, plane2)

    def test_iter(self):
        result = list(self.plane)
        self.assertEqual(result, [0.0, 0.0, -1.0, 2480.0])

    def test_getitem(self):
        result = self.plane[2]
        self.assertEqual(result, -1.0)

    def test_setitem(self):
        self.plane[2] = -2.0
        self.assertEqual(self.plane[2], -2.0)

    def test_is_parallel(self):
        plane2 = cwplane3d.CwPlane3d(cwvector3d.CwVector3d(-42.500000, 47.500000, 2480.000000), cwvector3d.CwVector3d(0.000000, 0.000000, -1.000000))
        self.assertTrue(self.plane.is_parallel(plane2))

    def test_is_perpendicular(self):
        plane2 = cwplane3d.CwPlane3d(cwvector3d.CwVector3d(-42.500000, 47.500000, 2480.000000), cwvector3d.CwVector3d(1.000000, 0.000000, 0.000000))
        self.assertTrue(self.plane.is_perpendicular(plane2))

    def test_is_coplanar(self):
        plane2 = cwplane3d.CwPlane3d(cwvector3d.CwVector3d(-42.500000, 47.500000, 280.000000), cwvector3d.CwVector3d(0.000000, 0.000000, -1.000000))
        self.assertTrue(self.plane.is_coplanar(plane2))

    def test_is_point_on_plane(self):
        point = cwvector3d.CwVector3d(-42.500000, 47.500000, 2480.000000)
        self.assertTrue(self.plane.is_point_on_plane(point))

    def test_distance_to_point(self):
        point = cwvector3d.CwVector3d(-42.500000, 47.500000, 0.000000)
        result = self.plane.distance_to_point(point)
        self.assertAlmostEqual(result, 2480.0)

    def test_distance_to_plane(self):
        plane2 = cwplane3d.CwPlane3d(cwvector3d.CwVector3d(-42.500000, 47.500000, 2480.000000), cwvector3d.CwVector3d(0.000000, 0.000000, -1.000000))
        result = self.plane.distance_to_plane(plane2)
        self.assertAlmostEqual(result, 0.0)

if __name__ == '__main__':
    unittest.main()
    