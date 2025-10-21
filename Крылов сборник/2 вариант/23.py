def task23(start, end):
    if start > end or start == 18:
        return 0
    if start == end:
        return 1
    if start < end:
        return task23(start + 1, end) + task23(start + 4, end) + task23(start * 2, end)


print(task23(4, 11) * task23(11, 28))
