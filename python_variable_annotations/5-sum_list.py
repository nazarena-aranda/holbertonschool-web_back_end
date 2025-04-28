#!/usr/bin/env python3
"""
Write a type-annotated function sum_list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """which takes a list input_list of floats"""
    return sum(input_list)
