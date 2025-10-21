import math

def bisector_length(a, b, c):
    la = math.sqrt(b * c * (1 - (a ** 2) / ((b + c) ** 2)))
    lb = math.sqrt(a * c * (1 - (b ** 2) / ((a + c) ** 2)))
    lc = math.sqrt(a * b * (1 - (c ** 2) / ((a + b) ** 2)))
    return la, lb, lc

a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))

if a + b > c and a + c > b and b + c > a:
    la, lb, lc = bisector_length(a, b, c)
    print(f"Длины биссектрис:\nL_a = {la:.2f}, L_b = {lb:.2f}, L_c = {lc:.2f}")
else:
    print("Треугольник с такими сторонами не существует")
