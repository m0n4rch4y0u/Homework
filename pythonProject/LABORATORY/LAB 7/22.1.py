while True:
    surname = input("Введите фамилию (или введите 'q' для выхода): ").strip()
    if surname.lower() == 'q':
        break
    phone_number = input("Введите номер телефона: ").strip()
    with open("файл", 'a', encoding="utf-8") as file:
        file.write(surname + ',' + phone_number + '\n')
    print("Данные успешно записаны.")
print("Запись данных завершена.")

with open("файл", 'r', encoding='utf-8') as f:
    data = f.readlines()

phones_dict = {}
for line in data:
    parts = line.split(',')
    surname = parts[0]
    phone_number = parts[-1]
    prefix = phone_number[:3]
    if prefix not in phones_dict:
        phones_dict[prefix] = []
    phones_dict[prefix].append(phone_number)

found_matches = False

with open("ффайл", 'w', encoding='utf-8') as out_f:
    for prefix, numbers in phones_dict.items():
        if len(numbers) > 1:
            found_matches = True
            out_f.write(f'Номера с одинаковыми первыми тремя цифрами ({prefix}):\n')
            for number in numbers:
                out_f.write(number + '\n')

if not found_matches:
    print('Совпадений не найдено.')
else:
    print('Результат сохранён в файле: ффайл')
