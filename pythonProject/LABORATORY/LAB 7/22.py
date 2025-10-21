from math import *


def ch(x):
    ch = (exp(x) + exp(-1 * x)) / 2
    return ch


x = float(input("Введите значение x: "))
y = ch(x + 2) - 3 * ch(x) + (tan(1 - ch(2 * x - 3)) ** 2)
print(y)
