from random import *

n = int(input("Введите размерность массива: "))
print()
A = [randint(1, 100) for i in range(n)]
print("Массив А:", A)

s = 0
for x in range(n):
    s += A[x]
sred = s / len(A)
print('Среднее арифметическое массива:', sred)
