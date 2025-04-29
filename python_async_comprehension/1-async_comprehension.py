#!/usr/bin/env python3
"""
Import async_generator from the previous task
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """10 random numbers using an async comprehensing"""
    return [i async for i in async_generator()]
