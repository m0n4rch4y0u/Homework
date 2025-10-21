summ = 0
for n in range(3, 10001):
    s = '1' + '2' * n
    while '12' in s or '5522' in s or '2222' in s:
        if '12' in s:
            s = s.replace('12', '55', 1)
        if '2222' in s:
            s = s.replace('2222', '1', 1)
        if '5522' in s:
            s = s.replace('5522', '21', 1)
    for i in range(len(s)):
        summ += int(s[i])
    if summ == 142:
        print(n)
        break
    else:
        summ = 0
