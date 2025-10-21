from random import *


m = int(input("Введите размерность матрицы: "))
n = int(input("Введите размерность матрицы: "))

A = [[randint(10, 100) for j in range(m)] for i in range(m)]

S = 0
for i in range(m):
    for j in range(m):
        print(A[i][j], end=' ')
        if i == j:
            S += A[i][j]
    print()
print("Сумма элементов главной диагонали:", S)