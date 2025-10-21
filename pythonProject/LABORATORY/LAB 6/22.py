q = [1.5, 2, 3.1, 4.2, 6, 7.5, 8.3, 9]
s = int(input("Введите вводимое значение: "))
q.pop(4)
qc = []
for i in range(len(q)):
    if i == 4:
        qc.append(s)
    qc.append(q[i])
print("Итоговый список:", qc)
