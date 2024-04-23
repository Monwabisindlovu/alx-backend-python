#!/usr/bin/env python3
"""
Module for task 1
"""
import asyncio
from typing import List
from async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronous coroutine that collects 10 random numbers using an async comprehensing
    over async_generator, then returns the 10 random numbers.
    """
    return [i async for i in async_generator()]

