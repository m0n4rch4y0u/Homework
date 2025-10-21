import fnmatch

for x in range(2025, 10**9+1, 2025):
    if fnmatch.fnmatch(str(x), '1?31*437?'):
        print(x, x // 2025)