"""
Домашнє завдання: Fibonacci Search
Алгоритми пошуку та хешування

Fibonacci Search - алгоритм пошуку, який використовує числа Фібоначчі
для поділу масиву замість поділу навпіл (як у бінарному пошуку).
"""

import time


def fibonacci_search(arr, key):
    """
    Пошук Фібоначчі - використовує числа Фібоначчі для поділу масиву.
    
    Args:
        arr: відсортований масив
        key: шукане значення
    
    Returns:
        індекс елемента або -1 якщо не знайдено
    
    Складність:
        Часова: O(log n)
        Просторова: O(1)
    """
    n = len(arr)
    
    if n == 0:
        return -1
    
    # Ініціалізація чисел Фібоначчі
    # fib_m2 = F(k-2), fib_m1 = F(k-1), fib = F(k)
    fib_m2 = 0  # (k-2)-е число Фібоначчі
    fib_m1 = 1  # (k-1)-е число Фібоначчі
    fib = fib_m1 + fib_m2  # k-е число Фібоначчі
    
    # Знаходимо найменше число Фібоначчі, яке >= n
    while fib < n:
        fib_m2 = fib_m1
        fib_m1 = fib
        fib = fib_m1 + fib_m2
    
    # Зміщення для елімінованої частини масиву
    offset = -1
    
    # Поки є елементи для перевірки
    while fib > 1:
        # Перевіряємо валідний індекс (не виходимо за межі масиву)
        i = min(offset + fib_m2, n - 1)
        
        if arr[i] < key:
            # Ключ у правій частині, зсуваємо Фібоначчі на два вниз
            fib = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib - fib_m1
            offset = i
        elif arr[i] > key:
            # Ключ у лівій частині, зсуваємо Фібоначчі на один вниз
            fib = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib - fib_m1
        else:
            # Знайшли елемент!
            return i
    
    # Перевіряємо останній елемент (якщо залишився)
    if fib_m1 and offset + 1 < n and arr[offset + 1] == key:
        return offset + 1
    
    return -1


def binary_search(arr, key):
    """
    Ітеративний бінарний пошук для порівняння.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def compare_algorithms(arr, test_keys, iterations=1000):
    """
    Порівнює продуктивність Fibonacci Search та Binary Search.
    """
    print("\n" + "=" * 60)
    print("ПОРІВНЯННЯ ПРОДУКТИВНОСТІ")
    print("=" * 60)
    print(f"Розмір масиву: {len(arr)}")
    print(f"Кількість ітерацій: {iterations}")
    print("-" * 60)
    
    # Тест Fibonacci Search
    start = time.perf_counter()
    for _ in range(iterations):
        for key in test_keys:
            fibonacci_search(arr, key)
    fib_time = time.perf_counter() - start
    
    # Тест Binary Search
    start = time.perf_counter()
    for _ in range(iterations):
        for key in test_keys:
            binary_search(arr, key)
    bin_time = time.perf_counter() - start
    
    print(f"Fibonacci Search: {fib_time:.6f} сек")
    print(f"Binary Search:    {bin_time:.6f} сек")
    print("-" * 60)
    
    if fib_time < bin_time:
        print(f"Fibonacci Search швидший на {((bin_time - fib_time) / bin_time * 100):.2f}%")
    else:
        print(f"Binary Search швидший на {((fib_time - bin_time) / fib_time * 100):.2f}%")


# ===================== ТЕСТУВАННЯ =====================
if __name__ == "__main__":
    # Тестовий масив
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
    
    print("=" * 60)
    print("FIBONACCI SEARCH")
    print("=" * 60)
    print(f"Масив: {arr}")
    print("-" * 60)
    
    # Тести
    test_cases = [7, 1, 25, 13, 8, 0, 30]
    
    for key in test_cases:
        result = fibonacci_search(arr, key)
        if result != -1:
            print(f"Пошук {key:2d}: знайдено на індексі {result}")
        else:
            print(f"Пошук {key:2d}: не знайдено")
    
    # Порівняння алгоритмів
    large_arr = list(range(0, 10000, 2))  # [0, 2, 4, ..., 9998]
    test_keys = [0, 500, 2500, 5000, 7500, 9998, 9999]
    compare_algorithms(large_arr, test_keys)
    
    # Теоретичне порівняння
    print("\n" + "=" * 60)
    print("ТЕОРЕТИЧНЕ ПОРІВНЯННЯ")
    print("=" * 60)
    print("""
┌─────────────────────┬─────────────────┬──────────────────┐
│   Характеристика    │  Binary Search  │ Fibonacci Search │
├─────────────────────┼─────────────────┼──────────────────┤
│ Часова складність   │    O(log n)     │     O(log n)     │
├─────────────────────┼─────────────────┼──────────────────┤
│ Просторова складн.  │      O(1)       │       O(1)       │
├─────────────────────┼─────────────────┼──────────────────┤
│ Операція поділу     │   Ділення / 2   │  Числа Фібоначчі │
├─────────────────────┼─────────────────┼──────────────────┤
│ Арифметика          │ +, -, *, /      │    Тільки +, -   │
├─────────────────────┼─────────────────┼──────────────────┤
│ Доступ до пам'яті   │   Випадковий    │ Більш послідовний│
└─────────────────────┴─────────────────┴──────────────────┘

ПЕРЕВАГИ FIBONACCI SEARCH:
✓ Використовує тільки додавання і віднімання (без ділення)
✓ Більш послідовний доступ до пам'яті
✓ Краще для повільних носіїв (HDD, стрічкові накопичувачі)
✓ Ефективний для дуже великих масивів

ПЕРЕВАГИ BINARY SEARCH:
✓ Простіша реалізація
✓ На сучасних CPU з швидким діленням — часто швидший
✓ Більш передбачувана поведінка
""")
