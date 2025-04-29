#!/usr/bin/env python3
"""
Import async_comprehension from the previous file and write a
measure_runtime coroutine
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime should measure the total runtime and return it"""
    start = time.perf_counter()

    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)

    end = time.perf_counter()

    total = end - start
    return total
