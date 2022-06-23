# Coding Guidelines

# ToDo

Please follow the style guide below when adding functions. 

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

