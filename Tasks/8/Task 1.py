# Проста функція для виведення улюбленого фільму

def favorite_movie(name):
    """
    Приймає назву улюбленого фільму та виводить повідомлення.

    Parameters:
    name (str): Назва фільму
    """
    print(f"My favorite movie is named {name}")


# тестую Task 1
print("=" * 50)
print("TASK 1 - Улюблений фільм")
print("=" * 50)
favorite_movie("The Matrix")
favorite_movie("Interstellar")
favorite_movie("The Lord of the Rings")
print()