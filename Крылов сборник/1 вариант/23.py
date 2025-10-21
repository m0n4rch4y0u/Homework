def task23(start, end):
    if start > end or start == 11 or start == 17:
        return 0
    if start == end:
        return 1
    if start < end:
        return task23(start + 1, end) + task23(start + 4, end) + task23(start * 2, end)


print(task23(3, 24))
