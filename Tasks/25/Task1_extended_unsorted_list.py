"""
Task 1: Extended UnsortedList
Розширення класу UnsortedList з методами append, index, pop, insert та slice
"""

from node import Node


class UnsortedList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    # ========== NEW METHODS FOR HOMEWORK ==========
    
    def append(self, item):
        """
        Додає елемент в кінець списку
        """
        new_node = Node(item)
        
        if self._head is None:
            self._head = new_node
            return
        
        # Знаходимо останній вузол
        current = self._head
        while current.get_next() is not None:
            current = current.get_next()
        
        current.set_next(new_node)
    
    def index(self, item):
        """
        Повертає індекс першого входження елемента
        Викидає ValueError якщо елемент не знайдено
        """
        current = self._head
        position = 0
        found = False
        
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
                position += 1
        
        if found:
            return position
        else:
            raise ValueError(f"{item} is not in list")
    
    def pop(self, pos=None):
        """
        Видаляє та повертає елемент за індексом
        Якщо індекс не вказаний, видаляє останній елемент
        """
        if self.is_empty():
            raise IndexError("pop from empty list")
        
        # Якщо позиція не вказана, видаляємо останній елемент
        if pos is None:
            # Якщо тільки один елемент
            if self._head.get_next() is None:
                data = self._head.get_data()
                self._head = None
                return data
            
            # Знаходимо передостанній елемент
            current = self._head
            while current.get_next().get_next() is not None:
                current = current.get_next()
            
            data = current.get_next().get_data()
            current.set_next(None)
            return data
        
        # Перевірка коректності індексу
        size = self.size()
        if pos < 0 or pos >= size:
            raise IndexError("pop index out of range")
        
        # Видалення першого елемента
        if pos == 0:
            data = self._head.get_data()
            self._head = self._head.get_next()
            return data
        
        # Знаходимо елемент для видалення
        current = self._head
        previous = None
        position = 0
        
        while position < pos:
            previous = current
            current = current.get_next()
            position += 1
        
        data = current.get_data()
        previous.set_next(current.get_next())
        return data
    
    def insert(self, pos, item):
        """
        Вставляє елемент на вказану позицію
        """
        # Перевірка коректності індексу
        size = self.size()
        if pos < 0 or pos > size:
            raise IndexError("list assignment index out of range")
        
        # Вставка на початок
        if pos == 0:
            self.add(item)
            return
        
        # Знаходимо позицію для вставки
        new_node = Node(item)
        current = self._head
        previous = None
        position = 0
        
        while position < pos:
            previous = current
            current = current.get_next()
            position += 1
        
        new_node.set_next(current)
        previous.set_next(new_node)
    
    def slice(self, start, stop):
        """
        Повертає копію списку від start до stop (не включаючи stop)
        """
        result = UnsortedList()
        
        # Перевірка коректності параметрів
        size = self.size()
        if start < 0:
            start = 0
        if stop > size:
            stop = size
        
        if start >= stop:
            return result  # Повертаємо порожній список
        
        # Збираємо елементи для зрізу
        current = self._head
        position = 0
        temp_items = []
        
        while current is not None and position < stop:
            if position >= start:
                temp_items.append(current.get_data())
            current = current.get_next()
            position += 1
        
        # Додаємо елементи до нового списку в зворотному порядку
        # щоб зберегти оригінальний порядок після використання add()
        for item in reversed(temp_items):
            result.add(item)
        
        return result

    def __repr__(self):
        representation = "<UnsortedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

    
if __name__ == "__main__":
    print("=== Тестування Extended UnsortedList ===\n")
    
    my_list = UnsortedList()
    
    # Тест базових методів
    print("1. Базові методи (з оригінального класу):")
    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    print(f"   Після add(31, 77, 17): {my_list}")
    print(f"   size(): {my_list.size()}")
    print(f"   search(77): {my_list.search(77)}")
    print(f"   search(100): {my_list.search(100)}")
    
    # Тест append
    print("\n2. Тестуємо append:")
    my_list.append(93)
    my_list.append(26)
    my_list.append(54)
    print(f"   Після append(93, 26, 54): {my_list}")
    
    # Тест index
    print("\n3. Тестуємо index:")
    print(f"   index(77): {my_list.index(77)}")
    print(f"   index(26): {my_list.index(26)}")
    try:
        my_list.index(100)
    except ValueError as e:
        print(f"   index(100): ValueError - {e}")
    
    # Тест insert
    print("\n4. Тестуємо insert:")
    my_list.insert(0, 100)  # На початок
    print(f"   Після insert(0, 100): {my_list}")
    my_list.insert(3, 200)  # В середину
    print(f"   Після insert(3, 200): {my_list}")
    my_list.insert(my_list.size(), 300)  # В кінець
    print(f"   Після insert(size(), 300): {my_list}")
    
    # Тест pop
    print("\n5. Тестуємо pop:")
    popped = my_list.pop()  # Видаляємо останній
    print(f"   pop() повернув: {popped}")
    print(f"   Список після pop(): {my_list}")
    
    popped = my_list.pop(0)  # Видаляємо перший
    print(f"   pop(0) повернув: {popped}")
    print(f"   Список після pop(0): {my_list}")
    
    popped = my_list.pop(2)  # Видаляємо з середини
    print(f"   pop(2) повернув: {popped}")
    print(f"   Список після pop(2): {my_list}")
    
    # Тест slice
    print("\n6. Тестуємо slice:")
    print(f"   Поточний список: {my_list}")
    sliced = my_list.slice(1, 4)
    print(f"   slice(1, 4): {sliced}")
    sliced = my_list.slice(0, 2)
    print(f"   slice(0, 2): {sliced}")
    sliced = my_list.slice(3, 10)  # stop > size
    print(f"   slice(3, 10): {sliced}")
    
    # Тест remove (з оригінального класу)
    print("\n7. Тестуємо remove (оригінальний метод):")
    my_list.remove(77)
    print(f"   Після remove(77): {my_list}")
    print(f"   Фінальний розмір: {my_list.size()}")
    
    # Тест граничних випадків
    print("\n8. Граничні випадки:")
    empty_list = UnsortedList()
    try:
        empty_list.pop()
    except IndexError as e:
        print(f"   pop() з порожнього списку: IndexError - {e}")
    
    single_list = UnsortedList()
    single_list.add(42)
    print(f"   Список з одним елементом: {single_list}")
    popped = single_list.pop()
    print(f"   pop() повернув: {popped}, список: {single_list}")
