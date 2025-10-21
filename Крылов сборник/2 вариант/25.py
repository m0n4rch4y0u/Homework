from fnmatch import fnmatch

for x in range(12007, 10**10, 12007):
    if fnmatch(str(x), '9*?001?1'):
        print(x, x // 12007)