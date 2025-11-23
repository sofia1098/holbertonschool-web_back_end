#!/usr/bin/env python3
"""
This module provides mathematical operations for floating-point numbers.

It contains a type-annotated function called 'floor' that takes a float
argument and returns the floor value as an integer. The floor operation
returns the largest integer less than or equal to the given number.
The function demonstrates proper type annotations in Python 3 and follows
best practices for documentation and mathematical operations.
"""
import math


def floor(n: float) -> int:
    """
    Return the floor of a floating-point number as an integer.

    This function takes a floating-point number and returns the largest
    integer that is less than or equal to the input number. The floor
    operation effectively rounds down the number to the nearest integer.
    For positive numbers, it truncates the decimal part. For negative
    numbers, it rounds toward negative infinity to the next lower integer.
    This function uses the math.floor() method for accurate results.

    Args:
        n: The floating-point number to calculate the floor of.

    Returns:
        An integer representing the floor value of n.

    Examples:
        >>> floor(3.14)
        3
        >>> floor(5.9)
        5
        >>> floor(-2.3)
        -3
        >>> floor(10.0)
        10
    """
    return math.floor(n)
