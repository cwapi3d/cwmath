import unittest
from cwmath.cwplane3d import CwPlane3d
from cwmath.cwvector3d import CwVector3d

class TestCwPlane3d(unittest.TestCase):
    def test_call(self):
        plane = CwPlane3d(1, 2, 3, 4)
        result = plane(1, 2, 3)
        self.assertEqual(result, 20)

    def test_str(self):
        plane = CwPlane3d(1, 2, 3, 4)
        result = str(plane)
        self.assertEqual(result, "1x + 2y + 3z + 4 = 0")

    def test_repr(self):
        plane = CwPlane3d(1, 2, 3, 4)
        result = repr(plane)
        self.assertEqual(result, "CwPlane3d(1, 2, 3, 4)")

    def test_eq(self):
        plane1 = CwPlane3d(1, 2, 3, 4)
        plane2 = CwPlane3d(1, 2, 3, 4)
        self.assertEqual(plane1, plane2)

    def test_ne(self):
        plane1 = CwPlane3d(1, 2, 3, 4)
        plane2 = CwPlane3d(5, 6, 7, 8)
        self.assertNotEqual(plane1, plane2)

    def test_iter(self):
        plane = CwPlane3d(1, 2, 3, 4)
        result = list(plane)
        self.assertEqual(result, [1, 2, 3, 4])

    def test_getitem(self):
        plane = CwPlane3d(1, 2, 3, 4)
        result = plane[2]
        self.assertEqual(result, 3)

    def test_setitem(self):
        plane = CwPlane3d(1, 2, 3, 4)
        plane[2] = 5
        self.assertEqual(plane[2], 5)

    def test_is_parallel(self):
        plane1 = CwPlane3d(1, 2, 3, 4)
        plane2 = CwPlane3d(2, 4, 6, 8)
        self.assertTrue(plane1.is_parallel(plane2))

    def test_is_perpendicular(self):
        plane1 = CwPlane3d(1, 0, 0, 0)
        plane2 = CwPlane3d(0, 1, 0, 0)
        self.assertTrue(plane1.is_perpendicular(plane2))

    def test_is_coplanar(self):
        plane1 = CwPlane3d(1, 2, 3, 4)
        plane2 = CwPlane3d(2, 4, 6, 8)
        self.assertTrue(plane1.is_coplanar(plane2))

    def test_is_point_on_plane(self):
        plane = CwPlane3d(1, 2, 3, 4)
        point = CwVector3d(1, 2, 3)
        self.assertTrue(plane.is_point_on_plane(point))

    def test_distance_to_point(self):
        plane = CwPlane3d(1, 2, 3, 4)
        point = CwVector3d(1, 2, 3)
        result = plane.distance_to_point(point)
        self.assertAlmostEqual(result, 0.0)

    def test_distance_to_plane(self):
        plane1 = CwPlane3d(1, 2, 3, 4)
        plane2 = CwPlane3d(2, 4, 6, 8)
        result = plane1.distance_to_plane(plane2)
        self.assertAlmostEqual(result, 0.0)

    def test_intersection(self):
        plane1 = CwPlane3d(1, 2, 3, 4)
        plane2 = CwPlane3d(2, 4, 6, 8)
        result = plane1.intersection(plane2)
        self.assertEqual(result, CwVector3d(-2, 4, -2))

if __name__ == '__main__':
    unittest.main()