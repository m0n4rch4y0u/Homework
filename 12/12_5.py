def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

for n in range(1,1000):
    s = '>' + 14 * '1'