a = []
for x in '0123456789abcdefghijklmn':
    for y in '0123456789abcdefghijklmn':
        k = int('3' + x + y + '3', 24) + int('1' + y + '31', 24)
        if k % 5 == 0:
            a.append(x)
maxx = max(a)
print(maxx)
k2 = int('3' + maxx + '73', 24) + int('1' + '731', 24)
print(k2 / 5)
