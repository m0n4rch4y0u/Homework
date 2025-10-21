a = [int(x) for x in open('17var01.txt')]
min25 = min([n for n in a if n % 100 == 25])
maxsum = 0
k = 0
for i in range(len(a) - 2):
    if ((len(str(a[i])) == 2 and len(str(a[i+1])) != 2 and len(str(a[i+2])) != 2) or (len(str(a[i])) != 2 and len(str(a[i + 1])) == 2 and len(str(a[i+2])) != 2) or (len(str(a[i])) != 2 and len(str(a[i+1])) != 2 and len(str(a[i+2])) == 2)) and (a[i] + a[i + 1] + a[i + 2]) < min25:
        k += 1
        maxsum = max(maxsum, a[i] + a[i + 1] + a[i + 2])
print(k, maxsum)
