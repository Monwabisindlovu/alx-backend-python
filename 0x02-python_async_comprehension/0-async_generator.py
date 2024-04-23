#!/usr/bin/env python3

import asyncio
import random

async def async_generator():
    """
    This coroutine generates random numbers between 0 and 10.
    It yields a new number every second for 10 iterations.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
