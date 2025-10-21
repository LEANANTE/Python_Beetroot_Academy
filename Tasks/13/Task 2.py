def outer_function(message):
    """
    Зовнішня функція, яка повертає внутрішню функцію
    """

    def inner_function(name):
        """
        Внутрішня функція, яка використовує параметр зовнішньої функції
        """
        return f"{message}, {name}!"

    return inner_function


# Приклад використання для Task 2
print("Task 2 - Функція всередині функції:")
greeting = outer_function("Привіт")
welcome = outer_function("Ласкаво просимо")

print(greeting("Олександр"))  # Виведе: Привіт, Олександр!
print(welcome("Марія"))  # Виведе: Ласкаво просимо, Марія!


# Альтернативний приклад - фабрика функцій
def multiply_by(n):
    """Створює функцію множення на задане число"""

    def multiplier(x):
        return x * n

    return multiplier


multiply_by_2 = multiply_by(2)
multiply_by_5 = multiply_by(5)

print(f"3 * 2 = {multiply_by_2(3)}")  # Виведе: 6
print(f"3 * 5 = {multiply_by_5(3)}")  # Виведе: 15
print("-" * 50)