import random
print("Task 1: Знаходження найбільшого числа")
print("-" * 50)

# буде створюватись порожній список
numbers = []
i = 0

# 10 випадкових чисел
while i < 10:
# генерація випадкове число від 1 до 100
    random_number = random.randint(1, 100)
    numbers.append(random_number)
    i += 1

print(f"Згенерований список: {numbers}")

# Шукаємо найбільше число
max_number = numbers[0]  # нехай буде що перше число - найбільше
i = 1
# тоді
while i < len(numbers):
    if numbers[i] > max_number:
        max_number = numbers[i]
    i += 1

print(f"Найбільше число: {max_number}")
print()