n = int(input("Введите значение n: "))
an = 1
k = 1
for i in range(1, n + 1):
    an = k * an + (1 / k)
    k += 1
    print(f'a[{i}]:', an)
