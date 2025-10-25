# Task 3: Декоратор arg_rules - валідація аргументів

def arg_rules(type_: type, max_length: int, contains: list):
    """
    Декоратор для валідації аргументів функції

    Правила валідації:
    - type_: очікуваний тип аргументу
    - max_length: максимальна довжина аргументу
    - contains: список символів/підрядків, які повинен містити аргумент

    Якщо валідація не пройдена - повертає False та виводить причину
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            # Перевіряємо перший аргумент
            if not args:
                print("No arguments provided")
                return False

            first_arg = args[0]

            # Перевірка 1: Тип аргументу
            if not isinstance(first_arg, type_):
                print(f"Argument must be {type_.__name__}, got {type(first_arg).__name__}")
                return False

            # Перевірка 2: Довжина (для об'єктів, що мають довжину)
            if hasattr(first_arg, '__len__'):
                if len(first_arg) > max_length:
                    print(f"Argument length {len(first_arg)} exceeds maximum {max_length}")
                    return False

            # Перевірка 3: Наявність необхідних символів/підрядків
            if contains:
                missing_items = []
                for required in contains:
                    if required not in str(first_arg):
                        missing_items.append(required)

                if missing_items:
                    print(f"Argument must contain {missing_items}")
                    return False

            # Якщо всі перевірки пройдені, викликаємо оригінальну функцію
            return func(*args, **kwargs)

        return wrapper

    return decorator


# Тестування Task 3
@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan_v2(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print("\nTask 3 - Arg rules декоратор:")
print("Правила: type=str, max_length=15, contains=['05', '@']")

# Тест 1: довгий рядок (більше 15 символів)
print("\n Тест 1: 'johndoe05@gmail.com'")
print("  - Довжина: 19 символів (перевищує max_length=15)")
print("  - Містить '05': ✓")
print("  - Містить '@': ✓")
result1 = create_slogan_v2('johndoe05@gmail.com')
print(f"  Результат: {result1}")
assert create_slogan_v2('johndoe05@gmail.com') is False
print("Assertion пройдено (повернуто False через довжину)")

# Тест 2: коректний аргумент
print("\n📝 Тест 2: 'S@SH05'")
print("  - Довжина: 6 символів (< 15) ✓")
print("  - Містить '05': ✓")
print("  - Містить '@': ✓")
result2 = create_slogan_v2('S@SH05')
print(f"  Результат: {result2}")
assert create_slogan_v2('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
print("  ✅ Assertion пройдено (всі умови виконані)")

# Додаткові тести для перевірки
print("\n📝 Додаткові тести для перевірки роботи:")

print("\nТест 3: 'test' (не містить обов'язкових символів)")
result3 = create_slogan_v2('test')
print(f"Результат: {result3} (має бути False)")

print("\nТест 4: 'user@05' (містить всі символи, коротка довжина)")
result4 = create_slogan_v2('user@05')
print(f"Результат: {result4}")

print("\n" + "=" * 50)
print("ВСІ ЗАВДАННЯ ВИКОНАНІ УСПІШНО!")
print("=" * 50)


# Task 3 - комплексна перевірка
print("\n3. Arg rules декоратор (різні сценарії):")

@arg_rules(type_=str, max_length=10, contains=['#'])
def hashtag(tag):
    return f"Hashtag: {tag}"

print(f"   '#python' -> {hashtag('#python')}")
print(f"   'python' (без #) -> {hashtag('python')}")
print(f"   '#verylonghashtag' (>10) -> {hashtag('#verylonghashtag')}")