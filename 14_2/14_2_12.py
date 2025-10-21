def ntop(n, p):
    r = ''
    alh = '0123456789abcdefghijklmnopqrstuvwxyz'
    while n:
        r = alh[n % p] + r
        n //= p
    return r


for p in range(2, 10 ** 6):
    for x in range(0, p):
        for y in range(1, p):
            for z in range(0, p):
                k1 = 6 * p ** 3 + x * p ** 2 + 5 * p ** 1 + x * p ** 0
                k2 = 1 * p ** 3 + x * p ** 2 + 6 * p ** 1 + 5 * p ** 0
                k3 = y * p ** 3 + 8 * p ** 2 + z * p ** 1 + 0 * p ** 0
                k = k1 + k2
                if k == k3:
                    xyz = x * p ** 2 + y * p ** 1 + z * p ** 0
                    print(xyz)
                    break
