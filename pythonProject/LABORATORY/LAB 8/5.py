def remove_consecutive_duplicates(input_string):
    if len(input_string) <= 1:
        return input_string
    result = input_string[0]
    for char in input_string[1:]:
        if char != result[-1]:
            result += char
    return result


test_str = "aaarrrttt"
new_str = remove_consecutive_duplicates(test_str)
print(new_str)
