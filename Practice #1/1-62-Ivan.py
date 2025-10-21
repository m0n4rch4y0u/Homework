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

n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))

random_matrix = generate_random_matrix(n, m)
print("Матрица:")
print_matrix(random_matrix)

sum_abs_columns = [0] * m

for i in range(n):
    for j in range(m):
        sum_abs_columns[j] += abs(random_matrix[i][j])

max_sum_index = 0
for i in range(1, m):
    if sum_abs_columns[i] > sum_abs_columns[max_sum_index]:
        max_sum_index = i

max_element = -1
for i in range(n):
    if random_matrix[i][max_sum_index] > max_element:
        max_element = random_matrix[i][max_sum_index]

print("Ответ:", max_element)
