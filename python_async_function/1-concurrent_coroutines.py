#!/usr/bin/env python3
"""
Module définissant une routine asynchrone pour lancer
plusieurs coroutines wait_random de manière concurrente.
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Lance wait_random n fois avec un max_delay spécifié
    et retourne la liste de tous les délais par ordre croissant
    au fur et à mesure de leur achèvement.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
