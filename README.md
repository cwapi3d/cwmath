# Cadwork Math Utilities

![Logo](https://filehost.cadwork.ca/cadwork_logo.png)

[![PyPI](https://img.shields.io/pypi/v/cwmath)](https://pypi.python.org/pypi/cwmath/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cwmath)](https://pypi.python.org/pypi/cwmath/)
[![RTD](https://img.shields.io/readthedocs/cwmath)](https://docs.cadwork.com/projects/cwmath/en/latest/)
[![Issues](https://img.shields.io/github/issues/cwapi3d/cwmath)](https://github.com/cwapi3d/cwmath/issues)
[![Pulls](https://img.shields.io/github/issues-pr/cwapi3d/cwmath)](https://github.com/cwapi3d/cwmath/pulls)
[![GitHub](https://img.shields.io/github/license/cwapi3d/cwmath)](https://choosealicense.com/licenses/mit/)

This is the Cadwork Math Utilities library in Python.

## Installation

Install with pip:

```bash
  pip install cwmath
```
    
## Contributing

Contributions are always welcome!
Before contributing, please check our [contributing agreement](CONTRIBUTING.md).
  
## Roadmap

- Guides
- Examples
- API Documentation
  
## Authors

- [@jspaquet](https://github.com/jspaquet)
- [@Brunner246](https://github.com/Brunner246)
  
## License

[MIT](https://choosealicense.com/licenses/mit/)

# Style Guide

Please follow the style guide below when adding functions.
[Guidelines](GUIDELINES.md)

```python

# imports:
import math
import sys
from myclass import MyClass


# example function
def add_one(number: int) -> int:
    """Increase number by one.
    
    Function written by John Doe.

    Args:
        number: a number

    Returns:
        number increased by one
    """
    return number + 1


# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

if foo == 'blah':
    do_blah_thing()
do_one()
do_two()
do_three()

```

# Examples
```python
import cadwork
import element_controller as ec
import geometry_controller as gc

import sys

sys.path.append("...\\...\cwmath\\src")

from cwmath import cwplane3d
from cwmath import cwvector3d

element_ids = ec.get_active_identifiable_element_ids()
if len(element_ids) > 0:
    point1 = gc.get_p1(*element_ids)
    point2 = gc.get_p2(*element_ids)
    yl = gc.get_yl(*element_ids)
    plane = cwplane3d.CwPlane3d(point1,yl)
    print(point1)
    print(yl)
    print(plane)

    distance = plane.distance_to_point(cadwork.point_3d(0.,0.,0.))
    print(distance)

    vector1 = cwvector3d.CwVector3d.from_point_3d(point1)
    vector2 = cwvector3d.CwVector3d.from_point_3d(point2)
    norm =(vector2 - vector1).normalize()
    print(norm)
```
