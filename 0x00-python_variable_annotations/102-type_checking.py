#!/usr/bin/env python3
"""
Using mypy to validate a piece of code

This script defines a function 'zoom_array' that takes a Tuple and an optional
factor as arguments and returns a List containing each element of the Tuple
repeated by the specified factor. It then demonstrates the use of this function
by creating an array and zooming it in by a factor of 2 and 3.
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms in on the elements of the input Tuple.

    Args:
        lst (Tuple): The input Tuple.
        factor (int, optional): The zoom factor (default is 2).

    Returns:
        List: A List containing each element of the Tuple repeated by the
        specified factor.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
