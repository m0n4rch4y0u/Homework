alh = 'АБРТЫ'
k = 0
for w1 in alh:
    for w2 in alh:
        for w3 in alh:
            for w4 in alh:
                for w5 in alh:
                    word = w1 + w2 + w3 + w4 + w5
                    k += 1
                    if word.count('Р') == 0 and word.count('А') == 0:
                        print(k)
                        exit()

