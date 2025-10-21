from random import *


def generate_random_matrix(rows, cols):
    matrix = [[0] * cols for k in range(rows)]
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = randint(-100, 100)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(f'{num:3}' for num in row))


def process_matrix(n, m, matrix):
    result = [[0] * (m + 1) for k in range(n + 1)]
    for i in range(n):
        for j in range(m): #Старые значения
            result[i][j] = matrix[i][j]
    for i in range(n):
        row_count_0 = sum(1 for x in matrix[i] if x < 0) #Строки
        result[i][m] = row_count_0
    for j in range(m):
        row_count_0 = sum(1 for k in range(n) if matrix[k][j] < 0) #Cтолбцы
        result[n][j] = row_count_0
    all_row_count_0 = sum(sum(1 for x in row if x < 0) for row in matrix) #Финальный элемент
    result[n][m] = all_row_count_0
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