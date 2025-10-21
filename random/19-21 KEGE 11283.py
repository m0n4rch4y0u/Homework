def game(a, b, n):
    if a + b >= 342: return n % 2 == 0
    if n == 0: return 0
    g = [game(a + 2, b, n - 1), game(a, b + 2, n - 1), game(a * 5, b, n - 1), game(a, b * 5, n - 1)]
    return any(g) if (n - 1) % 2 == 0 else all(g)


print('19: ', [s for s in range(1, 326) if game(11, s, 2)])
print('20: ', [s for s in range(1, 326) if not game(11, s, 1) and game(11,s,3)])
print('21: ', [s for s in range(1, 326) if not game(11, s, 2) and game(11,s,4)])

