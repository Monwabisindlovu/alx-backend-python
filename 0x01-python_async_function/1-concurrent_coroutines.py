#!/usr/bin/env python3
"""Defines 1-concurrent_coroutines.py"""

import asyncio
from typing import List
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay
    between 0 and max_delay seconds.

    :param max_delay: Maximum delay in seconds (default is 10).
    :return: The random delay.
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Asynchronous coroutine that spawns wait_random n times
    with the specified max_delay.

    :param n: Number of times to spawn wait_random.
    :param max_delay: Maximum delay in seconds for wait_random (default is 10).
    :return: List of delays in ascending order.
    """
    delays = []

    """ Use asyncio.gather to concurrently execute wait_random"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)

    """ Sort the results in ascending order"""
    delays = sorted(results)

    return delays
