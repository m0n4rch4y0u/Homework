alh = 'АГМНСТУ'
k = 0
for x1 in alh:
    for x2 in alh:
        for x3 in alh:
            for x4 in alh:
                for x5 in alh:
                    for x6 in alh:
                        s = x1 + x2 + x3 + x4 + x5 + x6
                        k += 1
                        if s[0] != 'У' and s.count('М') == 2 and s.count('Г') <= 1:
                            print(k, s)

