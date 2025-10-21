from sys import setrecursionlimit

setrecursionlimit(10000)


def n_to_p(n, p):
    alf = '0123456789abcdefghijklmnopqrstuvwxyz'
    r = ''
    while n:
        r = alf[n % p] + r
        n //= p
    return r

def perevod(n):
    digits = '01234'
    if n < 5:
        return digits[n]
    return perevod(n // 5) + digits[n % 5]


s = 4 * 25 ** 2022 - 2 * 5 ** 2000 + 125 ** 1011 - 3 * 5 ** 100 - 660
print(n_to_p(s, 25).count('4'))
SS