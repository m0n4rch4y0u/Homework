from random import *


def swip(arr):
    last_element = arr[-1]
    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = last_element
    return arr

n = int(input("Введите размерность массива: "))
array = [randint(-100, 100) for i in range(n)]
print("Исходный массив:", array)
new_array = swip(array)
print("Ответ:", new_array)
