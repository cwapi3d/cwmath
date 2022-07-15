import cadwork
from math import (acos, pi,)

# example codestyle
def add_one(number:int) -> int:
    """Increase number by one.

    Examples:
        >>> add_one(5)
        6.0
        >>> add_one(6)
        7.0
        
    Args:
        number (int): a number

    Returns:
        int: number increased by one
    """
    return number + 1

def angle_between_vectors(v1:cadwork.point_3d, v2:cadwork.point_3d) -> float:
    """Get angle between two vectors. 

    Examples:
        >>> v1 = cadwork.point_3d(1., 0., 0.)
        >>> v2 = cadwork.point_3d(0., 1., 0.)
        >>> angle_between_vectors(v1, v2)
        90.0
       
    Args:
        v1 (cadwork.point_3d): a first vector 
        v2 (cadwork.point_3d): a second vector

    Returns:
        float: angle in degrees
    """
    return acos(v1.dot(v2) / (v1.magnitude() * v2.magnitude())) * (180 /pi)

