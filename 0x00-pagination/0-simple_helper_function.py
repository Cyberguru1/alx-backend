#!/usr/bin/env python3
"""
Contains definition of index_range helper function
to simulate pagination
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    2 integer arguments are given as input and returns a tuple of size two
    containing the start and end indexes
    Args:
        page (int): page number to return (pages are 1-indexed)
        page_size (int): number of items per page
    Return:
        tuple(start_index, end_index)
    """
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)
