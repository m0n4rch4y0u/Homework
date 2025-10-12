# Ввод данных
N = int(input("Введите натуральное число N: "))

# 1) Сколько цифр в числе?
digits = str(N)
num_digits = len(digits)
print(f"1) Количество цифр: {num_digits}")

# 2) Сумма цифр числа
sum_digits = sum(int(digit) for digit in digits)
print(f"2) Сумма цифр: {sum_digits}")

# 3) Входит ли "3" в число?
digit_3 = '3' in digits
print(f"3) Есть ли цифра 3: {'да' if digit_3 else 'нет'}")

# 4) Обратный порядок цифр
reversed_number = int(digits[::-1])
print(f"4) Число в обратном порядке: {reversed_number}")

# 5) Поменять первую и последнюю цифру
if num_digits > 1:
    first_digit = digits[0]
    last_digit = digits[-1]
    middle = digits[1:-1]
    swapped = int(last_digit + middle + first_digit)
else:
    swapped = N
print(f"5) Первая и последняя цифра поменяны: {swapped}")

# 6) Сколько раз встречается 0?
zero_count = digits.count('0')
print(f"6) Количество нулей: {zero_count}")

# 7) Сумма квадратов цифр больше числа?
sum_squares = sum(int(digit)**2 for digit in digits)
result = sum_squares > N
print(f"7) Сумма квадратов цифр ({sum_squares}) больше числа {N}: {'да' if result else 'нет'}")