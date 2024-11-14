from random import *


def swip(arr, K, P, M):
    n = len(arr)
    if K >= n or P >= n or K + M > n or P + M > n:
        raise ValueError("Некорректные индексы или длина массива")  # Ошибка
    temp = arr[K:K + M]
    for i in range(M):
        arr[K + i] = arr[P + i]
    for i in range(M):
        arr[P + i] = temp[i]
    return arr


n = int(input("Введите размерность массива: "))
arr = [randint(1, 100) for i in range(n)]
print("Исходный массив:", arr)
new_arr = swip(arr, 1, 5, 3)
print("Ответ:", new_arr)
