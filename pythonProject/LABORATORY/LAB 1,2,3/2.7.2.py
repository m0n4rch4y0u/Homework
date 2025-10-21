from math import *

a = []
a.append(int(input('Введите значение a: ')))
x = int(input('Введите значение x: '))
l2 = sqrt(25 - cos(x) / 5 ** 2)
a.append(l2)
n = 1
while abs(a[n] - a[n - 1]) > 0.0000005:
    an = sqrt(25 - cos(x - a[n - 1] ** 3) / 5 ** n)
    a.append(an)
    n += 1
print(a[n])
