from random import *

A = []
B = []
k = 0
n = int(input("Введите кол-во элементов массива: "))
for i in range(n):
    A.append(randint(-5, 5))
for j in range(len(A)):
    if A[j] > 0:
        k += 1
for z in range(len(A)):
    if z > k:
        B.append(z)
print(B[-1])