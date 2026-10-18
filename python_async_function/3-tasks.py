#!/usr/bin/env python3
"""
Module pour créer et retourner un objet asyncio.Task
à partir de la coroutine wait_random.
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Prend un entier max_delay et retourne un objet asyncio.Task
    qui encapsule la coroutine wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
