#!/usr/bin/env python3
'''Make multiplier function'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Return function multi float by multi'''
    def multiply(n: float) -> float:
        '''Return n multipied'''
        return n * multiplier
    return multiply
