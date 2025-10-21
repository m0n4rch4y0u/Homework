from random import *

A = []
s = 0
nech = 0
n = int(input("Введите кол-во элементов массива: "))
for i in range(n):
    A.append(randint(1, 5))
for j in range(len(A)):
    if A[j] % 2 == 1:
        nech = 2 * A[j]
        break
for k in range(len(A)):
    if A[k] == nech:
        print(k)
        break