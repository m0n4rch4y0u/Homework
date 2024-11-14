from random import *

n = int(input("Введите размерность массива: "))
print()

arrayA = [randint(1, 100) for i in range(n)]
print("Массив А:", arrayA)

s = 0
for x in range(n):
    s += arrayA[x]
sred = s / len(arrayA)
print('Среднее арифметическое массива:', sred)
