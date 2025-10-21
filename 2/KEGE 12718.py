print('k l m n')
for k in 0, 1:
    for l in 0, 1:
        for m in 0, 1:
            for n in 0, 1:
                f1 = (not (k <= m)) and (k or n) or (l <= n)
                if f1 == 0:
                    print(k, l, m, n)
