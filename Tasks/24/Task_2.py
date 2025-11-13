from stack import Stack


def is_balanced(expression):
    """
    Перевіряє чи збалансовані дужки (), {}, []
    """
    s = Stack()

    # Словник відповідності закриваючих і відкриваючих дужок
    matching = {')': '(', '}': '{', ']': '['}
    opening = set(['(', '{', '['])
    closing = set([')', '}', ']'])

    for char in expression:
        if char in opening:
            # Якщо відкриваюча дужка - додаємо в стек
            s.push(char)
        elif char in closing:
            # Якщо закриваюча дужка
            if s.is_empty():
                # Немає відповідної відкриваючої
                return False

            # Перевіряємо чи відповідає остання відкриваюча дужка
            if s.pop() != matching[char]:
                return False

    # Якщо стек порожній - всі дужки збалансовані
    return s.is_empty()


def check_balance():
    """Основна функція для перевірки балансу дужок"""
    expression = input("Введіть вираз для перевірки: ")

    if is_balanced(expression):
        print("✅ Дужки збалансовані")
    else:
        print("❌ Дужки НЕ збалансовані")

    return is_balanced(expression)


# Приклади тестування
if __name__ == "__main__":
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[()]}", True),
        ("((()))", True),
        ("(()", False),
        ("())", False),
    ]

    print("Тестування:")
    for expr, expected in test_cases:
        result = is_balanced(expr)
        status = "✅" if result == expected else "❌"
        print(f"{status} '{expr}' -> {result} (очікувалось {expected})")

    print("\n" + "=" * 50)
    check_balance()