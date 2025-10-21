f = open('17.txt')
min123 = min([x for x in f if int(x) % 123 == 0])
a = [int(i) for i in f]
k = 0
for i in range(len(a) - 1):
    if (a[i] % 2023 >= min123 and a[i + 1] % 2023 < min123) or (a[i + 1] % 2023 >= min123 and a[i] % 2023 < min123):
        k += 1
print(k)
