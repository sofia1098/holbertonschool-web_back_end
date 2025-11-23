#!/usr/bin/env python3
"""
This module provides mathematical operations for mixed-type lists.

It contains a type-annotated function called 'sum_mixed_list' that takes
a list containing both integers and floats as argument and returns their
sum as a float. The function demonstrates proper type annotations for
Union types with lists in Python 3, following best practices for handling
multiple numeric types and ensuring type safety in mathematical operations.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate and return the sum of all integers and floats in a list.

    This function takes a list containing a mix of integers and floating-point
    numbers and returns the total sum of all elements as a float. It works
    with any combination of int and float values, automatically converting
    the result to a float type. The function uses Python's built-in sum()
    function for efficient calculation.

    Args:
        mxd_lst: A list containing integers and/or floats to sum.

    Returns:
        A float representing the sum of all numbers in mxd_lst.

    Examples:
        >>> sum_mixed_list([5, 4, 3.14, 666, 0.99])
        679.13
        >>> sum_mixed_list([1, 2, 3])
        6.0
        >>> sum_mixed_list([1.5, 2.5, 3.5])
        7.5
    """
    return float(sum(mxd_lst))
