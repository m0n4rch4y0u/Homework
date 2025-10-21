def divs(n):
    d = [1, n]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.append(i)
            d.append(n // i)
    return sorted(d)
k = 0
for i in range(600000,10**10):
    delit = divs(i)
    for j in delit:
        if delit[j] % 7 == 0 and delit[j] != 7:


