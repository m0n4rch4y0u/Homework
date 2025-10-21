s = []
for a in range(1,10000):
        if all(((x % 13 == 0) <= (not(x % 21 == 0))) or (x+a >= 500) for x in range(1,10000)):
            print(a)
            break
