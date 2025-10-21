def perevod(n):
    digits = '0123'
    if n < 4: return digits[n]
    return perevod(n // 4) + digits[n % 4]


for i in range(1, 1000):
    n = perevod(i)
    if i % 4 == 0:
        n = n + n[-2:]
    else:
        n = n + perevod(i % 4 * 2)
    r = int(n, 4)
    if r < 369:
        print(i)

