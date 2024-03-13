__author__ = 'Brunner'
__date__ = '13.03.2024'

from dataclasses import dataclass
from math import sqrt
from cwmath import cwvector3d


@dataclass
class CwPlane3d:
    """Plane class for 3D planes. """
    coefficient_a: float
    coefficient_b: float
    coefficient_c: float
    constant_d: float

    def __call__(self, x: float, y: float, z: float) -> float:
        """ Calculate the value of the plane at a given point.

        Args:
            x: x-coordinate of the point
            y: y-coordinate of the point
            z: z-coordinate of the point


        Returns:
            float: value of the plane at the given point
        """
        return self.coefficient_a * x + self.coefficient_b * y + self.coefficient_c * z + self.constant_d

    def __str__(self) -> str:
        return f'{self.coefficient_a}x + {self.coefficient_b}y + {self.coefficient_c}z + {self.constant_d} = 0'

    def __repr__(self) -> str:
        return f'CwPlane3d({self.coefficient_a}, {self.coefficient_b}, {self.coefficient_c}, {self.constant_d})'

    def __eq__(self, other: 'CwPlane3d') -> bool:
        return abs(self.coefficient_a - other.coefficient_a) < 1e-6 and abs(
            self.coefficient_b - other.coefficient_b) < 1e-6 and abs(
            self.coefficient_c - other.coefficient_c) < 1e-6 and abs(
            self.constant_d - other.constant_d) < 1e-6

    def __ne__(self, other: 'CwPlane3d') -> bool:
        return not self.__eq__(other)

    def __iter__(self):
        yield self.coefficient_a
        yield self.coefficient_b
        yield self.coefficient_c
        yield self.constant_d

    def __getitem__(self, index: int) -> float:
        return (self.coefficient_a, self.coefficient_b, self.coefficient_c, self.constant_d)[index]

    def __setitem__(self, index: int, value: float) -> None:
        if index == 0:
            self.coefficient_a = value
        elif index == 1:
            self.coefficient_b = value
        elif index == 2:
            self.coefficient_c = value
        elif index == 3:
            self.constant_d = value

    def is_parallel(self, other: 'CwPlane3d') -> bool:
        """ Check if two planes are parallel.

        Args:
            Another plane in 3D space

        Returns:
            True if the planes are parallel, False otherwise
        """
        return abs(self.coefficient_a * other.coefficient_b - self.coefficient_b * other.coefficient_a) < 1e-6 and abs(
            self.coefficient_a * other.coefficient_c - self.coefficient_c * other.coefficient_a) < 1e-6 and abs(
            self.coefficient_b * other.coefficient_c - self.coefficient_c * other.coefficient_b) < 1e-6

    def is_perpendicular(self, other: 'CwPlane3d') -> bool:
        """ Check if two planes are perpendicular.

        Args:
            Another plane in 3D space

        Returns:
            True if the planes are perpendicular, False otherwise
        """
        return abs(
            self.coefficient_a * other.coefficient_a + self.coefficient_b * other.coefficient_b + self.coefficient_c * other.coefficient_c) < 1e-6

    def is_coplanar(self, other: 'CwPlane3d') -> bool:
        """ Check if two planes are coplanar.

        Args:
            Another plane in 3D space

        Returns:
            True if the planes are coplanar, False otherwise
        """
        return self.coefficient_a / other.coefficient_a \
                == self.coefficient_b / other.coefficient_b \
                == self.coefficient_c / other.coefficient_c

    def is_point_on_plane(self, point: 'cwvector3d.CwVector3d') -> bool:
        """ Check if a point is on the plane.

        Args:
            a point in 3D space

        Returns:
            True if the point is on the plane, False otherwise
        """
        return abs(
            self.coefficient_a * point.x + self.coefficient_b * point.y + self.coefficient_c * point.z + self.constant_d) < 1e-6

    def distance_to_point(self, point: 'cwvector3d.CwVector3d') -> float:
        """ Calculate the distance from a point to the plane.
        The distance from a point to a plane is given by the formula:
        |ax + by + cz + d| / sqrt(a^2 + b^2 + c^2)
        where (a, b, c) is the normal vector of the plane,
        (x, y, z) are the coordinates of the point, and
        d is the constant term in the plane equation.

        Args:
            a point in 3D space

        Returns:
            distance from the point to the plane
        """
        numerator = abs(self.coefficient_a * point.x + self.coefficient_b * point.y + self.coefficient_c * point.z + self.constant_d)
        denominator = sqrt(self.coefficient_a**2 + self.coefficient_b**2 + self.coefficient_c**2)
        return numerator / denominator

    def distance_to_plane(self, other: 'CwPlane3d') -> float:
        """ Calculate the distance from a plane to another plane.

        Args:
            another plane in 3D space

        Returns:
            distance from the plane to the other plane
        """
        return abs(self.constant_d - other.constant_d) / sqrt(
            self.coefficient_a ** 2 + self.coefficient_b ** 2 + self.coefficient_c ** 2)
