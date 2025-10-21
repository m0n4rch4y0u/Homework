f = open('17 3.txt')
a = [int(x) for x in f]
max47 = max([y for y in a if y % 100 == 47])
k = 0
maxsumm = 0
for i in range(len(a) - 3):
    if ((a[i] > 1000 and a[i+1] > 1000 and a[i+2] <= 1000 and a[i+3] <= 1000) or (a[i] > 1000 and a[i+2] > 1000 and a[i+1] <= 1000 and a[i+3] <= 1000) or (a[i] > 1000 and a[i+3] > 1000 and a[i+2] <= 1000 and a[i+1] <= 1000) or (a[i + 1] > 1000 and a[i+2] > 1000 and a[i] <= 1000 and a[i+3] <= 1000) or (a[i+1] > 1000 and a[i+3] > 1000 and a[i+2] <= 1000 and a[i] <= 1000) or (a[i+2] > 1000 and a[i+3] > 1000 and a[i+1] <= 1000 and a[i] <= 1000)) and ((a[i] + a[i+1] + a[i+2] + a[i+3]) <= max47):
        k += 1
        maxsumm = max(maxsumm,a[i] + a[i+1] + a[i+2] + a[i+3])
print(k, maxsumm)