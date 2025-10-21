f = open('24var02.txt')
s = f.readline()
ind_a = []
for i in range(len(s)):
    if s[i] == 'A':
        ind_a.append(i)
maxcnt = -1
for i in range(349, len(ind_a)):
    maxcnt = max(maxcnt, ind_a[i] - ind_a[i-349] + 1)
print(maxcnt)
