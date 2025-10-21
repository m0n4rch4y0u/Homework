print('x y z')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
                f1 = not(z) and x or x and y
                if f1 == 1:
                    print(x, y, z)
