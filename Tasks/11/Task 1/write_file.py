#!/usr/bin/env python3
"""
Скрипт для створення файлу myfile.txt та запису тексту в нього
"""

# Створюємо та відкриваємо файл для запису
with open("myfile.txt", "w") as file:
    # Записуємо рядок з символом нового рядка в кінці
    file.write("Hello file world!\n")

print("Файл 'myfile.txt' створено успішно!")