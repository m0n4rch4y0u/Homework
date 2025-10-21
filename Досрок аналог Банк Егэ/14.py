def n_to_p(n, p):
    alf = '0123456789abcdefghijklmnopqrstuvwxyz'
    r = ''
    while n:
        r = alf[n % p] + r
        n //= p
    return r


f = 4 ** 2018 + 7 ** 2022 + 2024 + 13 ** 2018 + 2020 - 17 * (4 ** 2020)
s = 0
while f > 0:
    s += f % 27
    f = f // 27
print(s)
