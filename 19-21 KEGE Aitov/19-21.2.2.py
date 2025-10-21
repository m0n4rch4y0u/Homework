from functools import lru_cache


def moves(s):
    return s + 1, s + 2, s * 3


@lru_cache
def game(s):
    if any(x >= 131 for x in moves(s)): return 'win1'
    if all(game(x) == 'win1' for x in moves(s)): return 'loss1'
    if any(game(x) == 'loss1' for x in moves(s)): return 'win2'
    if any(game(x) == 'win2' for x in moves(s)): return 'loss12'


for s in range(1, 131):
    if game(s) == 'loss1':
        print('19: ', s)
    if game(s) == 'win2':
        print('20: ', s)
    if game(s) == 'loss12':
        print('21: ', s)
