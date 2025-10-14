#!/usr/bin/env python3
"""
Дослідження модифікації sys.path та її впливу на імпорт модулів
"""

import sys
import os


def explore_sys_path():
    """Інтерактивне дослідження sys.path"""

    print("=" * 60)
    print("ДОСЛІДЖЕННЯ sys.path")
    print("=" * 60)

    # 1. Відображення початкового sys.path
    print("\n1. Початковий sys.path:")
    for i, path in enumerate(sys.path):
        print(f"   [{i}] {path}")

    # 2. Перевірка можливості модифікації sys.path
    print("\n2. Чи можна модифікувати sys.path? Давайте перевіримо...")

    # Додаємо новий каталог до sys.path
    new_dir = "/tmp/мої_кастомні_модулі"
    print(f"   Додаємо: {new_dir}")
    sys.path.append(new_dir)

    # Перевіряємо, чи додалося
    print("\n   Оновлений sys.path (останні 3 записи):")
    for path in sys.path[-3:]:
        print(f"   ... {path}")

    # 3. Тестуємо, чи впливає модифікація на імпорт
    print("\n3. Тестуємо, чи впливає модифікація на імпорт модулів...")

    # Створюємо тимчасовий тестовий каталог і модуль
    test_dir = os.path.expanduser("~/temp_python_test")
    test_module_path = os.path.join(test_dir, "test_module.py")

    # Створюємо каталог, якщо не існує
    os.makedirs(test_dir, exist_ok=True)

    # Створюємо тестовий модуль
    with open(test_module_path, 'w') as f:
        f.write('''
def hello():
    return "Привіт з динамічно доданого модуля!"

MODULE_VERSION = "1.0"
''')

    print(f"   Створено тестовий модуль у: {test_module_path}")

    # Спробуємо імпортувати ДО додавання до sys.path
    print("\n   Спробуємо імпортувати test_module ДО додавання до sys.path...")
    try:
        import test_module
        print("   Імпорт успішний (модуль вже був доступний)")
    except ImportError:
        print("   ImportError - модуль не знайдено (як і очікувалось)")

    # Додаємо каталог до sys.path
    print(f"\n   Додаємо {test_dir} до sys.path...")
    sys.path.insert(0, test_dir)  # Вставляємо на початок для пріоритету

    # Спробуємо імпортувати ПІСЛЯ додавання до sys.path
    print("   Спробуємо імпортувати test_module ПІСЛЯ додавання до sys.path...")
    try:
        import test_module
        print(f"   Імпорт успішний!")
        print(f"   Версія модуля: {test_module.MODULE_VERSION}")
        print(f"   Результат функції: {test_module.hello()}")
    except ImportError as e:
        print(f"   ImportError: {e}")

    # 4. Інші операції з sys.path
    print("\n4. Інші операції з sys.path:")

    # Вставка в конкретну позицію
    sys.path.insert(1, "/інший/кастомний/шлях")
    print("   Можна вставляти в конкретні позиції")

    # Видалення шляхів
    if "/інший/кастомний/шлях" in sys.path:
        sys.path.remove("/інший/кастомний/шлях")
        print("   Можна видаляти конкретні шляхи")

    # Модифікація існуючих записів
    original = sys.path[0]
    sys.path[0] = "/модифікований/шлях"
    print("   Можна модифікувати існуючі записи")
    sys.path[0] = original  # Відновлюємо

    # 5. Зв'язок зі змінною середовища
    print("\n5. Змінна середовища PYTHONPATH:")
    pythonpath = os.environ.get('PYTHONPATH', 'Не встановлено')
    print(f"   Поточний PYTHONPATH: {pythonpath}")

    if pythonpath != 'Не встановлено':
        print("   Каталоги PYTHONPATH у sys.path:")
        for path in pythonpath.split(os.pathsep):
            if path in sys.path:
                print(f"   ✓ {path}")

    # Прибирання
    print("\n6. Прибирання:")
    if os.path.exists(test_module_path):
        os.remove(test_module_path)
        print(f"   Видалено: {test_module_path}")
    if os.path.exists(test_dir):
        os.rmdir(test_dir)
        print(f"   Видалено: {test_dir}")

    print("\n" + "=" * 60)
    print("ВИСНОВКИ:")
    print("=" * 60)
    print("""
1. ТАК, sys.path можна модифікувати з Python
2. ТАК, модифікації впливають на те, де Python шукає модулі
3. Зміни тимчасові (лише для поточної сесії Python)
4. Підтримувані операції:
   - append() - додати в кінець
   - insert() - додати в конкретну позицію
   - remove() - видалити конкретний шлях
   - Пряма модифікація через індекс
5. Змінна середовища PYTHONPATH ініціалізує sys.path,
   але не обмежує модифікації під час виконання
""")


if __name__ == "__main__":
    explore_sys_path()