def choose_func(nums: list, func1, func2):
    """
    Вибирає, яку функцію застосувати до списку чисел:
    - func1: якщо всі числа позитивні
    - func2: в іншому випадку

    Args:
        nums: список чисел
        func1: функція для обробки, якщо всі числа позитивні
        func2: функція для обробки, якщо є негативні числа

    Returns:
        Результат виконання відповідної функції
    """
    # Перевіряємо, чи всі числа позитивні
    if all(num > 0 for num in nums):
        # Якщо всі позитивні - викликаємо func1
        return func1(nums)
    else:
        # Якщо є негативні - викликаємо func2
        return func2(nums)


# Тестові функції для Task 3
def square_nums(nums):
    """Підносить кожне число до квадрату"""
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    """Видаляє негативні числа зі списку"""
    return [num for num in nums if num > 0]


# Тестування Task 3
print("Task 3 - Функція choose_func:")

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

result1 = choose_func(nums1, square_nums, remove_negatives)
result2 = choose_func(nums2, square_nums, remove_negatives)

print(f"nums1 = {nums1}")
print(f"Результат (всі позитивні, квадрати): {result1}")

print(f"nums2 = {nums2}")
print(f"Результат (є негативні, видалення): {result2}")

# Перевірка assertions
assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]
print("\n Всі assertions пройдені успішно!")

приклади використання choose_func
print("\n" + "=" * 50)
print("Додаткові приклади:")

# Приклад з іншими функціями
def double_nums(nums):
    """Подвоює кожне число"""
    return [num * 2 for num in nums]

def get_absolute_values(nums):
    """Повертає абсолютні значення"""
    return [abs(num) for num in nums]

nums3 = [2, 4, 6, 8]
nums4 = [-5, -3, 2, -1]

print(f"\nnums3 = {nums3}")
print(f"choose_func з double/absolute: {choose_func(nums3, double_nums, get_absolute_values)}")

print(f"\nnums4 = {nums4}")
print(f"choose_func з double/absolute: {choose_func(nums4, double_nums, get_absolute_values)}")