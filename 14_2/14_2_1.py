a = []
for x in '0123456789abcdefghij':
    k = int('12345' + x + '78', 20) + int('9' + x + '765', 20)
    if k % 19 == 0:
        a.append(k)
print(max(a) // 19)
