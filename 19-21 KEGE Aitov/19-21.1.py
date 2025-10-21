def WIN1(s):
    return s + 1 >= 141 or s * 2 >= 141


def LOSS1(s):
    return (not WIN1(s)) and WIN1(s + 1) and WIN1(s * 2)


def WIN2(s):
    return LOSS1(s + 1) or LOSS1(s * 2)


def LOSS12(s):
    return WIN1(s + 1) and WIN2(s * 2) or WIN2(s + 1) and WIN1(s * 2)


for s in range(1, 141):
    if LOSS1(s):
        print('19:', s)
    if WIN2(s):
        print('20:', s)
    if LOSS12(s):
        print('21:', s)
