from math import *

k = float(input("Введите k: "))
x = float(input("Введите x: "))
y = float(input("Введите y: "))
alpha = float(input("Ввeдите alpha: "))
a = int(input("Ввeдите a: "))
b = int(input("Ввeдите b: "))
c = int(input("Ввeдите c: "))
d = int(input("Ввeдите d: "))
n = int(input("Ввeдите n: "))

# 1) +
c1 = 100 ** 3 - 92 ** 2 + k
# 2) +
c2 = sqrt((1 - cos(x)) / 2)
# 3) +
c3 = (sqrt(abs(x)) * log(x ** 2, e)) / (-1.25 * x + e ** (x / 2))
# 4) +
c4 = sqrt(sin(x) ** 2 + cos(y ** 3) ** 2)
# 5) +
c5 = sqrt(x + sqrt(x ** 2 + 4 * y ** 2))
# 6) +
c6 = (e ** (-0.5)) * (x - alpha)
# 7) +
c7 = (1 / tan(x)) - sin(sqrt(x ** 2 + 1))
# 8) +
c8 = (0.25 * (a - b)) / (0.125 - ((abs(b)) / (10 ** (n + 3) + ((log(b) / (c - d))))))

print("1)", c1)
print("2)", c2)
print("3)", c3)
print("4)", c4)
print("5)", c5)
print("6)", c6)
print("7)", c7)
print("8)", c8)
