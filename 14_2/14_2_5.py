a = []
for x in '0123456789abcde':
    k = int('131' + x + '1', 15) + int('13' + x + '3', 17)
    if k % 11 == 0:
        a.append(k)
print(max(a) // 11)
