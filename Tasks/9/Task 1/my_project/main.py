# Основний скрипт, що використовує обидва модулі
from module1 import get_info
from module2 import enhanced_greeting, circle_info


def main():
    # Використання module1 напряму
    print(get_info())
    print("-" * 40)

    # Використання module2, який імпортує з module1
    print(enhanced_greeting("Олена", 25))
    print("-" * 40)

    # Обчислення для кола
    radius = 5
    info = circle_info(radius)
    print(f"Коло з радіусом {radius}:")
    print(f"  Площа: {info['площа']:.2f}")
    print(f"  Довжина кола: {info['довжина_кола']:.2f}")


if __name__ == "__main__":
    main()