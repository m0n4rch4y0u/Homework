n = 103
x = 101
for i in range(x, 0, -2):
    n = i + (1 / n)
n = 1 / n
print(n)
