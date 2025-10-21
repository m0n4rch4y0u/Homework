from random import *


def generate_random_matrix(rows, cols):
    matrix = [[0] * cols for k in range(rows)]
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = randint(1, 100)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(f'{num:3}' for num in row))


def process_matrix(n, m, matrix):
    max_col_index = 0
    max_abs_sum = -1
    for j in range(m):
        abs_sum = sum(abs(matrix[i][j]) for i in range(n))
    if abs_sum > max_abs_sum:
        max_abs_sum = abs_sum
        max_col_index = j
    min_value = 10 ** 10
    for i in range(n):
        if matrix[i][max_col_index] < min_value:
            min_value = matrix[i][max_col_index]
    return min_value


n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))

random_matrix = generate_random_matrix(n, m)
print("Исходная матрица:")
print()
print_matrix(random_matrix)
print()
processed_matrix = process_matrix(n, m, random_matrix)
print("Ответ:", processed_matrix)
