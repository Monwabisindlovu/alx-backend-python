#!/usr/bin/env python3
"""
Module for async comprehension.
"""

import asyncio
from typing import List
from async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronous coroutine that collects 10 random numbers using an async comprehension
    over async_generator, then returns the 10 random numbers.
    """
    return [i async for i in async_generator()][:10]


# Test your code
if __name__ == "__main__":
    asyncio.run(async_comprehension())
