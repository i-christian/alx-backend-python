#!/usr/bin/env python3
'''
.2-measure_runtime.py
'''

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Executes async_comprehension 4 times and measures the total execution time.

    This coroutine measures the total execution time of executing
    async_comprehension 4 times concurrently using asyncio.gather.

    Returns:
        float: The total execution time in seconds.

    '''
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
