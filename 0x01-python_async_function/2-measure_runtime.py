#!/usr/bin/env python3
''' measures the total execution time for value in iterable:
    passwait_n(n, max_delay), and returns total_time / n '''
import asyncio
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' measures the total execution time for value in iterable:
        passwait_n(n, max_delay), and returns total_time / n '''
    start = time()
    asyncio.run(wait_n(n, max_delay))
    end = time()
    return (end - start) / n
