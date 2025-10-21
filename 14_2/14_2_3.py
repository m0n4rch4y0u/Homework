n = 0
for x in '0123456789abcdefghijklmno':
    k = int('3' + x + '4' + x + '3' + x + '3', 25) + int('1' + x + '3' + x + '1' + x, 25)
    if k % 24 == 0:
        n += 1
print(n)
