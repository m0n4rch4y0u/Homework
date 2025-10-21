from random import *

A = []
n = int(input("Введите кол-во элементов массива: "))
const = int(input("Введите константу: "))
score = 0
for i in range(n):
    A.append(randint(1, 100))
for j in range(len(A)):
    if A[j] > const:
        score += 1
print("Массив A:")
for k, number in enumerate(A, start=1):
    print(f"{k}. {number}")
print(f'Количество значений больше const в массиве A: {score}')
