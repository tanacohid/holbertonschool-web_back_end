#!/usr/bin/env python3

"""
Module pour mesurer le temps d'exécution moyen de la coroutine wait_n.
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Mesure le temps d'exécution total pour wait_n(n, max_delay)
    et retourne le temps moyen par coroutine (total_time / n).
    """
    start_time: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time.perf_counter()

    total_time: float = end_time - start_time
    return total_time / n
