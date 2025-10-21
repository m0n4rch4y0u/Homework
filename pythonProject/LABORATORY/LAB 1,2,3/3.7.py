x = int(input("Введите натуральное число: "))
summ = 0
count = 0
while x != 0:
    x0 = x % 10
    if x0 % 2 == 0:
        summ += x0
        count += 1
    x0 = 0
    x = x // 10
print("Среднее арифмитическая четных цифр:", summ / count)
