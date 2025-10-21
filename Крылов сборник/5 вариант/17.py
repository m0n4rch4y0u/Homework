a = [int(x) for x in open('17var05.txt')]
maxx = max([y for y in a])
max2 = -1
cnt = 0
for i in range(len(a) - 1):
    if a[i] + a[i + 1] == maxx:
        cnt += 1
        max2 = max(max2, a[i] ** 2 + a[i + 1] ** 2)
print(cnt, max2)
