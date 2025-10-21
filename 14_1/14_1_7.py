from collections import *


def ntop(n, p):
    r = ''
    alh = '0123456789abcdefghijklmnopqrstuvwxyz'
    while n:
        r = alh[n % p] + r
        n //= p
    return r


print(ntop(2 ** 2026 + 2 ** 2025 + 2 ** 2024 - 2, 16))
