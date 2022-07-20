# Cadwork Math Utilities

[![PyPI](https://img.shields.io/pypi/v/cwmath)](https://pypi.python.org/pypi/cwmath/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cwmath)](https://pypi.python.org/pypi/cwmath/)
[![RTD](https://img.shields.io/readthedocs/cwmath)](https://math.cadwork.dev)
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
Before contributing, please check [contributing agreement](CONTRIBUTING.md).
  
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
def add_one(number:int) -> int:
    """Increase number by one.
    Function written by John Doe.

    Args:
        number (int): a number

    Returns:
        int: number increased by one
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
