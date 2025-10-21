import fnmatch

for x in range(143, 10**9+1, 143):
    if fnmatch.fnmatch(str(x), '131*131?'):
        print(x, x // 143)