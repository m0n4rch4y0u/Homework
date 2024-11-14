from random import *


def generate_random_matrix(rows, cols):
    matrix = [[0] * cols for k in range(rows)]
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = randint(0, 1)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(f'{num:3}' for num in row))  # 3 означает ширину поля для вывода числа.


def process_matrix(n, m, matrix, l, k):
    zeros_count = 0
    for i in range(l):
        for j in range(m):
            if matrix[i][j] == 0:
                zeros_count += 1
    for i in range(l, n):
        for j in range(k):
            if matrix[i][j] == 0:
                zeros_count += 1

    return zeros_count


n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))
l = int(input("Введите количество верхних L строк: "))
k = int(input("Введите количество левых K столбцов: "))

random_matrix = generate_random_matrix(n, m)
print("Исходная матрица:")
print()
print_matrix(random_matrix)
print()
print("Ответ:")
print()
processed_matrix = process_matrix(n, m, random_matrix, l, k)
print(processed_matrix)
