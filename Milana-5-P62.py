from random import *


def generate_random_matrix(rows, cols):
    matrix = [[0] * cols for k in range(rows)]
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = randint(1, 10)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(f'{num:3}' for num in row))


def process_matrix(n, m, matrix):
    result = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m): #Старые значения
            result[i][j] = matrix[i][j]
    for i in range(n):
        row_sum = sum(matrix[i])  # Cредние значения по строкам
        result[i][m] = row_sum / m
    for j in range(m):
        col_sum = sum(matrix[k][j] for k in range(n))  # Cредние значения по столбцам
        result[n][j] = col_sum / n
    all_sum = sum(sum(row) for row in matrix)  # Среднее значение последней ячейки
    result[n][m] = all_sum / (n * m)
    return result

n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))

random_matrix = generate_random_matrix(n, m)
print("Исходная матрица:")
print()
print_matrix(random_matrix)
print()
print("Итоговая матрица:")
print()
processed_matrix = process_matrix(n, m, random_matrix)
print_matrix(processed_matrix)