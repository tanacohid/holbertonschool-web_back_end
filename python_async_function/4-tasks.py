#!/usr/bin/env python3
"""
Module définissant une routine asynchrone task_wait_n qui crée
et gère des objets asyncio.Task pour task_wait_random.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Crée n tâches task_wait_random avec le max_delay spécifié
    et retourne la liste de tous les délais par ordre croissant
    au fur et à mesure de leur achèvement.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
