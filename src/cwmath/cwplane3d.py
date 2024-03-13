__author__ = 'Brunner'
__date__ = '13.03.2024'

from dataclasses import dataclass
from math import sqrt

from cwvector3d import CwVector3d

@dataclass
class CwPlane3d:
    """Plane class for 3D planes. """
    coefficient_a: float
    coefficient_b: float
    coefficient_c: float
    constant_d: float

    def __call__(self, x: float, y: float, z: float) -> float:
        return self.a * x + self.b * y + self.c * z + self.d

    def __str__(self) -> str:
        return f'{self.a}x + {self.b}y + {self.c}z + {self.d} = 0'

    def __repr__(self) -> str:
        return f'CwPlane3d({self.a}, {self.b}, {self.c}, {self.d})'
    
    def __eq__(self, other: 'CwPlane3d') -> bool:
        return abs(self.a - other.a) < 1e-6 and abs(self.b - other.b) < 1e-6 and abs(self.c - other.c) < 1e-6 and abs(self.d - other.d) < 1e-6
    
    def __ne__(self, other: 'CwPlane3d') -> bool:
        return not self.__eq__(other)
    
    def __iter__(self):
        yield self.a
        yield self.b
        yield self.c
        yield self.d

    def __getitem__(self, index: int) -> float:
        return (self.a, self.b, self.c, self.d)[index]
    
    def __setitem__(self, index: int, value: float) -> None:
        if index == 0:
            self.a = value
        elif index == 1:
            self.b = value
        elif index == 2:
            self.c = value
        elif index == 3:
            self.d = value
    
    def is_parallel(self, other: 'CwPlane3d') -> bool:
        """ Check if two planes are parallel.

        Args:
            Another plane in 3D space

        Returns:
            True if the planes are parallel, False otherwise
        """
        return abs(self.a * other.b - self.b * other.a) < 1e-6 and abs(self.a * other.c - self.c * other.a) < 1e-6 and abs(self.b * other.c - self.c * other.b) < 1e-6
    
    def is_perpendicular(self, other: 'CwPlane3d') -> bool:
        """ Check if two planes are perpendicular.

        Args:
            Another plane in 3D space

        Returns:
            True if the planes are perpendicular, False otherwise
        """
        return abs(self.a * other.a + self.b * other.b + self.c * other.c) < 1e-6
    
    def is_coplanar(self, other: 'CwPlane3d') -> bool:
        """ Check if two planes are coplanar.

        Args:
            Another plane in 3D space

        Returns:
            True if the planes are coplanar, False otherwise
        """
        return self.is_parallel(other) and self.is_perpendicular(other)
    
    def is_point_on_plane(self, point: 'CwVector3d') -> bool:
        """ Check if a point is on the plane.

        Args:
            a point in 3D space

        Returns:
            True if the point is on the plane, False otherwise
        """
        return abs(self.a * point.x + self.b * point.y + self.c * point.z + self.d) < 1e-6
    
    def distance_to_point(self, point: 'CwVector3d') -> float:
        """ Calculate the distance from a point to the plane.

        Args:
            a point in 3D space

        Returns:
            distance from the point to the plane
        """
        return abs(self.a * point.x + self.b * point.y + self.c * point.z + self.d) / sqrt(self.a**2 + self.b**2 + self.c**2)
    
    def distance_to_plane(self, other: 'CwPlane3d') -> float:
        """ Calculate the distance from a plane to another plane.

        Args:
            another plane in 3D space

        Returns:
            distance from the plane to the other plane
        """
        return abs(self.d - other.d) / sqrt(self.a**2 + self.b**2 + self.c**2)
    
    def intersection(self, other: 'CwPlane3d') -> 'CwVector3d':
        """ Calculate the intersection point of two planes.

        Args:
            another plane in 3D space

        Returns:
            intersection point of the two planes
        """
        return CwVector3d(self.b * other.c - self.c * other.b, self.c * other.a - self.a * other.c, self.a * other.b - self.b * other.a) / (self.a * other.b - self.b * other.a)
    