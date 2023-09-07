#!/usr/bin/env python3
""" Importing modules"""
import asyncio, random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int , max_delay: int) -> List[float]:
    """ 
    Returns the list of all the delays (float values). 
    The list of the delays should be in ascending order 
    """
    tasks = [wait_random(max_delay) for _ in range(n)]

    results = await asyncio.gather(*tasks)

    return sorted(results)
