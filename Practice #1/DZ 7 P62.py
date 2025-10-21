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
    total_sum = sum(sum(row) for row in matrix)
    result = []
    for i in range(n):
        row_sum = sum(matrix[i])
        new_row = matrix[i].copy()
        if total_sum == 0:
            new_row.append(0)
        else:
            new_row.append(f'{(row_sum / total_sum * 100):.0f}'+'%')
        result.append(new_row)
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
