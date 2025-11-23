#!/usr/bin/env python3
"""
This module provides higher-order functions for mathematical operations.

It contains a type-annotated function called 'make_multiplier' that takes
a float multiplier as argument and returns a new function. The returned
function multiplies any given float by the original multiplier value.
This demonstrates proper type annotations for functions that return
functions (Callable types) in Python 3, following best practices for
functional programming patterns and type safety.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create and return a function that multiplies a float by a multiplier.

    This function takes a float multiplier as argument and returns a new
    function. The returned function accepts a float as its argument and
    returns the product of that float and the original multiplier. This
    is an example of a closure where the inner function captures the
    multiplier variable from the outer function's scope.

    Args:
        multiplier: A float value to be used as the multiplier.

    Returns:
        A function that takes a float and returns its product with multiplier.

    Examples:
        >>> multiply_by_2 = make_multiplier(2.0)
        >>> multiply_by_2(5.0)
        10.0
        >>> multiply_by_10 = make_multiplier(10.0)
        >>> multiply_by_10(3.5)
        35.0
    """
    def multiplier_function(n: float) -> float:
        """Multiply the given float by the captured multiplier."""
        return n * multiplier
    
    return multiplier_function
