from math import *

k = int(input("Введите значение k: "))
l = int(input("Введите значение l: "))
m = int(input("Введите значение m: "))
x = float(input("Введите значение x: "))
if m == min(k, l):
    yx = sin(abs(x)) / sqrt((x ** 2) + 1)
elif m == max(k, l):
    yx = abs(x) * log(1 + x, e)
elif min(k, l) <= m <= max(k, l):
    yx = x**3 + x + 10**(-2)
else:
    yx = -1
zy = yx**4 - yx**2 + 5
print("Значение функции у от х:", yx)
print("Значение функции x от y:", zy)