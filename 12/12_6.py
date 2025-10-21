k = 0
for n in range(1, 1000):
    s = '0' + '2' * n
    while '02' in s or '2222' in s or '4422' in s:
        if '02' in s:
            s = s.replace('02', '44', 1)
        if '4422' in s:
            s = s.replace('4422', '20', 1)
        if '2222' in s:
            s = s.replace('2222', '0', 1)
    sum_of_s = sum(map(int, s))
    if sum_of_s == 100:
        k += 1
print(k)