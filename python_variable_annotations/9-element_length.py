#!/usr/bin/env python3
"""
This module provides utility functions for sequence length operations.

It contains a type-annotated function called 'element_length' that takes
an iterable of sequences and returns a list of tuples. Each tuple contains
the original sequence and its length as an integer. This demonstrates
proper type annotations for iterables, sequences, and complex return types
in Python 3, following best practices for documentation and type safety.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in an iterable of sequences.

    This function takes an iterable containing sequences (such as strings,
    lists, or tuples) and returns a list of tuples. Each tuple contains
    the original sequence as the first element and its length as the
    second element. The function works with any iterable of sequences,
    making it flexible for various input types.

    Args:
        lst: An iterable containing sequences to measure.

    Returns:
        A list of tuples, each containing a sequence and its length as int.

    Examples:
        >>> element_length(["hello", "world"])
        [('hello', 5), ('world', 5)]
        >>> element_length([[1, 2, 3], [4, 5]])
        [([1, 2, 3], 3), ([4, 5], 2)]
        >>> element_length(("abc", "defgh"))
        [('abc', 3), ('defgh', 5)]
    """
    return [(i, len(i)) for i in lst]
