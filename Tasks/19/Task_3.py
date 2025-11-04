class MyIterable:
    """
    Власний ітерабельний клас з підтримкою індексації.
    """

    def __init__(self, data):
        self.data = list(data)

    def __iter__(self):
        """Повертає ітератор для використання в for-in циклі"""
        return MyIterator(self.data)

    def __getitem__(self, index):
        """Дозволяє доступ через квадратні дужки [index]"""
        if isinstance(index, slice):
            # Підтримка зрізів: obj[1:3]
            return MyIterable(self.data[index])
        else:
            # Звичайний індекс: obj[0]
            return self.data[index]

    def __len__(self):
        """Підтримка len()"""
        return len(self.data)

    def __repr__(self):
        return f"MyIterable({self.data})"


class MyIterator:
    """Окремий клас ітератора"""

    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        raise StopIteration


# Тестування:
my_obj = MyIterable([1, 2, 3, 4, 5])

# Використання в циклі for-in:
print("Ітерація:")
for item in my_obj:
    print(item, end=' ')  # 1 2 3 4 5
print()

# Доступ через квадратні дужки:
print(f"my_obj[0] = {my_obj[0]}")  # 1
print(f"my_obj[-1] = {my_obj[-1]}")  # 5
print(f"my_obj[1:3] = {my_obj[1:3]}")  # MyIterable([2, 3])

# Додаткова функціональність:
print(f"len(my_obj) = {len(my_obj)}")  # 5