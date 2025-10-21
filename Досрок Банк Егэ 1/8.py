letters = 'АПКСУ'
k = 0
for w1 in letters:
    for w2 in letters:
        for w3 in letters:
            for w4 in letters:
                for w5 in letters:
                    for w6 in letters:
                        word = w1 + w2 + w3 + w4 + w5 + w6
                        k += 1
                        if word.count('У') == 1 and 'AA' not in word:
                            print(k)
