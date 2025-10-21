import fnmatch

for x in range(157, 10**10+1, 157):
    if fnmatch.fnmatch(str(x), '1$3456%8'):
        print(x, x // 157)