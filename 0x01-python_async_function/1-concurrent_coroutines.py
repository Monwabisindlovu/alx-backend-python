#!/usr/bin/env python3
"""
Module for task 1
"""
import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async routine called 'wait_n' that takes in 2 int arguments:
    n and max_delay. It will spawn 'wait_random' n times with the
    specified max_delay. 'wait_n' should return the list of all the
    delays (float values). The list of the delays should be in
    ascending order without using sort() because of concurrency.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
