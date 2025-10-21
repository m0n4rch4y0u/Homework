from random import *

A = []
B = []
s = 0
n = int(input("Введите кол-во элементов массива: "))
for i in range(n):
    A.append(randint(1, 5))
for j in range(len(A)):
    s += A[j]
    B.append((A[j]) / (1 + (s) ** 2))

print("Массив A:")
for k, number in enumerate(A, start=1):
    print(f"{k}. {number}")
print("Массив B:")
for k, number in enumerate(B, start=1):
    print(f"{k}. {number}")
