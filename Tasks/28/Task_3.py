"""
Task 3: Hybrid Quick Sort with Insertion Sort

Покращення quick_sort з sort.py шляхом використання insertion_sort 
для малих підмасивів (partition limit).

Оригінальні функції з курсу:

    def insertion_sort(array):
        for index in range(1, len(array)):
            current_value = array[index]
            position = index
            while position > 0 and array[position - 1] > current_value:
                array[position] = array[position - 1]
                position = position - 1
            array[position] = current_value

    def quick_sort_helper(array, first, last):
        if first < last:
            split_point = partition(array, first, last)
            quick_sort_helper(array, first, split_point - 1)
            quick_sort_helper(array, split_point + 1, last)
"""

import random
import time


# Адаптований insertion_sort для діапазону [low, high]
# (базується на insertion_sort з sort.py)
def insertion_sort_range(array, low, high):
    """
    Insertion sort для діапазону array[low:high+1].
    Адаптація оригінального insertion_sort з sort.py.
    """
    for index in range(low + 1, high + 1):
        current_value = array[index]
        position = index
        
        while position > low and array[position - 1] > current_value:
            array[position] = array[position - 1]
            position = position - 1
        
        array[position] = current_value


# Partition з sort.py (без змін)
def partition(array, first, last):
    """Оригінальна функція partition з sort.py"""
    pivot_value = array[first]
    
    left_mark = first + 1
    right_mark = last
    
    done = False
    while not done:
        while left_mark <= right_mark and array[left_mark] <= pivot_value:
            left_mark = left_mark + 1
        
        while array[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1
        
        if right_mark < left_mark:
            done = True
        else:
            temp = array[left_mark]
            array[left_mark] = array[right_mark]
            array[right_mark] = temp
    
    temp = array[first]
    array[first] = array[right_mark]
    array[right_mark] = temp
    
    return right_mark


def quick_sort_hybrid(array, partition_limit=10):
    """
    Гібридний Quick Sort.
    Використовує insertion_sort для підмасивів розміром <= partition_limit.
    """
    _quick_sort_helper_hybrid(array, 0, len(array) - 1, partition_limit)


def _quick_sort_helper_hybrid(array, first, last, partition_limit):
    """
    Модифікований quick_sort_helper з sort.py.
    
    Зміна: якщо розмір підмасиву <= partition_limit,
    використовуємо insertion_sort замість рекурсії.
    """
    # МОДИФІКАЦІЯ: для малих підмасивів використовуємо insertion sort
    if last - first + 1 <= partition_limit:
        insertion_sort_range(array, first, last)
        return
    
    # Оригінальна логіка з sort.py
    if first < last:
        split_point = partition(array, first, last)
        _quick_sort_helper_hybrid(array, first, split_point - 1, partition_limit)
        _quick_sort_helper_hybrid(array, split_point + 1, last, partition_limit)


# ============================================================================
# ЧОМУ ЦЕ МАЄ СЕНС (Why does this make sense?)
# ============================================================================
#
# 1. НАКЛАДНІ ВИТРАТИ QUICK SORT:
#    - Кожен рекурсивний виклик має overhead (збереження стеку, виклик функції)
#    - Partition потребує порівнянь навіть для 2-3 елементів
#    - Для малих масивів ці витрати перевищують користь від O(n log n)
#
# 2. ПЕРЕВАГИ INSERTION SORT ДЛЯ МАЛИХ МАСИВІВ:
#    - Простий цикл без рекурсії
#    - Мінімальні накладні витрати
#    - Відмінна локальність даних (cache-friendly)
#    - Для n < 15-20: O(n²) з малим константним фактором швидше 
#      ніж O(n log n) з великим overhead
#
# 3. ПРАКТИЧНЕ ЗАСТОСУВАННЯ:
#    - Java Arrays.sort() використовує подібну оптимізацію
#    - Python Timsort також комбінує алгоритми
#    - Оптимальний partition_limit: 10-20 елементів
#
# ============================================================================


def analyze_partition_limits():
    """Аналіз продуктивності з різними значеннями partition_limit"""
    
    print("\n" + "=" * 70)
    print("АНАЛІЗ: час виконання для різних partition_limit")
    print("=" * 70)
    
    sizes = [1000, 5000, 10000, 50000]
    limits = [1, 5, 10, 15, 20, 30, 50]
    
    print(f"\n{'Розмір':<10}", end="")
    for limit in limits:
        print(f"{'lim=' + str(limit):<9}", end="")
    print()
    print("-" * 70)
    
    best_limits = {}
    
    for size in sizes:
        print(f"{size:<10}", end="")
        base_array = [random.randint(1, 10000) for _ in range(size)]
        times = {}
        
        for limit in limits:
            test_array = base_array[:]
            
            start = time.time()
            quick_sort_hybrid(test_array, partition_limit=limit)
            elapsed = time.time() - start
            
            times[limit] = elapsed
            print(f"{elapsed:<9.4f}", end="")
        
        best_limit = min(times, key=times.get)
        best_limits[size] = best_limit
        print()
    
    print("-" * 70)
    
    print("\nОптимальний partition_limit:")
    for size, limit in best_limits.items():
        print(f"  Розмір {size:>6}: limit = {limit}")
    
    return best_limits


if __name__ == "__main__":
    print("=" * 70)
    print("Task 3: Hybrid Quick Sort (quick_sort + insertion_sort)")
    print("=" * 70)
    
    # Демонстрація
    test = [random.randint(1, 100) for _ in range(20)]
    print(f"\nВхідний масив:   {test}")
    quick_sort_hybrid(test, partition_limit=10)
    print(f"Відсортований:   {test}")
    
    # Перевірка
    test2 = [random.randint(1, 1000) for _ in range(100)]
    expected = sorted(test2[:])
    quick_sort_hybrid(test2)
    print(f"\nПеревірка (100 елементів): {'✓ Коректно' if test2 == expected else '✗ Помилка'}")
    
    # Пояснення
    print("\n" + "=" * 70)
    print("ЧОМУ ЦЕ ПРАЦЮЄ:")
    print("-" * 70)
    print("""
1. Quick Sort має overhead на рекурсію та partitioning
2. Для малих підмасивів (< 10-20) цей overhead занадто великий
3. Insertion Sort простіший і швидший для малих масивів:
   - Немає рекурсії
   - Краще використання CPU cache
   - Менше порівнянь для майже відсортованих даних
4. Комбінація дає найкращу загальну продуктивність
""")
    
    # Аналіз
    analyze_partition_limits()
    
    print("\n" + "=" * 70)
    print("ВИСНОВОК: Оптимальний partition_limit = 10-20")
    print("=" * 70)
