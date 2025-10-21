from random import *

A = []
n = int(input("Введите кол-во элементов массива: "))
for i in range(n):
    A.append(randint(3, 5))
count_of_number = A.count(5)
print("Массив A:")
for k, number in enumerate(A, start=1):
    print(f"{k}. {number}")
print(f'Количество числа 5 в массиве A: {count_of_number}')