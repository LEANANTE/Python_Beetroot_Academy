def with_index(iterable, start=0):
    """
    Власна реалізація enumerate.
    Повертає генератор пар (індекс, елемент).
    """
    index = start
    for item in iterable:
        yield (index, item)
        index += 1

# Тестування:
my_list = ['a', 'b', 'c']
for idx, val in with_index(my_list, start=1):
    print(f"{idx}: {val}")
# Вивід: 1: a, 2: b, 3: c