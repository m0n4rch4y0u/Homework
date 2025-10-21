def task23(start, end):
    if start < end: return 0
    if start == end: return 1
    return task23(start - 1, end) + task23(start - 2, end) + task23(start // 3, end)


print(task23(16, 11) * task23(11, 6))
