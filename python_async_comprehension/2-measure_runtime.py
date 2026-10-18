#!/usr/bin/env python3
"""
Module pour mesurer le temps d'exécution de quatre compréhensions
asynchrones exécutées en parallèle via asyncio.gather.
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Exécute async_comprehension quatre fois en parallèle à l'aide
    d'asyncio.gather, mesure le temps total d'exécution et le retourne.
    """
    start_time: float = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time: float = time.perf_counter()

    return end_time - start_time
