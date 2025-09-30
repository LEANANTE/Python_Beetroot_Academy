print("=== TASK 3: Words Combination ===")

# Запит на вхідний рядок
input_string = input("Enter a word: ")

# 5 випадкових комбінацій
print(f"\n5 random combinations of '{input_string}':")
for i in range(5):
    # Перетворюємо рядок в список символів
    chars = list(input_string)
    # перемішуємо символи
    random.shuffle(chars)
    # з'єднуємо назад в рядок
    random_word = ''.join(chars)
    print(f"{i + 1}. {random_word}")