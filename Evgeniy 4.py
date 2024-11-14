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
    min_val = 10 ** 10
    for row in matrix:
        avg = sum(row) / m
        if min_val == 10 ** 10 or avg < min_val:
            min_val = avg

    return min_val


n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))

random_matrix = generate_random_matrix(n, m)
print("Исходная матрица:")
print()
print_matrix(random_matrix)
print()
processed_matrix = process_matrix(n, m, random_matrix)
print("Ответ:", processed_matrix)
