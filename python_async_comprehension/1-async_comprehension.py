#!/usr/bin/env python3
"""Collect 10 numbers from async_generator via comprehension."""


from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return list of 10 random floats from async_generator."""
    return [value async for value in async_generator()]
