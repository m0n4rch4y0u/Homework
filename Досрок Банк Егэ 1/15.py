for a in range(1,1000):
    for x in range(1, 1000):
        if ((x % a != 0) <= ((x % 14 == 0) <= (x % 4 != 0))) == 0:
            break
    else:
        print(a)