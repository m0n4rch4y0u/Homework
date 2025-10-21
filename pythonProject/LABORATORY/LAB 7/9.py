from math import *


def area_of_the_polygon(n, R):
    a = 2 * R * sin(radians(180 / n))
    r = R * cos(radians(180 / n))
    S = 0.5 * a * n * r
    return S


n = int(input("Введите кол-во углов в многоугольнике: "))
R = int(input("Введите радиус описанной окружности: "))
print(area_of_the_polygon(n, R))
