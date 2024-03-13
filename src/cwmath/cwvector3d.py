__author__ = 'Brunner'
__date__ = '13.03.2024'


class CwVector3d:
    """Vector class for 3D vectors."""

    def __init__(self, x: float, y: float, z: float):
        self._x = x
        self._y = y
        self._z = z

    @classmethod
    def from_point_3d(cls, point_3d: 'cadwork.point_3d') -> 'CwVector3d':
        """Create a CwVector3d from a cadwork.point_3d.

        Args:
            point_3d: 3d point

        Returns:
            vector
        """
        return cls(point_3d.x, point_3d.y, point_3d.z)

    @property
    def x(self) -> float:
        return self._x
    
    @x.setter
    def x(self, value: float) -> None:
        self._x = value
    
    @property
    def y(self) -> float:
        return self._y
    
    @y.setter
    def y(self, value: float) -> None:
        self._y = value

    @property
    def z(self) -> float:
        return self._z
    
    @z.setter
    def z(self, value: float) -> None:
        self._z = value

    def dot(self, other: 'CwVector3d') -> float:
        """ Calculates the dot product of two vectors.

        Args:
            other: vector

        Returns:
            dot product
        """
        return self._x * other._x + self._y * other._y + self._z * other._z
    
    def magnitude(self) -> float:
        """ Calculates the magnitude of the vector.

        Returns:
            magnitude
        """
        return (self._x**2 + self._y**2 + self._z**2)**0.5
    
    def normalize(self) -> 'CwVector3d':
        """ Normalizes the vector.

        Returns:
            normalized vector
        """
        return self / self.magnitude()
        
    def __add__(self, other: 'CwVector3d') -> 'CwVector3d':
        return CwVector3d(self._x + other._x, self._y + other._y, self._z + other._z)
    
    def __sub__(self, other: 'CwVector3d') -> 'CwVector3d':
        return CwVector3d(self._x - other._x, self._y - other._y, self._z - other._z)
    
    def __mul__(self, scalar: float) -> 'CwVector3d':
        return CwVector3d(self._x * scalar, self._y * scalar, self._z * scalar)
    
    def __truediv__(self, scalar: float) -> 'CwVector3d':
        return CwVector3d(self._x / scalar, self._y / scalar, self._z / scalar)
    
    def __neg__(self) -> 'CwVector3d':
        return CwVector3d(-self._x, -self._y, -self._z)
    
    def __eq__(self, other: 'CwVector3d') -> bool:
        return abs(self._x - other._x) < 1e-6 and abs(self._y - other._y) < 1e-6 and abs(self._z - other._z) < 1e-6
    
    def __ne__(self, other: 'CwVector3d') -> bool:
        return not self.__eq__(other)
    
    def __str__(self) -> str:
        return f'({self._x}, {self._y}, {self._z})'
    
    def __repr__(self) -> str:
        return f'CwVector({self._x}, {self._y}, {self._z})'
    
    def __iter__(self):
        yield self._x
        yield self._y
        yield self._z

    def __getitem__(self, index: int) -> float:
        return (self._x, self._y, self._z)[index]
    
    def __setitem__(self, index: int, value: float) -> None:
        if index == 0:
            self._x = value
        elif index == 1:
            self._y = value
        elif index == 2:
            self._z = value
        else:
            raise IndexError('Index out of range')
