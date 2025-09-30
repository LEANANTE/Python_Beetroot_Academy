print("=== TASK 1: The Guessing Game ===")
import random

# випадкове число від 1 до 10
secret_number = random.randint(1, 10)

# Запитуємо користувача вгадати число
guess = int(input("Guess a number between 1 and 10: "))

# Перевіряємо відповідь
if guess == secret_number:
    print(f"Congratulations! You guessed it right! The number was {secret_number}")
else:
    print(f"Sorry, the number was {secret_number}. Better luck next time!")

print("\n")