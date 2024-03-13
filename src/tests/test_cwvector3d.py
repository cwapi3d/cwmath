import unittest

from cwmath import cwvector3d


class TestCwVector3d(unittest.TestCase):
    def setUp(self):
        self.vector1 = cwvector3d.CwVector3d(1, 2, 3)
        self.vector2 = cwvector3d.CwVector3d(4, 5, 6)

    def test_dot_product(self):
        result = self.vector1.dot(self.vector2)
        self.assertEqual(result, 32)

    def test_magnitude(self):
        result = self.vector1.magnitude()
        self.assertAlmostEqual(result, 3.7416573867739413)

    def test_normalization(self):
        result = self.vector1.normalize()
        self.assertEqual(result, cwvector3d.CwVector3d(0.2672612419124244, 0.5345224838248488, 0.8017837257372732))

    def test_normalization_magnitude(self):
        result = self.vector1.normalize().magnitude()
        self.assertAlmostEqual(result, 1.0)

    def test_normalization_direction(self):
        start_pt = cwvector3d.CwVector3d(0, 0, 100)
        end_pt = cwvector3d.CwVector3d(0, 0, 0)
        result = (end_pt - start_pt).normalize()
        self.assertEqual(result, cwvector3d.CwVector3d(0, 0, -1))

    def test_addition(self):
        result = self.vector1 + self.vector2
        self.assertEqual(result, cwvector3d.CwVector3d(5, 7, 9))

    def test_subtraction(self):
        result = self.vector1 - self.vector2
        self.assertEqual(result, cwvector3d.CwVector3d(-3, -3, -3))

    def test_scalar_multiplication(self):
        result = self.vector1 * 2
        self.assertEqual(result, cwvector3d.CwVector3d(2, 4, 6))

    def test_scalar_division(self):
        result = self.vector1 / 2
        self.assertEqual(result, cwvector3d.CwVector3d(0.5, 1, 1.5))

    def test_negation(self):
        result = -self.vector1
        self.assertEqual(result, cwvector3d.CwVector3d(-1, -2, -3))

    def test_equality(self):
        self.assertEqual(self.vector1, cwvector3d.CwVector3d(1, 2, 3))
        self.assertNotEqual(self.vector1, self.vector2)

    def test_string_representation(self):
        result = str(self.vector1)
        self.assertEqual(result, "(1, 2, 3)")

    def test_indexing(self):
        self.assertEqual(self.vector1[0], 1)
        self.assertEqual(self.vector1[1], 2)
        self.assertEqual(self.vector1[2], 3)
        with self.assertRaises(IndexError):
            self.vector1[3] = 4


if __name__ == '__main__':
    unittest.main()
