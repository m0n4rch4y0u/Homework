from string import ascii_lowercase, digits


def n_to_p(n, p):
    t = ''
    a = digits + ascii_lowercase
    while n:
        d = a[n % p]
        t = d + t
        n //= p
    return t


f = open('17 (2).txt')
a = [int(i) for i in f]
max0F = 0
k = 0
maxsumm = 0
for x in a:
    ch16 = str(n_to_p(x, 16))
    if ch16[-2:] == '0f':
        max0F = max(max0F, int(ch16, 16))
for i in range(len(a) - 1):
    if ((a[i] % 7 == 0 and a[i + 1] % 7 != 0) or (a[i] % 7 != 0 and a[i + 1] % 7 == 0)) and (a[i] + a[i + 1]) % max0F == 0:
        k += 1
        maxsumm = max(maxsumm, a[i] + a[i + 1])
print(k, maxsumm)
