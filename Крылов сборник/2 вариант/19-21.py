def game(s, n):
    if s >= 223: return n % 2 == 0
    if n == 0: return 0
    h = [game(s + 1, n - 1), game(s + 4, n - 1), game(s * 3, n - 1)]
    return any(h) if n % 2 != 0 else all(h)


print('19)', [s for s in range(1, 223) if game(s, 2)])
print('20)', [s for s in range(1, 223) if not(game(s, 1)) and game(s, 3)])
print('21)', [s for s in range(1, 223) if not(game(s, 2)) and game(s,4)])