a = []
for x in '0123456789abcdef':
    k = int(x + '131' + x + '131', 16) + int('100400' + x, 16)
    if k % 15 == 0:
        a.append(k)
        print(k)
print(min(a) // 15)
