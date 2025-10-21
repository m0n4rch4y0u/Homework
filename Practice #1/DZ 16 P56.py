from random import *

n = int(input("Введите размерность массива: "))
print()
array = [randint(-100, 100) for i in range(n)]
print("Массив А:", array)
print()

summ_minus = 0
summ_plus = 0
summ = 0
for i in range(n):
    if array[i]>=0:
        summ_plus+=array[i]
    else:
        summ_minus += array[i]
summ = summ_plus + summ_minus
if summ >= 0:
    array.append(-1*summ)
else:
    array.append(summ)

print("Ответ:", array)
