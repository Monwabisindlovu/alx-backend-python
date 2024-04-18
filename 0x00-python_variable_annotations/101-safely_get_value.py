#!/usr/bin/env python3
"""
Adding type annotations to the function 'safely_get_value'.

This script defines a function 'safely_get_value' that retrieves a value
associated with a key from a dictionary safely. It includes type annotations
using the 'typing' module to indicate the expected types of the parameters and
the return value.
"""
from typing import TypeVar, Mapping, Any, Union, Optional


T = TypeVar('T')


def safely_get_value(
    dct: Mapping[Any, T],
    key: Any,
    default: Optional[T] = None
) -> Union[T, None]:
    """
    Gets the value associated with the key from the dictionary safely,
    with an optional default value.

    Args:
        dct (Mapping[Any, T]): The dictionary to retrieve the value from.
        key (Any): The key to look up in the dictionary.
        default (Optional[T], optional): The default value to return if the key
            is not present (default is None).

    Returns:
        Union[T, None]: The value associated with the key if present,
        otherwise the default value (or None if not specified).
    """
    if key in dct:
        return dct[key]
    else:
        return default
