from collections import *


def ntop(n, p):
    r = ''
    alh = '0123456789abcdefghijklmnopqrstuvwxyz'
    while n:
        r = alh[n % p] + r
        n //= p
    return r


a = []
for x in range(1, 1000):
    if len(ntop(x, 12)) == 2 and str(ntop(x, 16)[-1]) == '3' and str(ntop(x, 5)[-1]) == '1':
        a.append(x)
print(max(a))
