for x in '0123456789abcdefghijklm':
    s = int('1' + x + '1' + x + '1' + x + '1' + x + '1', 23) + int('20' + x + '24', 23) + int('1' + x + '235', 23)
    if s % 22 == 0:
        print(s // 22)
        break
