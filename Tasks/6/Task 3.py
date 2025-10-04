print("Task 3: Числа, що діляться на 7, але не кратні 5")
print("-" * 50)

# список чисел від 1 до 100
all_numbers = []
i = 1

while i <= 100:
    all_numbers.append(i)
    i += 1

print(f"Створено список від 1 до 100 (довжина: {len(all_numbers)})")

# окреслюю числа, що діляться на 7, але не кратні 5
result_list = []
i = 0

while i < len(all_numbers):
    number = all_numbers[i]
    # чек: чи ділиться на 7 І НЕ ділиться на 5
    if number % 7 == 0 and number % 5 != 0:
        result_list.append(number)
    i += 1

print(f"Числа, що діляться на 7, але не кратні 5:")
print(result_list)
print(f"Всього таких чисел: {len(result_list)}")