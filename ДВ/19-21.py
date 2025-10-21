def game(s, n):
    if s >= 129: return n % 2 == 0
    if n == 0: return 0
    g = [game(s + 1, n-1), game(s * 2, n-1)]
    return any(g) if n % 2 != 0 else all(g)


print('19)', [s for s in range(1, 129) if game(s, 2)])
print('20)', [s for s in range(1, 129) if not (game(s, 1)) and game(s, 3)])
print('21)', [s for s in range(1, 129) if not (game(s, 2)) and game(s, 4)])
