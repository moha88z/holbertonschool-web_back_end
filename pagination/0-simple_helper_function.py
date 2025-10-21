#!/usr/bin/env python3
"""Helper function for pagination."""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Compute start and end indexes (end is exclusive) for 1-indexed pagination.

    Example:
      page=1, page_size=7  -> (0, 7)
      page=3, page_size=15 -> (30, 45)
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
