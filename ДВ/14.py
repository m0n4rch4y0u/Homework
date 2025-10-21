s = 3 * 289**2024 + 81 * 49121 - 9 * 1681 - 6011
summ = 0
while s > 0:
    digit = s % 31
    if digit <= 17:
        summ += digit
    s //= 31
print(summ)
