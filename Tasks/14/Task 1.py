# Task 1: Декоратор logger - виводить інформацію про виклик функції

def logger(func):
    """
    Декоратор, який виводить назву функції та передані їй аргументи
    NOTE! It should print the function, not the result of its execution!
    """

    def wrapper(*args, **kwargs):
        # Форматуємо аргументи для виводу (без лапок для чисел)
        args_repr = [str(arg) for arg in args]
        kwargs_repr = [f"{k}={v}" for k, v in kwargs.items()]
        all_args = ", ".join(args_repr + kwargs_repr)

        # Виводимо інформацію про виклик у форматі з прикладу
        print(f"{func.__name__} called with {all_args}")

        # Викликаємо оригінальну функцію та повертаємо результат
        return func(*args, **kwargs)

    return wrapper


# Тестування Task 1
@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


print("Task 1 - Logger декоратор:")
print("Приклад 1:")
result1 = add(4, 5)  # Виведе: add called with 4, 5
print(f"Результат функції: {result1}\n")

print("Приклад 2:")
result2 = square_all(2, 3, 4)  # Виведе: square_all called with 2, 3, 4
print(f"Результат функції: {result2}")
print("-" * 50)


# Task 1 - перевірка формату виводу
print("\n1. Logger декоратор:")
@logger
def multiply(a, b, c):
    return a * b * c

result = multiply(2, 3, 4)
print(f"   Результат множення: {result}")