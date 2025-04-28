#!/usr/bin/env python3
"""
Import wait_random from 0-basic_async_syntax
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Takes an integer max_delay and returns a asyncio.Task"""
    return asyncio.create_task(wait_random(max_delay))
