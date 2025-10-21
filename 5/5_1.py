a = []
for n in range(1, 10000):
    n1 = bin(n)[2:]
    if n1.count('1') % 2 == 0:
        n2 = '10' + n1[2:] + '0'
    else:
        n2 = '11' + n1[2:] + '1'
    r = int(n2, 2)
    if r < 20:
        a.append(n)
print(max(a))
