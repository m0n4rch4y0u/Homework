def game(a, b, n):
    if a + b >= 62: return n % 2 == 0
    if n == 0: return 0
    g = [game(a + 5, b, n - 1), game(a, b + 5, n - 1), game(a * 2, b, n - 1), game(a, b * 2, n - 1)]
    return any(g) if (n - 1) % 2 == 0 else all(g)


print('19: ', [s for s in range(1, 61) if game(10, s, 2)])
print('20: ', [s for s in range(1, 61) if not game(10, s, 1) and game(10,s,3)])
print('21: ', [s for s in range(1, 61) if not game(10, s, 2) and game(10,s,4)])