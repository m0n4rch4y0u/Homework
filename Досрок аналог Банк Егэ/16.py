from functools import lru_cache
from sys import setrecursionlimit

@lru_cache()
def f(n):
    if n >= 2025:
        return n
    else:
        return n + 3 + f(n + 3)


setrecursionlimit(10000000)

print(f(2018) - f(2022))
