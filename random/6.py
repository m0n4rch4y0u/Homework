min_n = 10 ** 6
for n in range(3, 100):
    s = '2' + n * '5'
    while '25' in s or '35' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '53', 1)
        if '35' in s:
            s = s.replace('35', '2', 1)
        if '555' in s:
            s = s.replace('555', '23', 1)
    s = str(s)
    summ_s = 0
    for i in range(len(s)):
        summ_s += int(s[i])
    if s % 7 == 0 and n < min_n:
        min_n = n
print(n)
