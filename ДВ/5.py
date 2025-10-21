for n in range(1,10000):
    s = bin(n)[2:]
    if s.count('1') % 2 == 0:
        s = '10' + s[2:] + '0'
    else:
        s = '11' + s[2:] + '1'
    r = int(s,2)
    if r < 35:
        print(n)