summ = 0
for n in range(3, 10000):
    s = '1' + n * '2'
    while '12' in s or '3322' in s or '2222' in s:
        if '12' in s:
            s = s.replace('12', '33', 1)
        if '2222' in s:
            s = s.replace('2222', '1', 1)
        if '3322' in s:
            s = s.replace('3322', '21', 1)
    for i in range(len(s)):
        summ += int(s[i])
    if summ == 218:
        print(n)
        break
    else:
        summ = 0

