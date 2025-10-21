f = open('24_досрок2_2024.txt.txt')
s = f.readline()
s = s.replace('O', 'N')
s = s.replace('P', 'N')
s = s.replace('NN', 'N N')
s = s.replace('NN', 'N N')
s = s.split()
maxs = 0
for i in range(len(s)):
    maxs = max(len(s[i]), maxs)
print(maxs)
