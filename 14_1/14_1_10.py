from collections import *


def ntop(n, p):
    r = ''
    alh = '0123456789abcdefghijklmnopqrstuvwxyz'
    while n:
        r = alh[n % p] + r
        n //= p
    return r


k = 12 * 32 ** 2 + 16 ** 3 - 0.5 * 8 ** 2 + 12
print(k)
print(Counter(ntop(16364, 8)))
