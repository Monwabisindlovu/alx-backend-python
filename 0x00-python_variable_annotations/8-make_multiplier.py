#!/usr/bin/env python3
"""
Complex types - functions
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier to be used.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the product of the float and the multiplier.
    """
    def multiplier_function(x: float) -> float:
        """Multiplies x by the multiplier"""
        return x * multiplier

    return multiplier_function
