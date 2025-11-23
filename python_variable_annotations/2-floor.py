#!/usr/bin/env python3
"""
This module provides type conversion operations for numeric types.

It contains a type-annotated function called 'to_str' that takes a float
argument and returns its string representation. This conversion is useful
for displaying numeric values as text or for string manipulation operations.
The function demonstrates proper type annotations in Python 3 and follows
best practices for documentation and type conversion operations.
"""


def to_str(n: float) -> str:
    """
    Convert a floating-point number to its string representation.

    This function takes a floating-point number and returns a string
    that represents the numeric value as text. The conversion preserves
    the decimal representation of the number, making it suitable for
    display purposes, logging, or any operation that requires string
    manipulation of numeric values. The function is properly type-annotated
    to ensure type safety and clear documentation.

    Args:
        n: The floating-point number to convert to a string.

    Returns:
        A string representation of the float value n.

    Examples:
        >>> to_str(3.14)
        '3.14'
        >>> to_str(10.0)
        '10.0'
        >>> to_str(-5.5)
        '-5.5'
        >>> to_str(0.0)
        '0.0'
    """
    return str(n)
