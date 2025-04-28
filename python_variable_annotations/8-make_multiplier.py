#!/usr/bin/env python3
"""
type-annotated function make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """that takes a float multiplier as argument and returns a function"""
    return lambda x: x*multiplier
