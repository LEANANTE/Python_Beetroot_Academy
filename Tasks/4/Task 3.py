# Math Quiz Program
# Програма ставить математичне питання і перевіряє відповідь

print("TASK 3: Math Quiz")
print("-" * 40)

# Математичний вираз
question = "What is 15 + 27?"
correct_answer = 42

# Ставимо питання
print(f"Question: {question}")
user_answer = input("Your answer: ")

# Конвертуємо введення користувача в число
try:
    user_answer = int(user_answer)

    # Перевіряємо відповідь
    if user_answer == correct_answer:
        print("Correct! Well done!")
    else:
        print(f"Wrong! The correct answer is {correct_answer}")

except ValueError:
    print("Error! Please enter a valid number!")

# Додатковий приклад з іншим питанням
print("\n" + "-" * 40)
print("Bonus question:")

question2 = "What is 8 * 7?"
correct_answer2 = 56

print(f"Question: {question2}")
user_answer2 = input("Your answer: ")

try:
    user_answer2 = int(user_answer2)

    if user_answer2 == correct_answer2:
        print("Correct! You're good at math!")
    else:
        print(f"❌ Wrong! The correct answer is {correct_answer2}")

except ValueError:
    print("Error! Please enter a valid number!")