f = open('17-1.txt')
a = [int(i) for i in f]
summ = 0
maxsumm = 0
k = 0
count = 0
for i in a:
    if abs(i) < 100:
        count += 1
for u in range(len(a) - 1):
    if ((a[u] + a[u + 1]) / 2) > count:
        k += 1
        maxsumm = max(maxsumm, a[u] + a[u + 1])
print(k, maxsumm)