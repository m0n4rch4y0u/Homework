for a in range(-10000, 10000):
    if all(((x ** 2 + y ** 2 > 128) or (y < -1 * x + a)) for x in range(0, 150) for y in range(0, 150)):
        print(a)
        break
