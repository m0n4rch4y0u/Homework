def game(a, b, n):
    if a + b >= 68: return n % 2 == 0
    if n == 0: return 0
    g = [game(a + 2, b, n - 1), game(a, b + 2, n - 1), game(a * 3, b, n - 1), game(a, b * 3, n - 1)]
    return any(g) if n % 2 != 0 else all(g)


print('19: ', [s for s in range(1, 59) if game(8, s, 1)])
print('19: ', [s for s in range(1, 59) if game(8, s, 2)])
print('20: ', [s for s in range(1, 59) if not game(8, s, 1) and game(11, s, 3)])
# print('21: ', [s for s in range(1, 59) if not game(8, s, 2) and game(11,s,4)])
print('21: ', [s for s in range(1, 59) if game(8, s, 2) or game(8, s, 4)])
