def Del(n, m):
    return n % m == 0

b = list(range(142, 253))
for a in range(1, 1000):
    a_true = True
    for x in range(1,1000):
        if (Del(x, 6) <= (not Del(x,15))) or (not (x + a in b)) == False:
            break
    else:
        print(a)
