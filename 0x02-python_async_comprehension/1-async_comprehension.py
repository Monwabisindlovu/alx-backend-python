#!/usr/bin/env python3

from async_generator import async_generator

async def async_comprehension():
    """
    This coroutine collects 10 random numbers using async comprehension.
    """
    return [i async for i in async_generator()]
