# Cadwork Math Utilities

![Logo](https://filehost.cadwork.ca/cadwork_logo.png)

[![PyPI](https://img.shields.io/pypi/v/cwmath)](https://pypi.python.org/pypi/cwmath/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cwmath)](https://pypi.python.org/pypi/cwmath/)
[![RTD](https://img.shields.io/readthedocs/cwmath)](https://docs.cadwork.com/projects/cwmath/en/latest/)
[![Issues](https://img.shields.io/github/issues/cwapi3d/cwmath)](https://github.com/cwapi3d/cwmath/issues)
[![Pulls](https://img.shields.io/github/issues-pr/cwapi3d/cwmath)](https://github.com/cwapi3d/cwmath/pulls)
[![GitHub](https://img.shields.io/github/license/cwapi3d/cwmath)](https://choosealicense.com/licenses/mit/)
[![codecov](https://codecov.io/gh/cwapi3d/cwmath/graph/badge.svg?token=UU9QLGLMEQ)](https://codecov.io/gh/cwapi3d/cwmath)

Dependency-free geometry types for cadwork plugin authors. Frozen `Point` / `Vec`
pairs in 2D and 3D, a right-handed `Frame3`, `Plane3`, `Line3`, and projections.
Python 3.14, managed with UV. Millimetres are the implicit length unit.

## Installation

```bash
uv add cwmath
```

From a checkout:

```bash
uv sync --group dev
```

## Example

Copy this into a cadwork plugin (or cadwork IDLE). It converts a host
`point_3d`, builds a frame, drops a local point onto the XY plane, and
converts the foot back for `cwapi3d`.

```python
import cadwork
from cwmath import (
    Frame3,
    Plane3,
    Point3,
    Vec3,
    project_point_on_plane,
    to_point_3d,
)

origin = Point3.from_xyz(cadwork.point_3d(1000.0, 2000.0, 0.0))
x_dir = Vec3.from_xyz(cadwork.point_3d(1.0, 0.0, 0.0))
y_dir = Vec3.from_xyz(cadwork.point_3d(0.0, 1.0, 0.0))
frame = Frame3.from_origin_xy(origin, x_dir, y_dir)

local = Point3(50.0, 25.0, 10.0)
world = frame.to_world(local)
plane = Plane3.from_point_normal(origin, frame.z_axis)
foot = project_point_on_plane(world, plane)
result = to_point_3d(foot)
```

`to_point_3d` imports `cadwork` only at the call site. Unit tests inject a
duck-typed factory instead of the host.

## Contributing

Contributions are always welcome!
Before contributing, please check our [contributing agreement](CONTRIBUTING.md).

## Authors

- [@jspaquet](https://github.com/jspaquet)
- [@Brunner246](https://github.com/Brunner246)

## License

[MIT](https://choosealicense.com/licenses/mit/)
