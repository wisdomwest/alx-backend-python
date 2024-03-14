#!/usr/bin/env python3
'''Duck typing - first element of a sequence'''

from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Return first element of a sequence'''
    if lst:
        return lst[0]
    else:
        return None
