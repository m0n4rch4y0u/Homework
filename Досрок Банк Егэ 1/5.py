for n in range(1, 110):
    n1 = bin(n)[2:]
    if n % 2 == 0:
        n1 += '10'
    else:
        n1 = '1' + n1 + '10'
    r = int(n1, 2)
    if r <= 110:
        print(r)
