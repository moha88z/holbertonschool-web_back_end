#!/usr/bin/env python3
"""Yield 10 random numbers with 1s delay."""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yield 10 random floats 0-10, each after 1 second."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
