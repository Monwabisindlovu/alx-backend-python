#!/usr/bin/env python3
"""
Module for asynchronous comprehension.
"""

import asyncio
from typing import List
from random import uniform

# Asynchronous generator that yields random numbers between 0 and 10
async def async_generator() -> float:
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)

# Asynchronous comprehension that collects 10 random numbers
async def async_comprehension() -> List[float]:
    return [i async for i in async_generator()]

# Coroutine to measure runtime of four parallel comprehensions
async def measure_runtime() -> float:
    start_time = asyncio.get_event_loop().time()
    results = await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time

# Main function to run the measure_runtime coroutine
async def main():
    runtime = await measure_runtime()
    print(f"Total runtime: {runtime}")

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
