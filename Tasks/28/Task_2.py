"""
Task 2: Merge Sort without Slice Operator

Модифікація merge_sort з sort.py БЕЗ використання slice operator.

Оригінальний merge_sort з курсу (ВИКОРИСТОВУЄ SLICE):

    def merge_sort(array):
        if len(array) > 1:
            mid = len(array) // 2
            left_half = array[:mid]      # <-- slice operator
            right_half = array[mid:]     # <-- slice operator
            
            merge_sort(left_half)
            merge_sort(right_half)
            ...

Завдання: переписати БЕЗ array[:mid] та array[mid:]
"""


def merge_sort(array):
    """
    Merge Sort без slice operator.
    Замість створення нових списків використовуємо індекси.
    """
    if len(array) > 1:
        # Створюємо допоміжний масив один раз
        aux = [0] * len(array)
        _merge_sort_helper(array, aux, 0, len(array) - 1)


def _merge_sort_helper(array, aux, low, high):
    """
    Рекурсивна функція сортування.
    
    Замість slice (array[:mid]) використовуємо індекси low, mid, high
    для визначення меж підмасивів.
    """
    if low < high:
        mid = (low + high) // 2
        
        # Замість: left_half = array[:mid]; merge_sort(left_half)
        _merge_sort_helper(array, aux, low, mid)
        
        # Замість: right_half = array[mid:]; merge_sort(right_half)
        _merge_sort_helper(array, aux, mid + 1, high)
        
        # Зливаємо підмасиви
        _merge(array, aux, low, mid, high)


def _merge(array, aux, low, mid, high):
    """
    Злиття двох відсортованих підмасивів БЕЗ slice operator.
    
    Оригінал використовував:
        left_half[i] та right_half[j]
    
    Ми використовуємо:
        array[low..mid] як ліву частину
        array[mid+1..high] як праву частину
    """
    # Копіюємо елементи в допоміжний масив
    for k in range(low, high + 1):
        aux[k] = array[k]
    
    i = low        # індекс для лівої частини (замість left_half)
    j = mid + 1    # індекс для правої частини (замість right_half)
    k = low        # індекс для результату
    
    # Зливаємо - логіка як в оригіналі, але з індексами
    while i <= mid and j <= high:
        if aux[i] <= aux[j]:
            array[k] = aux[i]
            i = i + 1
        else:
            array[k] = aux[j]
            j = j + 1
        k = k + 1
    
    # Копіюємо залишок лівої частини
    while i <= mid:
        array[k] = aux[i]
        i = i + 1
        k = k + 1
    
    # Копіюємо залишок правої частини
    while j <= high:
        array[k] = aux[j]
        j = j + 1
        k = k + 1


# ============================================================================
# ПОРІВНЯННЯ: зі slice vs без slice
# ============================================================================
#
# ОРИГІНАЛ (зі slice):              МОДИФІКАЦІЯ (без slice):
# -----------------------------     -------------------------------
# left_half = array[:mid]           Використовуємо індекси low, mid
# right_half = array[mid:]          Використовуємо індекси mid+1, high
#                                   
# Створює нові списки               Працюємо з оригінальним масивом
# на кожному рівні рекурсії         + один допоміжний масив aux
#
# ПЕРЕВАГИ версії без slice:
# - Менше виділення пам'яті (один aux замість багатьох списків)
# - Потенційно швидше для великих масивів
# - Більш ефективне використання пам'яті
# ============================================================================


if __name__ == "__main__":
    import random
    
    print("=" * 60)
    print("Task 2: Merge Sort без slice operator")
    print("=" * 60)
    
    # Тест 1: Простий масив
    test1 = [64, 34, 25, 12, 22, 11, 90, 5]
    print(f"\nВхідний масив:   {test1}")
    merge_sort(test1)
    print(f"Відсортований:   {test1}")
    
    # Тест 2: Випадковий масив
    test2 = [random.randint(1, 100) for _ in range(15)]
    print(f"\nВипадковий:      {test2}")
    merge_sort(test2)
    print(f"Відсортований:   {test2}")
    
    # Тест 3: Зворотно відсортований
    test3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(f"\nЗворотний:       {test3}")
    merge_sort(test3)
    print(f"Відсортований:   {test3}")
    
    # Тест 4: Один елемент
    test4 = [42]
    merge_sort(test4)
    print(f"\nОдин елемент:    {test4}")
    
    # Перевірка коректності
    test5 = [random.randint(1, 1000) for _ in range(100)]
    expected = sorted(test5[:])
    merge_sort(test5)
    print(f"\nПеревірка (100 елементів): {'✓ Коректно' if test5 == expected else '✗ Помилка'}")
    
    print("\n" + "=" * 60)
    print("Ключова зміна: замість array[:mid] використовуємо")
    print("індекси low, mid, high для визначення меж підмасивів")
    print("=" * 60)
