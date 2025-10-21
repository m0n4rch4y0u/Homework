from collections import *


def ntop(n, p):
    r = ''
    alh = '0123456789abcdefghijklmopqrstuvwxyz'
    while n:
        r = alh[n % p] + r
        n //= p
    return r


k = 4 * 81 ** 5 + 3 ** 12 - 37
print(ntop(k, 9))
print(Counter(ntop(k, 9)))
