for a in range(-10000, 10000):
    if all((4 * x + y < a) or (x < y) or (22 <= x) for x in range(0, 100) for y in range(0,100)):
        print(a)
        break
