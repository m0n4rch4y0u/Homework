import fnmatch

for x in range(47, 10**10+1, 47):
    for y in range(len(x) - 1):
        if fnmatch.fnmatch(str(x), '9*4*0'):
            if x[y] > 