a10 = [2]
s = 0
for i in range(9):
    a10.append(a10[i] + i ** 2)
for j in range(len(a10)):
    s += a10[j]
print("Среднее арифмитическое массива:", s / 10)
