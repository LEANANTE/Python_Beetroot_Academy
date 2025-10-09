# калькулятор з довільною кількістю аргументів

def make_operation(operator, *args):
    """
    Виконує арифметичну операцію над довільною кількістю чисел.

    Parameters:
    operator (str): Арифметичний оператор ('+', '-', або '*')
    *args: Довільна кількість числових аргументів

    Returns:
    int/float: Результат операції
    """
    # чи передані числа?
    if not args:
        return 0 if operator in ['+', '-'] else 1

    # оцінка валідність оператора
    if operator not in ['+', '-', '*']:
        raise ValueError(f"Unsupported operator: {operator}. Use '+', '-', or '*'")

    # Виконуємо операцію залежно від оператора
    if operator == '+':
        result = sum(args)
    elif operator == '-':
        result = args[0]
        for num in args[1:]:
            result -= num
    elif operator == '*':
        result = 1
        for num in args:
            result *= num

    return result

# тести Task 3
print("=" * 50)
print("TASK 3 - Простий калькулятор")
print("=" * 50)

# випадки з завдання
test_cases = [
    ('+', [7, 7, 2], 16),
    ('-', [5, 5, -10, -20], 30),
    ('*', [7, 6], 42)
]

print("Основні тести:")
for op, nums, expected in test_cases:
    result = make_operation(op, *nums)
    status = "✓" if result == expected else "✗"
    print(f"  {status} make_operation('{op}', {', '.join(map(str, nums))}) = {result} (очікується: {expected})")

print("\nДодаткові тести:")