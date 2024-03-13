__author__ = 'Brunner'
__date__ = '13.03.2024'

from math import sqrt
from cwmath import cwvector3d


class CwPlane3d:
    """Plane class for 3D planes. """

    def __init__(self, point_3d, normal_vector):
        self._coefficient_a = normal_vector.x
        self._coefficient_b = normal_vector.y
        self._coefficient_c = normal_vector.z
        self._constant_d = -(self._coefficient_a * point_3d.x + self._coefficient_b * point_3d.y + self._coefficient_c * point_3d.z)   

    @property
    def coefficient_a(self) -> float:
        return self._coefficient_a
    
    @coefficient_a.setter
    def coefficient_a(self, value: float) -> None:
        self._coefficient_a = value

    @property
    def coefficient_b(self) -> float:
        return self._coefficient_b
    
    @coefficient_b.setter
    def coefficient_b(self, value: float) -> None:
        self._coefficient_b = value

    @property
    def coefficient_c(self) -> float:
        return self._coefficient_c
    
    @coefficient_c.setter
    def coefficient_c(self, value: float) -> None:
        self._coefficient_c = value

    @property
    def constant_d(self) -> float:
        return self._constant_d
    
    @constant_d.setter
    def constant_d(self, value: float) -> None:
        self._constant_d = value

    def __call__(self, x: float, y: float, z: float) -> float:
        """ Calculate the value of the plane at a given point.

        Args:
            x: x-coordinate of the point
            y: y-coordinate of the point
            z: z-coordinate of the point


        Returns:
            float: value of the plane at the given point
        """
        return self._coefficient_a * x + self._coefficient_b * y + self._coefficient_c * z + self._constant_d

    def __str__(self) -> str:
        return f'{self._coefficient_a}x + {self._coefficient_b}y + {self._coefficient_c}z + {self._constant_d} = 0'

    def __repr__(self) -> str:
        return f'CwPlane3d({self._coefficient_a}, {self._coefficient_b}, {self._coefficient_c}, {self._constant_d})'

    def __eq__(self, other: 'CwPlane3d') -> bool:
        return abs(self._coefficient_a - other._coefficient_a) < 1e-6 and abs(
            self._coefficient_b - other._coefficient_b) < 1e-6 and abs(
            self._coefficient_c - other._coefficient_c) < 1e-6 and abs(
            self._constant_d - other._constant_d) < 1e-6

    def __ne__(self, other: 'CwPlane3d') -> bool:
        return not self.__eq__(other)

    def __iter__(self):
        yield self._coefficient_a
        yield self._coefficient_b
        yield self._coefficient_c
        yield self._constant_d

    def __getitem__(self, index: int) -> float:
        return (self._coefficient_a, self._coefficient_b, self._coefficient_c, self._constant_d)[index]

    def __setitem__(self, index: int, value: float) -> None:
        if index == 0:
            self._coefficient_a = value
        elif index == 1:
            self._coefficient_b = value
        elif index == 2:
            self._coefficient_c = value
        elif index == 3:
            self._constant_d = value

    def is_parallel(self, other: 'CwPlane3d') -> bool:
        """ Checks if two planes are parallel.

        Args:
            other: 3d plane

        Returns:
            if the planes are parallel
        """
        return abs(self._coefficient_a * other._coefficient_b - self._coefficient_b * other._coefficient_a) < 1e-6 and abs(
            self._coefficient_a * other._coefficient_c - self._coefficient_c * other._coefficient_a) < 1e-6 and abs(
            self._coefficient_b * other._coefficient_c - self._coefficient_c * other._coefficient_b) < 1e-6

    def is_perpendicular(self, other: 'CwPlane3d') -> bool:
        """ Checks if two planes are perpendicular.

        Args:
            other: 3d plane

        Returns:
            if the planes are perpendicular
        """
        return abs(
            self._coefficient_a * other._coefficient_a + self._coefficient_b * other._coefficient_b + self._coefficient_c * other._coefficient_c) < 1e-6

    def is_coplanar(self, other: 'CwPlane3d') -> bool:
        """ Checks if two planes are coplanar.

        Args:
            other: 3d plane

        Returns:
            if the planes are coplanar
        """
        if other._coefficient_a == 0:
            return self._coefficient_a == 0
        if other._coefficient_b == 0:
            return self._coefficient_b == 0
        if other._coefficient_c == 0:
            return self._coefficient_c == 0

        return self._coefficient_a / other._coefficient_a \
                == self._coefficient_b / other._coefficient_b \
                == self._coefficient_c / other._coefficient_c

    def is_point_on_plane(self, point: 'cwvector3d.CwVector3d') -> bool:
        """ Checks if a point is on the plane.

        Args:
            point: point

        Returns:
            if the point is on the plane
        """
        return abs(
            self._coefficient_a * point.x + self._coefficient_b * point.y + self._coefficient_c * point.z + self._constant_d) < 1e-6

    def distance_to_point(self, point: 'cwvector3d.CwVector3d') -> float:
        """ Calculates the distance from a point to the plane.
        The distance from a point to a plane is given by the formula:
        |ax + by + cz + d| / sqrt(a^2 + b^2 + c^2)
        where (a, b, c) is the normal vector of the plane,
        (x, y, z) are the coordinates of the point, and
        d is the constant term in the plane equation.

        Args:
            point: point

        Returns:
            distance from the point to the plane
        """
        numerator = abs(self._coefficient_a * point.x + self._coefficient_b * point.y + self._coefficient_c * point.z + self._constant_d)
        denominator = sqrt(self._coefficient_a**2 + self._coefficient_b**2 + self._coefficient_c**2)
        return numerator / denominator

    def distance_to_plane(self, other: 'CwPlane3d') -> float:
        """ Calculates the distance from a plane to another plane.

        Args:
            other: 3d plane

        Returns:
            distance to plane
        """
        return abs(self._constant_d - other._constant_d) / sqrt(
            self._coefficient_a ** 2 + self._coefficient_b ** 2 + self._coefficient_c ** 2)
