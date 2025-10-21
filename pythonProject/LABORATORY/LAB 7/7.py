A = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
s = 0
n = 10
for i in range(0, n + 1):
    if A[n - i] - A[i] > A[i]:
        s = s + A[i]
print(s)