N = int(input("Введите значение N: "))
summ = 0
N1 = 1.1
for i in range(1, N + 1):
    summ += (-1 * N1) * (-1) ** i
    N1 += 0.1
print("Итоговая сумма:", summ)
