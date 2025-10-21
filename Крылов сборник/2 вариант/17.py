a = [int(x) for x in open('17var02.txt')]
max100 = max([i for i in a if i % 1000 == 100])
maxx = 0
count = 0
for i in range(len(a) - 2):
    if ((len(str(a[i])) != 3 and len(str(a[i+1])) == 3 and len(str(a[i+2])) == 3) or (len(str(a[i])) == 3 and len(str(a[i+1])) == 3 and len(str(a[i+2])) != 3) or (len(str(a[i])) == 3 and len(str(a[i+1])) != 3 and len(str(a[i+2])) == 3)) and (a[i] + a[i+1] + a[i+2] <= max100):
        count += 1
        maxx = max(maxx,a[i] + a[i+1] + a[i+2])
print(count, maxx)

