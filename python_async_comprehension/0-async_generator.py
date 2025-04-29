#!/usr/bin/env python3
"""
A coroutine called async_generator
"""
import asyncio
import random


async def async_generator():
    """The coroutine will loop 10 times, each time asynchronously wait 1s"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
