a = []
for x in '0123456789abcdefgh':
    s = int('77968' + x + '11', 18) + int('4' + x + '213', 18)
    if s % 7 == 0:
        print(s // 7)

b = []
for x in '0123456789abcde':
    s = int('9897' + x + '21', 15) + int('12' + x + '023', 15)
    if s % 14 == 0:
        print(s//14)