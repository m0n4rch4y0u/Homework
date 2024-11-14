from random import *

n = int(input("Введите размерность массива: "))
k = int(input("Введите позиция начала удаления: "))
m = int(input("Введите кол-во элементов к удалению: "))

print()
array = [randint(0, 100) for i in range(n)]
print("Массив:", array)
print()
print("Ответ:", array[:k-1] + array[k+m-1:]) #массив начинается с 1
