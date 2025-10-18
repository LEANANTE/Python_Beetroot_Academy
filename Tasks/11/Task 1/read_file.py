#!/usr/bin/env python3
"""
Скрипт для читання та виведення вмісту файлу myfile.txt
"""

try:
    # Відкриваємо файл для читання
    with open("myfile.txt", "r") as file:
        # Читаємо весь вміст файлу
        contents = file.read()

    # Виводимо вміст на екран
    print("Вміст файлу 'myfile.txt':")
    print(contents)

except FileNotFoundError:
    print("Помилка: Файл 'myfile.txt' не знайдено!")
    print("Спочатку запустіть write_file.py для створення файлу.")