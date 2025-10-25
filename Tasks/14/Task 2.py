# Task 2: Декоратор stop_words - замінює заборонені слова на *

def stop_words(words: list):
    """
    Декоратор, який замінює вказані слова на * в результаті функції

    Args:
        words: список слів для заміни (без врахування регістру)
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            # Викликаємо оригінальну функцію
            result = func(*args, **kwargs)

            # Замінюємо кожне стоп-слово на * (без врахування регістру)
            for word in words:
                # застосовуємо регулярний вираз для заміни без врахування регістру
                import re
                result = re.sub(re.escape(word), '*', result, flags=re.IGNORECASE)

            return result

        return wrapper

    return decorator


# Тестування Task 2
@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print("\nTask 2 - Stop words декоратор:")
print("Тест зі стоп-словами ['pepsi', 'BMW']:")
result = create_slogan("Steve")
print(f"Вхід: Steve")
print(f"Результат: {result}")
print(f"Очікуваний: Steve drinks * in his brand new *!")

# перевіряємо assertion
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
print("Assertion пройдено! https://www.youtube.com/watch?v=lpUi2St40zo")
print("-" * 50)
# або
result = create_slogan("Steve")
print("Результат:", 'result')


# Task 2 - перевірка заміни слів
print("\n2. Stop words декоратор:")
@stop_words(['Python', 'React'])
def tech_message(lang):
    return f"I love {lang}! Python and React are great!"

print(f"   Оригінал: I love React! Python and React are great!")
print(f"   З заміною: {tech_message('React')}")