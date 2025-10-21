def perevod(n):
    digits = '0123'
    if n < 4: return digits[n]
    return perevod(n // 4) + digits[n % 4]


for i in range(1, 1000):
    s = perevod(i)
    if i % 4 == 0:
        s = s + s[-2:]
    else:
        s = s + perevod(i % 4 * 2)
    if int(s, 4) < 261:
        print(i)
