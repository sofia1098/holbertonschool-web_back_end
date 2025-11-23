#!/usr/bin/env python3
"""
This module provides utility functions for key-value pair operations.

It contains a type-annotated function called 'to_kv' that takes a string
and a numeric value (int or float) as arguments and returns a tuple.
The function demonstrates proper type annotations for Union types and
tuple operations in Python 3, following best practices for documentation
and type safety with multiple accepted types.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with a string key and the square of a numeric value.

    This function takes a string and a numeric value (either int or float)
    and returns a tuple where the first element is the string key and the
    second element is the square of the numeric value as a float. The
    squaring operation converts any integer input to float in the result,
    ensuring consistent return type annotation.

    Args:
        k: A string that will be the first element of the tuple.
        v: An integer or float value to be squared.

    Returns:
        A tuple containing the string k and the square of v as a float.

    Examples:
        >>> to_kv("eggs", 3)
        ('eggs', 9.0)
        >>> to_kv("school", 0.02)
        ('school', 0.0004)
        >>> to_kv("number", 5)
        ('number', 25.0)
    """
    return (k, float(v ** 2))
