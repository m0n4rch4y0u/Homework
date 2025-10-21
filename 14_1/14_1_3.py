from collections import *
from string import *


def ntop(n, p):
    r = ''
    alh = '0123456789abcdefghijklmnopqrstuvwxyz'
    while n:
        r = alh[n % p] + r
        n //= p
    return r


k = 2 * 9 ** 7 - 3 ** 8 - 19
print(Counter(ntop(k, 3)))
