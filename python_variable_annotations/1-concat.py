#!/usr/bin/env python3
"""
This module provides string manipulation operations for text processing.

It contains a type-annotated function called 'concat' that takes two string
arguments and returns their concatenation as a single combined string.
The function demonstrates proper type annotations in Python 3 and follows
best practices for documentation, code style, and string operations.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenate two strings and return the result.

    This function takes two string arguments and combines them into a
    single string by concatenating str2 to the end of str1.

    Args:
        str1: The first string to concatenate.
        str2: The second string to concatenate.

    Returns:
        A new string that is the concatenation of str1 and str2.

    Example:
        >>> concat("Hello", " World")
        'Hello World'
        >>> concat("Python", " Programming")
        'Python Programming'
    """
    return str1 + str2
