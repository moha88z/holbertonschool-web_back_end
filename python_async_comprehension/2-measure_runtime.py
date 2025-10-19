#!/usr/bin/env python3
"""Measure total runtime of running async_comprehension 4x in parallel."""


import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Execute async_comprehension 4x concurrently & return total runtime."""
    start: float = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end: float = time.perf_counter()
    return end - start
