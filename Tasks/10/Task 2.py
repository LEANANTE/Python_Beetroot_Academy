print("\n" + "=" * 50)
print("TASK 2: Обчислення a²/b з обробкою винятків")
print("=" * 50)


def calculate_squared_divided():
    """
    Функція приймає два числа від користувача
    і повертає квадрат a поділений на b
    """
    try:
        # Отримуємо введення від користувача
        a = input("\nВведіть число a: ")
        b = input("Введіть число b: ")

        # Намагаємося перетворити на числа
        a = float(a)
        b = float(b)

        # Обчислюємо результат
        result = (a ** 2) / b

        return result

    except ValueError:
        # Якщо введені значення не є числами
        print("Помилка: Введені значення повинні бути числами!")
        return None

    except ZeroDivisionError:
        # Якщо b дорівнює нулю
        print("Помилка: Неможливо ділити на нуль!")
        return None

    except Exception as e:
        # Для інших непередбачених помилок
        print(f"Несподівана помилка: {e}")
        return None


# Покращена версія з повторними спробами
def calculate_with_retry():
    """Версія з можливістю повторних спроб"""
    while True:
        try:
            print("\n--- Калькулятор a²/b ---")
            a_str = input("Введіть число a: ")
            b_str = input("Введіть число b: ")

            # Перетворюємо на числа
            a = float(a_str)
            b = float(b_str)

            # Перевіряємо ділення на нуль до обчислення
            if b == 0:
                raise ZeroDivisionError("b не може дорівнювати нулю")

            # Обчислюємо результат
            result = (a ** 2) / b

            print(f"\n Результат: {a}² / {b} = {result}")
            return result

        except ValueError:
            print(
                f" Помилка: '{a_str if 'a_str' in locals() else '?'}' або '{b_str if 'b_str' in locals() else '?'}' не є числом!")

        except ZeroDivisionError as e:
            print(f" Помилка: {e}")

        except KeyboardInterrupt:
            print("\n\nВихід з програми...")
            return None

        except Exception as e:
            print(f" Несподівана помилка: {e}")

        # Питаємо чи спробувати ще раз
        retry = input("\nСпробувати ще раз? (так/ні): ").lower()
        if retry not in ['так', 'yes', 'y', 'т']:
            print("Завершення програми.")
            return None


# Демонстрація роботи
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("ДЕМОНСТРАЦІЯ TASK 2")
    print("=" * 50)

    # Тестові сценарії для демонстрації
    print("\nПриклади тестових сценаріїв:")
    print("1. Нормальний випадок: a=4, b=2 → 4²/2 = 8")
    print("2. Ділення на нуль: a=5, b=0 → Помилка")
    print("3. Нечислові значення: a='text', b=2 → Помилка")

    # Викликаємо основну функцію
    print("\nЗапуск основної функції:")
    result = calculate_squared_divided()
    if result is not None:
        print(f"Результат: {result}")