#!/usr/bin/env python3
"""
Module for measuring the runtime of asynchronous comprehensions.
"""

import asyncio
from typing import List
from random import uniform


# Asynchronous generator that yields random numbers between 0 and 10
async def async_generator() -> float:
    """
    Asynchronous coroutine that yields random numbers between 0 and 10.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)


# Asynchronous comprehension that collects 10 random numbers
async def async_comprehension() -> List[float]:
    """
    Asynchronous coroutine that collects 10 random numbers using an async
    comprehension
    over async_generator, then returns the 10 random numbers.

    Returns:
        List[float]: A list of 10 random numbers between 0 and 10.
    """
    return [i async for i in async_generator()]


# Coroutine to measure runtime of four parallel comprehensions
async def measure_runtime() -> float:
    """
    Coroutine to measure the total runtime of four parallel asynchronous
    comprehensions.

    Returns:
        float: Total runtime.
    """
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
    """
    Main function to run the measure_runtime coroutine and print the
    total runtime.
    """
    runtime = await measure_runtime()
    print(f"Total runtime: {runtime}")


# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
