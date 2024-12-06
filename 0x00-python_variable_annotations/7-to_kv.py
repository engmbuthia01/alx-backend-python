#!/usr/bin/env python3
"""
Takes a string and an interger
or a float ad returns a Tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple"""
    return (k, float(v ** 2))
