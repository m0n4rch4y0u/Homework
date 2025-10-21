f = open('17.txt')
a = [int(i) for i in f]
min19 = min([i for i in a if i % 19 == 0])
k = 0
maxsum = 0
for i in range(len(a) - 1):
    if a[i] < min19 or a[i + 1] < min19:
        k += 1
        maxsum = max(maxsum, a[i] + a[i + 1])
print(k, maxsum)
