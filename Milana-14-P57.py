from random import *

n = int(input("Введите размерность массива: "))
print()
array = [randint(-100, 100) for i in range(n)]
print("Массив:", array)
array_plus = []
array_minus = []
for i in range(n):
    if array[i] > 0:
        array_plus.append(array[i])
    elif array[i] < 0:
        array_minus.append(array[i])
print()
print("Ответ с +:", array_plus)
print("Ответ с -:", array_minus)
