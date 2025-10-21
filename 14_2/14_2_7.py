a = []
for x in '0123456789abcdefghijkl':
    for y in '0123456789abc':
        k = int(x + '23' + x + '5', 22) - int('67' + y + '9' + y, 13)
        if k % 57 == 0 and k > 0:
            print(x, y, ':', k)
            a.append(k)
print(a)
print(1474647 // 57)
