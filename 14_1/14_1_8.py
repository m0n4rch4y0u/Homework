from collections import *


def ntop(n, p):
    r = ''
    alh = '0123456789abcdefghijklmnopqrstuvwxyz'
    while n:
        r = alh[n % p] + r
        n //= p
    return r


print(Counter(ntop(45 * 400 ** 10 - 8 ** 5 * 5 ** 8 + 16 * 20 ** 3 - 33, 20)))
