#!/usr/bin/env python3
"""Importing the asyncio module"""
import asyncio, random


async def wait_random(max_delay: int = 10) -> float:
    await asyncio.sleep(random.uniform(0, max_delay))
    return random.uniform(0, max_delay)

