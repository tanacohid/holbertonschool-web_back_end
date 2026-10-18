#!/usr/bin/env python3
"""
Module définissant une coroutine async_comprehension qui utilise
une compréhension asynchrone pour collecter 10 nombres aléatoires.
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collecte 10 nombres aléatoires via une compréhension asynchrone
    sur async_generator et retourne la liste de ces nombres.
    """
    return [number async for number in async_generator()]
