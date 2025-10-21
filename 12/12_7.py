k = 0
maxx = 1
for n in range(3, 10000):
    s = "4" + "0" * n
    while "000" in s or "40" in s or "100" in s:
        s = s.replace("000", "1", 1)

        s = s.replace("40", "0", 1)
        s = s.replace("100", "04", 1)
    sum_of_s = sum(map(int, s))
    if sum_of_s > maxx:
        maxx = sum_of_s
print(maxx)