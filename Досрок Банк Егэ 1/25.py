import fnmatch

for x in range(1779, 10**10+1, 1779):
    if fnmatch.fnmatch(str(x), '3?12?14*3'):
        print(x, x // 1779)