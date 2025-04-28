#!/usr/bin/env python3
"""
type-annotated function to_kv
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    """that takes a string k and an int OR float v as arguments"""
    return (k, v**2)
