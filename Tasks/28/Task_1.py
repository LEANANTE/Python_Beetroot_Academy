"""
Task 1: Cocktail Sort (Bidirectional Bubble Sort)

Модифікація bubble_sort з sort.py для сортування в обох напрямках.
Перший прохід рухається "вгору", другий - "вниз".

Оригінальний bubble_sort з курсу:

    def bubble_sort(array):
        for pass_num in range(len(array) - 1, 0, -1):
            for i in range(pass_num):
                if array[i] > array[i + 1]:
                    temp = array[i]
                    array[i] = array[i + 1]
                    array[i + 1] = temp
"""


def cocktail_sort(array):
    """
    Двонаправлене бульбашкове сортування (Cocktail Sort / Shaker Sort).
    
    Модифікація стандартного bubble_sort:
    1. Прохід зліва направо ("вгору") - найбільший елемент спливає вправо
    2. Прохід справа наліво ("вниз") - найменший елемент опускається вліво
    3. Повторюємо поки масив не відсортований
    """
    n = len(array)
    swapped = True
    start = 0
    end = n - 1
    
    while swapped:
        swapped = False
        
        # Прохід ВГОРУ (зліва направо) - як в оригінальному bubble_sort
        for i in range(start, end):
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
                swapped = True
        
        if not swapped:
            break
        
        swapped = False
        end = end - 1
        
        # Прохід ВНИЗ (справа наліво) - додаткова модифікація
        for i in range(end - 1, start - 1, -1):
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
                swapped = True
        
        start = start + 1


# ============================================================================
# КОЛИ ДОРЕЧНО ВИКОРИСТОВУВАТИ COCKTAIL SORT:
# ============================================================================
#
# 1. Проблема "черепах" (turtles) у звичайному bubble sort:
#    - "Черепахи" - це малі елементи в кінці масиву
#    - У bubble_sort вони рухаються лише на 1 позицію за прохід
#    - У cocktail_sort вони швидко переміщуються за зворотний прохід
#
# 2. Частково відсортовані масиви:
#    - Коли масив майже відсортований з обох кінців
#    - Cocktail sort швидше завершить роботу
#
# 3. Приклад:
#    Масив [2, 3, 4, 5, 1]:
#    - Bubble Sort: 4 проходи (1 рухається по 1 позиції)
#    - Cocktail Sort: ~2 проходи (1 швидко переміщується вліво)
#
# 4. Складність:
#    - Найгірший випадок: O(n²) - як у bubble sort
#    - Але на практиці часто швидше для певних типів даних
# ============================================================================


if __name__ == "__main__":
    import random
    
    print("=" * 60)
    print("Task 1: Cocktail Sort (модифікація bubble_sort)")
    print("=" * 60)
    
    # Тест 1: Масив з "черепахою" - демонструє перевагу
    test1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
    print(f"\nМасив з 'черепахою': {test1}")
    cocktail_sort(test1)
    print(f"Відсортований:       {test1}")
    
    # Тест 2: Випадковий масив
    test2 = [random.randint(1, 100) for _ in range(15)]
    print(f"\nВипадковий масив:    {test2}")
    cocktail_sort(test2)
    print(f"Відсортований:       {test2}")
    
    # Тест 3: Зворотно відсортований
    test3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(f"\nЗворотний масив:     {test3}")
    cocktail_sort(test3)
    print(f"Відсортований:       {test3}")
    
    # Перевірка коректності
    test4 = [random.randint(1, 100) for _ in range(50)]
    expected = sorted(test4[:])
    cocktail_sort(test4)
    print(f"\nПеревірка (50 елементів): {'✓ Коректно' if test4 == expected else '✗ Помилка'}")
    
    print("\n" + "=" * 60)
    print("ВИСНОВОК: Cocktail Sort доречний коли є 'черепахи' -")
    print("малі елементи в кінці масиву, або масив частково відсортований")
    print("=" * 60)
