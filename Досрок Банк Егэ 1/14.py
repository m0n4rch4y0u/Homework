for x in '0123456789abcdefghijklmnopq':
    k = int('123' + x + '23', 27) + int('635'+ x + '78', 27)
    if k % 26 == 0:
        print(k // 26)
