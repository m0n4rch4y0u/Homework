from functools import lru_cache
from sys import setrecursionlimit
setrecursionlimit(5000)

@lru_cache()
def f(n):
    n = str(n)
    s = 0
    for i in range(len(n)):
        s += int(n[i])
    n = int(n)
    if n < 3:
        return 1
    if n > 2 and s % 2 == 0:
        return f(n - 1) - f(n - 2)
    if n > 2 and s % 2 == 1:
        return f(n - 1) + f(n // 2)





print(f(100))
