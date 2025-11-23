#!/usr/bin/env python3
"""
This module provides arithmetic operations for floating-point numbers.

It contains a type-annotated function called 'add' that takes two float
arguments and returns their sum as a float. The function is designed to
demonstrate proper type annotations in Python 3 and follows best practices
for documentation and code style.
"""


def add(a: float, b: float) -> float:
    """
    Add two float numbers and return their sum.
    This function takes two floating-point numbers as arguments and
    returns their arithmetic sum as a float.

    Args:
        a: The first float number to add.
        b: The second float number to add.

    Returns:
        The sum of a and b as a float.

    Example:
        >>> add(3.5, 2.5)
        6.0
        >>> add(10.0, 5.0)
        15.0
    """
    return a + b
