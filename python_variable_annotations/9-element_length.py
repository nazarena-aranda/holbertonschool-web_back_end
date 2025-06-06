#!/usr/bin/env python3
"""
module of the function
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotate parameters and return values with the appropriate types"""
    return [(i, len(i)) for i in lst]
