for x in range(100):
    for y in range(100):
        for z in range(100):
            s = '0' + '1' * x + '2' * y + '3' * z
            s1 = s
            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01', '20', 1)
                s = s.replace('02', '301', 1)
                s = s.replace('03', '1102', 1)
            if s.count('1') == 20 and s.count('2') == 100 and s.count('3') == 40:
                print(s1.count('1'))
                break
