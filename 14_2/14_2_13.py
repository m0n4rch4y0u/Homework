def ntop(n, p):
    r = ''
    alh = '0123456789abcdefghijklmnopqrstuvwxyz'
    while n:
        r = alh[n % p] + r
        n //= p
    return r


for x in range(0, 27):
    for y in range(0, 27):
        a1 = 3 * 27 ** 8 + 1 * 27 ** 7 + x * 27 ** 6 + 1 * 27 ** 5 + 3 * 27 ** 4 + 1 * 27 ** 3 + y * 27 ** 2 + 1 * 27 ** 1 + 3 * 27 ** 0
        a2 = x * 27 ** 1 + y * 27 ** 0
        if a1 % 26 == 0 and a2 ** 0.5 % 1 == 0:
            print(a2)
            break
