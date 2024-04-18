#!/usr/bin/env python3
"""
Duck typing - Annotating the first element of a sequence
"""

from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the input sequence, or None if the sequence is empty.

    Args:
        lst (Sequence[Any]): A sequence of elements of any type.

    Returns:
        Union[Any, None]: The first element of the sequence, or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None

