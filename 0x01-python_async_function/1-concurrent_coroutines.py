#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes multiple coroutines concurrently and returns the list of all delays
    """
    delays = [wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*delays)


if __name__ == "__main__":
    import time

    async def main():
        start = time.time()
        print(await wait_n(5, 5))
        print(await wait_n(10, 7))
        print(await wait_n(10, 0))
        end = time.time()
        print(f"Total runtime: {end - start} seconds")

    asyncio.run(main())
