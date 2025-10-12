from math import *

# Ввод данных
x = float(input("Введите начало x (0-1): "))
step = float(input("Введите шаг: "))

# Проверка диапазона
if x < 0 or x > 1:
    print("x должен быть от 0 до 1")
    exit()

# Заголовок таблицы
print()
print("   x     |    y      | Производная")
print("---------|-----------|-------------")

# Вычисление и вывод
while x <= 1:
    y = sin(x)
    derivative = cos(x)
    print(f"{x:6.3f}   | {y:8.5f}  | {derivative:8.5f}")
    x += step