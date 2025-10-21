for n in range(1,100):
    s = '31' * n + '1' * (12 - n) + '9' * 2
    while '31' in s:
        s = s.replace('31', '7', 1)
    sum_of_s = sum(map(int, s))
    if sum_of_s == 60:
        print(n)
        break
