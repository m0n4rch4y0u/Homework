import fnmatch

for x in range(137, 10 ** 9, 137):
    if fnmatch.fnmatch(str(x), '1234*7?8'):
        print(x, x // 137)
