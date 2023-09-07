#!/usr/bin/env python3
"""importing modules """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a multiplier function based on the provided multiplier value"""
    def multiply_by_multiplier(number: float) -> float:
        """Multiply the given number by the stored multiplier value."""
        return number * multiplier
    return multiply_by_multiplier