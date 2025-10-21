def success(a):
    k = str(a)
    if int(k[0]) + int(k[1]) + int(k[2]) == int(k[3]) + int(k[4]) + int(k[5]):
        return 1
    else:
        return 0
A = []
k = 0
while True:
    a = input("Введите 6-ти значное число (или введите 'q' для выхода): ")
    if a.lower() == 'q':
        break
    A.append(a)
for i in range(len(A)):
    if success(A[i]) == 1:
        k += 1
print(k)
