#!/usr/bin/env python3
"""
type-annotated function sum_mixed_list
"""
from typing import List


def sum_mixed_list(mxd_lst: List[float]) -> float:
    """takes a list mxd_lst of integers and floats"""
    return sum(mxd_lst)
