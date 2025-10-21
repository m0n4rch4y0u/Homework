a = float(input("Введите а: "))
b = float(input("Введите b: "))
n = int(input("Введите n: "))
h = (b - a) / n
summ = 0
for i in range(1, n + 1):
    fi = (a + (i - 0.5) * h) / (1 + (a + (i - 0.5) * h) ** 2)
    summ += fi
print("Итоговое значение:", summ * h)
