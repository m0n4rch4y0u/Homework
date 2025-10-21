from fnmatch import fnmatch

for x in range(149, 10**8, 149):
    if fnmatch(str(x), '11*223'):
        print(x, x // 149)