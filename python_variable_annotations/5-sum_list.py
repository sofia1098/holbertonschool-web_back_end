#!/usr/bin/env python3
"""
This module provides mathematical operations for lists of numbers.

It contains a type-annotated function called 'sum_list' that takes a list
of floating-point numbers as argument and returns their sum as a float.
The function demonstrates proper type annotations for list operations in
Python 3 and follows best practices for documentation and type safety.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate and return the sum of all floats in a list.

    This function takes a list of floating-point numbers and returns
    the total sum of all elements in the list. It iterates through
    each element and accumulates their values to produce the final
    result. The function is properly type-annotated to ensure that
    only lists of floats are accepted and a float value is returned.

    Args:
        input_list: A list containing floating-point numbers to sum.

    Returns:
        A float representing the sum of all numbers in input_list.

    Examples:
        >>> sum_list([3.14, 1.11, 2.22])
        6.470000000000001
        >>> sum_list([1.5, 2.5, 3.5])
        7.5
        >>> sum_list([])
        0.0
    """
    return sum(input_list)
