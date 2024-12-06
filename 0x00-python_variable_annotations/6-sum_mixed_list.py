#!/usr/bin/env python3
"""
adds a mixed list of
items (floats and intergers)
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """adds mixed list and returns as float"""
    return sum(mxd_lst)
