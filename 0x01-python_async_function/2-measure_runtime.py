#!/usr/bin/env python3
"""Defines 2-measure_runtime.py"""

import asyncio
from typing import List
import time
from functools import wraps


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


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n.

    :param n: Number of times to execute wait_n.
    :param max_delay: Maximum delay in seconds for wait_random (default is 10).
    :return: Average execution time per call.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    average_time_per_call = total_time / n
    return average_time_per_call


if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
