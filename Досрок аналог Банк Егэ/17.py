f = open('17.txt')
a = [int(x) for x in f]
minnecht = min([x for x in a if x % 2 == 1])
k = 0
maxabs = 0
for i in range(len(a) - 1):
    if ((a[i] % 3 == 0 and a[i + 1] % 3 != 0) or (a[i] % 3 != 0 and a[i + 1] % 3 == 0)) and (
            abs(a[i] - a[i + 1]) < minnecht):
        k += 1
        maxabs = max(maxabs, abs(a[i] - a[i + 1]))
print(k, maxabs)
