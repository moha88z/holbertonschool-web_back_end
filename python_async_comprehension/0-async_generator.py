#!/usr/bin/env python3
"""Async generator that yields random numbers between 0 and 10."""

import asyncio
import random


async def async_generator():
    """Loop 10 times, wait 1 second each time, then yield a random number."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
