from collections import *


def ntop(n, p):
    r = ''
    alh = '0123456789abcdefghijklmnopqrstuvwxyz'
    while n:
        r = alh[n % p] + r
        n //= p
    return r


print(ntop(5 * 49 ** 5 + 3 * 7 ** 8 - 7 * 7 ** 4 + 100, 7))
print(Counter(ntop(5 * 49 ** 5 + 3 * 7 ** 8 - 7 * 7 ** 4 + 100, 7)))
print(2*3 + 6 * 3 + 5)