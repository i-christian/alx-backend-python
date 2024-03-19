#!/usr/bin/env python3
"""
.0-async_generator.py
"""
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """
    Asynchronous generator coroutine that yields rand numbers between 0 and 10.

    This coroutine loops 10 times, each time asynchronously waiting for 1 sec.
    and then yielding a random number between 0 and 10 using the random module.

    Yields:
        float: A random float between 0 and 10.

    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
