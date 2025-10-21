from math import *
k = 0
for x in range(1, 1000000):
    a1 = 5 * x ** 4 + 5 * x ** 3 + 1 * x ** 2 + 1 * x ** 1 + 3 * x ** 0
    a2 = 7 * 80 ** 3 + x * 80 ** 2 + x * 80 ** 2 + 5 * 80 ** 0
    n = abs(a2 - a1)
    if n <= 10**6:
        k += 1
print(k)