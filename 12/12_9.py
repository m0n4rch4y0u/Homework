maxx_in_s = 30
k = 0
for x in range(1, 40):
    for y in range(1, 40):
        for z in range(1, 40):
            s = '/' * z + '$' * y + '@' * x
            while '@$' in s or '/@' in s or '/$' in s:
                if '@$' in s:
                    s = s.replace('@$', '$@', 1)
                if '/@' in s:
                    s = s.replace('/@', '@/', 1)
                if '/$' in s:
                    s = s.replace('/$', '$/', 1)
            if x + y + z > maxx_in_s and s[29] == '@':
                maxx_in_s = x + y + z
print(maxx_in_s)
