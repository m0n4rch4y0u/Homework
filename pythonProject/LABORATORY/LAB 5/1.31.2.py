from random import *

A = []
B = []
n = int(input("Введите кол-во элементов массива: "))
for i in range(n):
    A.append(randint(1, 5))
B.append(A[0])
for j in range(len(A)-2):
    B.append((A[j+1]-A[j]) / 3)
B.append(A[-1])

print("Массив A:")
for k, number in enumerate(A, start=1):
    print(f"{k}. {number}")
print("Массив B:")
for k, number in enumerate(B, start=1):
    print(f"{k}. {number}")
