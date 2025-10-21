from random import *

A = []
s = 0
n = int(input("Введите кол-во элементов массива: "))
for i in range(n):
    A.append(randint(1, 100))
for j in range(len(A)):
    s += A[j]
sred = s / n
for k in range(len(A)):
    if A[k] > sred:
        print("Человеческий номер элемента в списке:", k + 1)
        exit()
