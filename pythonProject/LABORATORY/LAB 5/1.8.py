from random import *

random_numbers = []
numbers5 = []
for i in range(30):
    random_numbers.append(randint(1, 100))

for j in range(len(random_numbers)):
    if random_numbers[j] % 5 == 0:
        numbers5.append(random_numbers[j])

print("Список чисел кратных 5:")
for k, number in enumerate(numbers5, start=1):
    print(f"{k}. {number}")
