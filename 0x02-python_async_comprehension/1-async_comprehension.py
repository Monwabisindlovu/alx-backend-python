#!/usr/bin/env python3
"""
Module for asynchronous comprehension.
"""

import asyncio
from typing import List
from random import uniform


async def async_generator() -> float:
    """
    Asynchronous coroutine that yields random numbers between 0 and 10.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)


async def async_comprehension() -> List[float]:
    """
    Asynchronous coroutine that collects 10 random numbers using an async
    comprehension
    over async_generator, then returns the 10 random numbers.

    Returns:
        List[float]: A list of 10 random numbers between 0 and 10.
    """
    return [i async for i in async_generator()]
