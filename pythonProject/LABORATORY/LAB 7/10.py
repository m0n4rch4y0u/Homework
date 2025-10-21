def count_males(text):
    male_count = 0
    for line in text:
        parts = line.split()
        gender = parts[-1].strip().lower()
        if gender == "муж":
            male_count += 1
    return male_count


text = []
with open("Анкеты.txt", encoding='UTF-8') as file:
    for line in file:
        text.append(line)

num_males = count_males(text)
print(f"Количество анкет лиц мужского пола: {num_males}")
