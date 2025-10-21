a = []
for n in range(1, 226):
    n2 = bin(n)[2:]
    if n % 2 == 1:
        n2 = '11' + n2 + '11'
    else:
        n2 = '1' + n2 + '0'
    r = int(n2, 2)
    if r > 225:
        a.append(r)
print(min(a))