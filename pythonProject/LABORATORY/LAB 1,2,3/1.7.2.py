from math import *

s = 0
k = 0
x = 1
while x > 0.5 * 10 ** -4:
    x = ((-1) ** k) / factorial(2 * k)
    k += 1
    s += x
print(s)