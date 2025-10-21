from functools import lru_cache
from sys import setrecursionlimit

def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n * f(n - 1)


setrecursionlimit(1000000)

print(f(2024) // (f(2023) - f(2022)))
