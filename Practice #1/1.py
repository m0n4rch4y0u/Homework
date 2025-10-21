from random import *

n = int(input("Введите размерность массива: "))

A = [randint(1, 100) for i in range(n)]
B = [randint(1, 100) for j in range(n)]
C = []
print("Массив А:", A)
print("Массив B:", B)

for x in range(n):
    if A[x] > B[x]:
        C.append(A[x])
    else:
        C.append(B[x])
print("Массив C:", C)
