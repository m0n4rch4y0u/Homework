def task23(start, end):
    if start < end: return 0
    if start == end: return 1
    return task23(start - 2, end) + task23(start // 2, end)


print(task23(30, 14) * task23(14, 1))
