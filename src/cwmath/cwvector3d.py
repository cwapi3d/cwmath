__author__ = 'Brunner'
__date__ = '13.03.2024'

from dataclasses import dataclass

@dataclass
class CwVector3d:
    """Vector class for 3D vectors. """
    x: float
    y: float
    z: float

    def dot(self, other: 'CwVector3d') -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def magnitude(self) -> float:
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    
    def normalize(self) -> 'CwVector3d':
        return self / self.magnitude()
        
    def __add__(self, other: 'CwVector3d') -> 'CwVector3d':
        return CwVector3d(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other: 'CwVector3d') -> 'CwVector3d':
        return CwVector3d(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, scalar: float) -> 'CwVector3d':
        return CwVector3d(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def __truediv__(self, scalar: float) -> 'CwVector3d':
        return CwVector3d(self.x / scalar, self.y / scalar, self.z / scalar)
    
    def __neg__(self) -> 'CwVector3d':
        return CwVector3d(-self.x, -self.y, -self.z)
    
    def __eq__(self, other: 'CwVector3d') -> bool:
        return abs(self.x - other.x) < 1e-6 and abs(self.y - other.y) < 1e-6 and abs(self.z - other.z) < 1e-6
    
    def __ne__(self, other: 'CwVector3d') -> bool:
        return not self.__eq__(other)
    
    def __str__(self) -> str:
        return f'({self.x}, {self.y}, {self.z})'
    
    def __repr__(self) -> str:
        return f'CwVector({self.x}, {self.y}, {self.z})'
    
    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def __getitem__(self, index: int) -> float:
        return (self.x, self.y, self.z)[index]
    
    def __setitem__(self, index: int, value: float) -> None:
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        elif index == 2:
            self.z = value
        else:
            raise IndexError('Index out of range')

def point3d_to_vector3d(point: 'cadwork.point_3d') -> 'CwVector3d':
    return CwVector3d(point.x, point.y, point.z)