#!/usr/bin/env python3
""""""
import asyncio, time
from typing import List
wait_n = __import__('1-concurrent_coroutines.py').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """" """
    start_Time = time.time()

    asyncio.run(wait_n(n, max_delay))

    endTime = time.time()
    totalTime = endTime - start_Time

    return totalTime / n

