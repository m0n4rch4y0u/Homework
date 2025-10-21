import math
def square(d):
    S = math.pi * (d ** 2) / 4
    return S
d1 = float(input("Введите диаметр первого круга d1: "))
d2 = float(input("Введите диаметр второго круга d2: "))
d3 = float(input("Введите диаметр третьего круга d3: "))
print(f"Площадь первого круга S1: {square(d1):.2f}")
print(f"Площадь второго круга S2: {square(d2):.2f}")
print(f"Площадь третьего круга S3: {square(d3):.2f}")
