from itertools import product

words = product('АВОРТ', repeat=6)
s = 0
for w in words:
    word = ''.join(w)
    s+=1
    print(s, word)
