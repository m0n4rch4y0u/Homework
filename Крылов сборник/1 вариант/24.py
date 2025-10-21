f = open('24var01.txt')
s = f.readline()
ind_a = []
for i in range(len(s)):
    if s[i] == 'A':
        ind_a.append(i)
mincnt = 10 ** 10
for i in range(2023, len(ind_a)):
    mincnt = min(mincnt, ind_a[i] - ind_a[i-2023] + 1)
print(mincnt)
