#!/usr/bin/env python3
"""
.2-measure_runtime.py
"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measure_runtime - Computes the average runtime of wait_n.
    args:
        n - integer
        max_delay - integer
    return: float
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start) / n
