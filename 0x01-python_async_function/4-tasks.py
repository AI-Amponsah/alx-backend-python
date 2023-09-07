#!/usr/bin/env python3
""" Importing modules"""
import asyncio, random
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int , max_delay: int) -> List[float]:
    """ 
    Returns the list of all the delays (float values). 
    The list of the delays should be in ascending order 
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    results = await asyncio.gather(*tasks)

    return sorted(results)
