a = int(input("Введите а: "))
b = int(input("Введите b: "))
n = int(input("Введите n: "))
summ = 0
for i in range(1, n + 1):
    xi = a * b - i
    if xi > 0:
        summ += xi
print("Сумма положительных элементов", summ)
