#!/usr/bin/env python3
"""annotating types"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns values with appropriate types"""
    return [(i, len(i)) for i in lst]
