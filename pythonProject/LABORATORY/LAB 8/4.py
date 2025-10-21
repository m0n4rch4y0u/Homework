def find_longest_line(text):
    longest_line = ""
    with open(text, 'r', encoding='utf-8') as file:
        for line in file:
            stripped_line = line.rstrip()
            if len(stripped_line) > len(longest_line):
                longest_line = stripped_line
    return longest_line
longest = find_longest_line('text')
if longest is not None:
    print("Самая длинная строка:", longest)
