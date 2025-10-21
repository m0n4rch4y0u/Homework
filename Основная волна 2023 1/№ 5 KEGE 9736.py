results = []
for n in range(1, 171):
    b = bin(n)[2:]
    if n % 3 == 0:
        b = b + b[-3:]
    else:
        b = b + bin(3 * (n % 3))[2:]
    r = int(b, 2)
    if r <= 170:
        results.append(r)
print(max(results))
