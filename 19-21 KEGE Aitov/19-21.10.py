def win1(s):
    return (s + 1 >= 99 and s + 1 <= 131) or (s + 2 >= 99 and s + 2 <= 131) or (s * 3 >= 99 and s * 3 <= 131)


def loss1(s):
    return (not win1(s)) and win1(s + 1) and win1(s + 2) and win1(s * 3)


for s in range(1, 99):
    if loss1(s):
        print(s)
