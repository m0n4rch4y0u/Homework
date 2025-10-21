from itertools import *

k = 0
for x in product('АБВГ', repeat=5):
    s = ''.join(x)
    if s.count('А') == 1:
        k += 1
print(k)
