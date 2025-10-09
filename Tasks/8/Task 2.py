# Функція для створення словника з назвою країни та столицею

def make_country(name, capital):
    """
    Створює словник з назвою країни та її столицею.

    Parameters:
    name (str): Назва країни
    capital (str): Назва столиці

    Returns:
    dict: Словник з ключами 'name' та 'capital'
    """
    country_dict = {
        'name': name,
        'capital': capital
    }

    # виводимо значення словника
    print(f"Country name: {country_dict['name']}")
    print(f"Country capital: {country_dict['capital']}")
    print(f"Full dictionary: {country_dict}")

    return country_dict


# Тестування Task 2
print("=" * 50)
print("TASK 2 - Створення словника країни")
print("=" * 50)
ukraine = make_country("Ukraine", "Kyiv")
print()
france = make_country("France", "Paris")
print()
japan = make_country("Japan", "Tokyo")
print()