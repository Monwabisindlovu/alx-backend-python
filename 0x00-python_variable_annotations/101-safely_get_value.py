#!/usr/bin/env python3
"""
More involved type annotations
"""

from typing import Mapping, Any, Union, TypeVar

# Define a type variable for the default value
T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: T = None) -> Union[Any, T]:
    """
    Safely gets a value from a dictionary based on a key.

    Args:
        dct (Mapping): The input dictionary.
        key (Any): The key to retrieve the value from the dictionary.
        default (Optional[T]): The default value to return if the key is not found (default is None).

    Returns:
        Union[Any, T]: The value corresponding to the key in the dictionary, or the default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default

