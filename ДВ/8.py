from itertools import *

k = 0
for x in product('012345678', repeat=6):
    s = ''.join(x)
    if s[0] != '0' and s[0] not in '1357' and s[-1] not in '23' and s.count('1') >= 2:
        k += 1
print(k)
