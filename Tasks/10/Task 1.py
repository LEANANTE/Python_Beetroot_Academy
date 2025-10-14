print("="*50)
print("TASK 1: Робота з IndexError та KeyError")
print("="*50)

def oops():
    """Функція, яка явно викликає IndexError"""
    raise IndexError("Oops! This is an IndexError")

def call_oops():
    """Функція, яка викликає oops() і перехоплює помилку"""
    try:
        print("Викликаємо функцію oops()...")
        oops()
    except IndexError as e:
        print(f"Перехоплено IndexError: {e}")
    except KeyError as e:
        print(f"Перехоплено KeyError: {e}")

# Тестуємо з IndexError
print("\n1. Тестування з IndexError:")
call_oops()

# Тепер змінимо oops на KeyError
def oops():
    """Функція змінена - тепер викликає KeyError"""
    raise KeyError("Oops! This is a KeyError")

print("\n2. Тестування з KeyError:")
call_oops()

# Що станеться, якщо перехоплюємо тільки IndexError?
def call_oops_index_only():
    """Перехоплює тільки IndexError"""
    try:
        print("Викликаємо функцію oops() (тільки IndexError обробляється)...")
        oops()
    except IndexError as e:
        print(f"Перехоплено IndexError: {e}")

print("\n3. Якщо перехоплюємо тільки IndexError, а викидається KeyError:")
try:
    call_oops_index_only()
except KeyError as e:
    print(f"KeyError не був оброблений всередині функції: {e}")