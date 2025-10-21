def win1(s):
    return s+2 >= 221 or s + 3 >= 221 or s * 2 >= 221
def loss1(s):
    return (not win1(s)) and win1(s+2) and win1(s+3) and win1(s*2)
def win2(s):
    return loss1(s+2) or loss1(s+3) or loss1(s*2)
def loss12(s):
    return win1(s+2) and win2(s+3) or win2(s+2) and win1(s + 3) or win1(s+3) and win2(s*2) or win2(s+3) and win1(s*2) or win1(s+2) and win2(s*2) or win2(s+2) and win1(s*2)

for s in range(1, 221):
    if loss1(s):
        print('19:', s)
    if win2(s):
        print('20:', s)
    if loss12(s):
        print('21:', s)
