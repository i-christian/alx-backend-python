#!/usr/bin/env python3
"""
.1-async_comprehension.py
"""

import typing

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """
    Async coroutine that collects 10 rand numbers using async comprehension.

    This coroutine uses async comprehension over the async_generatorcoroutine
    coroutine to collect 10 random numbers asynchronously.

    Returns:
        List[float]: A list of 10 random float numbers.
    """
    return [rand async for rand in async_generator()]
