#!/usr/bin/env python3
"""
Write a function named index_range that takes two integer arguments
"""


def index_range(page, page_size) -> tuple:
    """The function should return a tuple of size"""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
