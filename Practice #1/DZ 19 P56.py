from random import *

n = int(input("Введите размерность массива: "))
B = int(input("Введите левую границу: "))
C = int(input("Введите правую границу: "))
print()
array = [randint(-100, 100) for i in range(n)]
print("Массив А:", array)
del array[B:C]
print()
print("Ответ:", array)
