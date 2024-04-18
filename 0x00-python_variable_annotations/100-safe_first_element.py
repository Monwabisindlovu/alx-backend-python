#!/usr/bin/env python3
"""Augmenting the code with the correct duck-typed annotations:"""
from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Returns the first element of the sequence or None if
    the sequence is empty."""
    if lst:
        return lst[0]
    else:
        return None
