#!/usr/bin/env python3
"""
Module définissant un générateur asynchrone qui produit
des nombres aléatoires après une attente d'une seconde.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Boucle 10 fois, attend 1 seconde à chaque itération
    et génère (yield) un nombre décimal aléatoire entre 0 et 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
