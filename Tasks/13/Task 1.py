def count_local_variables(func):
    """
    Функція для підрахунку кількості локальних змінних у функції
    """
    return func.__code__.co_nlocals

# Приклад використання для Task 1
def example_function():
    x = 10
    y = 20
    z = x + y
    return z

def another_function(a, b):
    result = a * b
    temp = result + 10
    return temp

print("Task 1 - Кількість локальних змінних:")
print(f"example_function має {count_local_variables(example_function)} локальних змінних")
print(f"another_function має {count_local_variables(another_function)} локальних змінних")
print("-" * 50)