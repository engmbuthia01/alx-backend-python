#!/usr/bin/env python3
"""
Module to define wait_n coroutine.
"""
import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.
    Returns a list of all delays in ascending order without using sort().
    """
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        # Insert delay into the list at the correct position
        for i, existing_delay in enumerate(delays):
            if delay < existing_delay:
                delays.insert(i, delay)
                break
        else:
            delays.append(delay)
    return delays
