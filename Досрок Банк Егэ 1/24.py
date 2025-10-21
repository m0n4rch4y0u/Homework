f = open('24.txt')
s = f.readline()
s = s.replace('W', 'Q')
s = s.replace('R', 'Q')
s = s.replace('2', '1')
s = s.replace('4', '1')
maxlen = 0
k = 1
for i in range(len(s)- 1):
    if s[i] != s[i+1]:
        k += 1
        maxlen = max(maxlen, k)
    else:
        k = 1
print(maxlen)