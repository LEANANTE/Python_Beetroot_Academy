def in_range(start, end=None, step=1):
    """
    Власна реалізація range.
    Може приймати 1, 2 або 3 аргументи.
    """
    # Якщо передано тільки один аргумент - це end, start = 0
    if end is None:
        end = start
        start = 0

    # Валідація step
    if step == 0:
        raise ValueError("Step cannot be zero")

    # Генерація значень
    current = start
    if step > 0:
        while current < end:
            yield current
            current += step
    else:
        while current > end:
            yield current
            current += step


# Тестування:
print(list(in_range(5)))  # [0, 1, 2, 3, 4]
print(list(in_range(2, 8)))  # [2, 3, 4, 5, 6, 7]
print(list(in_range(0, 10, 2)))  # [0, 2, 4, 6, 8]
print(list(in_range(10, 0, -2)))  # [10, 8, 6, 4, 2]