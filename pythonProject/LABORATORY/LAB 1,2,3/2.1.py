x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))
if x > y:
    z = (y + 0.5) / (1 + x ** 2)
else:
    z = (x + 0.5) / (1 + y ** 2)
print("Итоговое значение z:", z)