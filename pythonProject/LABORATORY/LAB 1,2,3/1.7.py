from math import *

x = float(input("Введите x: "))
y = float(input("Введите y: "))
z = float(input("Ввeдите z: "))

# 1) ++
a1 = (sqrt(abs(x - 1)) - abs(y) ** (1 / 3)) / (1 + (x ** 2 / 2) + (y ** 2 / 4))
b1 = x * (atan(z) + e ** (-1 * (x + 3)))
# 2) ++
a2 = (3 + e ** (y - 1)) / (1 + (x ** 2) * abs(y - tan(z)))
b2 = 1 + abs(y - x) + ((y - x) ** 2) / 2 + (abs(y - x) ** 3) / 3
# 3) ++
a3 = (2 * cos(x - (pi / 6))) / (0.5 + sin(y) ** 2)
b3 = 1 + ((z ** 2) / (3 + (z ** 2) / 5))

print("1)", a1, b1)
print("2)", a2, b2)
print("3)", a3, b3)
