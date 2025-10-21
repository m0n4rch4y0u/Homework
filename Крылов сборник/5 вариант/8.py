from itertools import product

cnt = 0
for x in product('01234567', repeat=5):
    s = ''.join(x)
    if s[0] != '0' and s.count('4') == 2 and all(x + '4' not in s for x in '1357') and all('4' + x not in s for x in '1357'):
        cnt += 1
print(cnt)
