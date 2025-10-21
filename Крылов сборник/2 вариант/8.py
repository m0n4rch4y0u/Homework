from itertools import product

c = 0
num = 0
for x in product('РЕПЛИКА', repeat=6):
    s = ''.join(x)
    num += 1
    if num % 2 == 0 and s[0] != 'К' and s.count('И') >= 2:
        c += 1
print(c)
