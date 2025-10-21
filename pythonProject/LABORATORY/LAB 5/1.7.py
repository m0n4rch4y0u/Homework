from random import *

X = []
Y = []
n = int(input("Введите кол-во элементов массива: "))
for i in range(n):
    X.append(randint(1, 100))
for k in range(len(X)):
    for j in X:
        y = X[k:n]
    Y.append(sum(y))

print("Массив X:")
for k, number in enumerate(X, start=1):
    print(f"{k}. {number}")
print("Массив Y:")
for k, number in enumerate(Y, start=1):
    print(f"{k}. {number}")
