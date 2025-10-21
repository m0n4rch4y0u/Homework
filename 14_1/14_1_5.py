from collections import *


def ntop(n, p):
    r = ''
    alh = '0123456789abcdefghijklmnopqrstuvwxyz'
    while n:
        r = alh[n % p] + r
        n //= p
    return r


k = 3 * 19 ** 5 + 361 ** 4 - 17 * 19 ** 3 - 37
print(Counter(ntop(k, 19)))
