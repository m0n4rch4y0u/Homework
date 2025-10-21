f = open('24var05.txt')
s = f.readline()
a = [''] + s.split('A') + ['']
cnt = []
for i in range(len(a) - 3):
    cnt.append(len(a[i] + 'A' + a[i + 1] + 'A' + a[i + 2] + 'A' + a[i + 3]))
print(max(cnt))
