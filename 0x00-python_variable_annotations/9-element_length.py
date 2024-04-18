#!/usr/bin/env python3
"""
Duck typing - Annotating an iterable object
"""

from typing import Iterable, Sequence, Tuple, List

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculates the length of each element in the input iterable.

    Args:
        lst (Iterable[Sequence]): An iterable object containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
        a sequence from the input iterable and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
