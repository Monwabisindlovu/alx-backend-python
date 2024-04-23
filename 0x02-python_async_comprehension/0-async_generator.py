#!/usr/bin/env python3
"""
Module for asynchronous generator.
"""

import asyncio
import random
from typing import Generator


# Two blank lines here
async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous coroutine that yields random numbers between 0 and 10.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
