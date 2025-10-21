a = []
for x in '0123456789abcde':
    for y in '0123456789abcdefg':
        k = int('123' + x + '5', 15) + int('67' + y + '9', 17)
        if k % 131 == 0:
            print(x, y, ':', k)
            a.append(k)
print(a)
print(89886 // 131)

