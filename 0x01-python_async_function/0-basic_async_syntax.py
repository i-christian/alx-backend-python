#!/usr/bin/env python3
"""
Write an asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random
that waits for a random delay between 0 and
max_delay (included and float value) seconds
and eventually returns it
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    wait_random - waits for a random number of seconds
    """
    wait_period: float = random.random() * max_delay
    await asyncio.sleep(wait_period)
    return wait_period
