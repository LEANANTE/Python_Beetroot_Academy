import random
print("Task 2: Спільні числа без дублікатів")
print("-" * 50)

# буде генеруватись перший список
list1 = []
i = 0
# тоді
while i < 10:
    random_number = random.randint(1, 10)
    list1.append(random_number)
    i += 1

print(f"Перший список: {list1}")

# буде генеруватись другий список
list2 = []
i = 0

while i < 10:
    random_number = random.randint(1, 10)
    list2.append(random_number)
    i += 1

print(f"Другий список: {list2}")

# Знайдемо спільні числа без дублікатів
common_numbers = []
i = 0

while i < len(list1):
    j = 0
    while j < len(list2):
        # якщо знайшли спільне число і його ще немає в результаті
        if list1[i] == list2[j] and list1[i] not in common_numbers:
            common_numbers.append(list1[i])
            break  # звертаємось до наступного числа з list1
        j += 1
    i += 1

# сортуємо
common_numbers.sort()
print(f"Спільні числа без дублікатів: {common_numbers}")
print()