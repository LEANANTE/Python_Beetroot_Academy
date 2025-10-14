#!/usr/bin/env python3
"""
mymod.py - Модуль Python, подібний до Unix утиліти wc
Підраховує рядки та символи у файлах.
"""

import os
import sys


def count_lines(name):
    """
    Підраховує кількість рядків у файлі.

    Параметри:
        name: str - ім'я файлу або файловий об'єкт

    Повертає:
        int - кількість рядків у файлі
    """
    # Обробляємо як рядок з ім'ям файлу, так і файловий об'єкт
    if isinstance(name, str):
        with open(name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return len(lines)
    else:
        # Припускаємо, що це файловий об'єкт
        current_pos = name.tell()  # Зберігаємо поточну позицію
        name.seek(0)  # Повертаємось на початок
        lines = name.readlines()
        name.seek(current_pos)  # Відновлюємо позицію
        return len(lines)


def count_chars(name):
    """
    Підраховує кількість символів у файлі.

    Параметри:
        name: str - ім'я файлу або файловий об'єкт

    Повертає:
        int - кількість символів у файлі
    """
    # Обробляємо як рядок з ім'ям файлу, так і файловий об'єкт
    if isinstance(name, str):
        with open(name, 'r', encoding='utf-8') as file:
            content = file.read()
            return len(content)
    else:
        # Припускаємо, що це файловий об'єкт
        current_pos = name.tell()  # Зберігаємо поточну позицію
        name.seek(0)  # Повертаємось на початок
        content = name.read()
        name.seek(current_pos)  # Відновлюємо позицію
        return len(content)


def test(name):
    """
    Тестова функція, яка викликає обидві функції підрахунку.

    Параметри:
        name: str - ім'я файлу для аналізу

    Виводить статистику про файл.
    """
    print(f"\nСтатистика файлу: {name}")
    print("-" * 40)

    # Перевіряємо, чи існує файл
    if isinstance(name, str) and not os.path.exists(name):
        print(f"Помилка: Файл '{name}' не знайдено!")
        return

    try:
        # Базова версія - відкриває файл двічі
        lines = count_lines(name)
        chars = count_chars(name)

        print(f"Рядків: {lines}")
        print(f"Символів: {chars}")

        # Обчислюємо середню кількість символів на рядок
        if lines > 0:
            avg_chars = chars / lines
            print(f"Середнє символів/рядок: {avg_chars:.1f}")

    except Exception as e:
        print(f"Помилка читання файлу: {e}")


def test_optimized(name):
    """
    Оптимізована версія, що відкриває файл лише один раз.

    Параметри:
        name: str - ім'я файлу для аналізу
    """
    print(f"\nСтатистика файлу (оптимізована) для: {name}")
    print("-" * 40)

    if not os.path.exists(name):
        print(f"Помилка: Файл '{name}' не знайдено!")
        return

    try:
        with open(name, 'r', encoding='utf-8') as file:
            lines = count_lines(file)
            file.seek(0)  # Повертаємось на початок файлу
            chars = count_chars(file)

        print(f"Рядків: {lines}")
        print(f"Символів: {chars}")

        if lines > 0:
            avg_chars = chars / lines
            print(f"Середнє символів/рядок: {avg_chars:.1f}")

    except Exception as e:
        print(f"Помилка читання файлу: {e}")


def wc(name, show_words=False):
    """
    Розширена функція, подібна до Unix команди wc.

    Параметри:
        name: str - ім'я файлу для аналізу
        show_words: bool - чи підраховувати слова

    Повертає:
        dict з підрахунками
    """
    stats = {'рядки': 0, 'слова': 0, 'символи': 0, 'байти': 0}

    if not os.path.exists(name):
        print(f"Помилка: Файл '{name}' не знайдено!")
        return stats

    try:
        with open(name, 'r', encoding='utf-8') as file:
            for line in file:
                stats['рядки'] += 1
                stats['символи'] += len(line)
                if show_words:
                    stats['слова'] += len(line.split())

        # Отримуємо розмір у байтах
        stats['байти'] = os.path.getsize(name)

        return stats

    except Exception as e:
        print(f"Помилка: {e}")
        return stats


# Секція інтерактивного тестування
def main():
    """Головна функція для тестування модуля"""
    print("\n" + "=" * 50)
    print("mymod.py - Тестування модуля")
    print("=" * 50)

    # Тестуємо на самому модулі
    module_file = __file__ if __file__ else "mymod.py"

    print("\n1. Тестування базових функцій на самому модулі:")
    test(module_file)

    print("\n2. Тестування оптимізованої версії:")
    test_optimized(module_file)

    print("\n3. Тестування розширеної функції wc:")
    stats = wc(module_file, show_words=True)
    print(f"\nПовна статистика для: {module_file}")
    print("-" * 40)
    for key, value in stats.items():
        print(f"{key.capitalize()}: {value}")

    # Створюємо тестовий файл
    test_filename = "тестовий_файл.txt"
    with open(test_filename, 'w', encoding='utf-8') as f:
        f.write("Рядок 1: Привіт, Світе!\n")
        f.write("Рядок 2: Модулі Python чудові.\n")
        f.write("Рядок 3: Тестуємо файлові операції.\n")

    print(f"\n4. Тестування на прикладі файлу '{test_filename}':")
    test(test_filename)

    # Прибирання
    if os.path.exists(test_filename):
        os.remove(test_filename)
        print(f"\n(Прибрано: видалено {test_filename})")

    # Інформація про PYTHONPATH
    print("\n" + "=" * 50)
    print("Інформація про PYTHONPATH:")
    print("=" * 50)
    print(f"Поточний каталог: {os.getcwd()}")
    print(f"Каталог модуля: {os.path.dirname(os.path.abspath(__file__))}")
    print("\nЧи потрібен PYTHONPATH:")
    print("- Якщо mymod.py в поточному каталозі: НІ")
    print("- Якщо mymod.py в sys.path Python: НІ")
    print("- Якщо mymod.py деінде: ТАК, додайте до PYTHONPATH")


if __name__ == "__main__":
    # Запускаємо тести, коли модуль виконується напряму
    main()
else:
    # Модуль імпортується
    print(f"Модуль 'mymod' успішно імпортовано з: {__file__}")
    print("Доступні функції: count_lines(), count_chars(), test(), test_optimized(), wc()")