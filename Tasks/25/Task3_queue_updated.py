"""
Task 3: Queue Implementation using Singly Linked List
Реалізація черги з використанням односпрямованого зв'язаного списку
Використовує клас Node з методами get_data() та set_next()
"""

from node import Node


class Queue:
    """
    Черга на основі односпрямованого зв'язаного списку
    FIFO (First In, First Out) структура даних
    """
    
    def __init__(self):
        """Ініціалізація порожньої черги"""
        self._head = None  # Початок черги (front)
        self._tail = None  # Кінець черги (rear)
        self._size = 0     # Розмір черги
    
    def is_empty(self):
        """Перевіряє, чи черга порожня"""
        return self._head is None
    
    def enqueue(self, item):
        """
        Додає елемент в кінець черги
        Часова складність: O(1)
        """
        temp = Node(item)
        
        if self._tail is None:
            # Якщо черга порожня
            self._head = self._tail = temp
        else:
            # Додаємо в кінець
            self._tail.set_next(temp)
            self._tail = temp
        
        self._size += 1
    
    def dequeue(self):
        """
        Видаляє та повертає елемент з початку черги
        Часова складність: O(1)
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        data = self._head.get_data()
        self._head = self._head.get_next()
        
        # Якщо черга стала порожньою
        if self._head is None:
            self._tail = None
        
        self._size -= 1
        return data
    
    def peek(self):
        """
        Повертає елемент з початку черги без видалення
        Часова складність: O(1)
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        return self._head.get_data()
    
    def size(self):
        """Повертає кількість елементів у черзі"""
        return self._size
    
    def clear(self):
        """Очищує чергу"""
        self._head = None
        self._tail = None
        self._size = 0
    
    def contains(self, item):
        """Перевіряє наявність елемента в черзі"""
        current = self._head
        while current is not None:
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False
    
    def __repr__(self):
        """Представлення черги як рядка"""
        if self.is_empty():
            return "<Queue: empty>"
        
        representation = "<Queue (front to rear): "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"
    
    def __len__(self):
        """Дозволяє використовувати len() для черги"""
        return self._size
    
    def __bool__(self):
        """Дозволяє перевірити чергу на порожність через if queue:"""
        return not self.is_empty()


class PriorityQueue:
    """
    Черга з пріоритетами на основі звичайної черги
    Елементи зберігаються як кортежі (priority, data)
    Менше значення priority = вищий пріоритет
    """
    
    def __init__(self):
        """Ініціалізація порожньої черги з пріоритетами"""
        self._head = None
        self._size = 0
    
    def is_empty(self):
        """Перевіряє, чи черга порожня"""
        return self._head is None
    
    def enqueue(self, item, priority):
        """
        Додає елемент з пріоритетом
        Часова складність: O(n)
        """
        temp = Node((priority, item))
        
        # Якщо черга порожня або новий елемент має найвищий пріоритет
        if self._head is None or priority < self._head.get_data()[0]:
            temp.set_next(self._head)
            self._head = temp
        else:
            # Знаходимо правильну позицію для вставки
            current = self._head
            while (current.get_next() is not None and 
                   current.get_next().get_data()[0] <= priority):
                current = current.get_next()
            
            temp.set_next(current.get_next())
            current.set_next(temp)
        
        self._size += 1
    
    def dequeue(self):
        """
        Видаляє та повертає елемент з найвищим пріоритетом
        Часова складність: O(1)
        """
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        
        priority, data = self._head.get_data()
        self._head = self._head.get_next()
        self._size -= 1
        return data
    
    def peek(self):
        """Повертає елемент з найвищим пріоритетом без видалення"""
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        
        priority, data = self._head.get_data()
        return data
    
    def size(self):
        """Повертає розмір черги"""
        return self._size
    
    def __repr__(self):
        """Представлення черги як рядка"""
        if self.is_empty():
            return "<PriorityQueue: empty>"
        
        representation = "<PriorityQueue: "
        current = self._head
        while current is not None:
            priority, data = current.get_data()
            representation += f"({priority}:{data}) "
            current = current.get_next()
        return representation + ">"


# Приклади використання черги
def hot_potato(names, num):
    """
    Гра "Гаряча картопля" - приклад використання черги
    Імітує передачу "картоплі" по колу
    """
    queue = Queue()
    
    # Додаємо всіх гравців до черги
    for name in names:
        queue.enqueue(name)
    
    while queue.size() > 1:
        # Передаємо картоплю num разів
        for _ in range(num):
            # Забираємо з початку і додаємо в кінець
            queue.enqueue(queue.dequeue())
        
        # Гравець, який тримає картоплю, вибуває
        eliminated = queue.dequeue()
        print(f"   {eliminated} вибуває з гри")
    
    # Повертаємо переможця
    return queue.dequeue()


def simulate_printer_queue(tasks, pages_per_minute):
    """
    Симуляція черги друку - приклад використання черги
    tasks: список кортежів (час_надходження, кількість_сторінок)
    """
    printer_queue = Queue()
    current_time = 0
    current_task = None
    task_end_time = 0
    
    print(f"\n   Швидкість друку: {pages_per_minute} сторінок/хвилину")
    
    # Сортуємо завдання за часом надходження
    tasks.sort(key=lambda x: x[0])
    task_index = 0
    
    while task_index < len(tasks) or not printer_queue.is_empty() or current_task:
        # Додаємо нові завдання до черги
        while task_index < len(tasks) and tasks[task_index][0] <= current_time:
            arrival_time, pages = tasks[task_index]
            printer_queue.enqueue((arrival_time, pages))
            print(f"   Час {current_time}: Нове завдання ({pages} стор.) додано до черги")
            task_index += 1
        
        # Якщо принтер вільний і є завдання в черзі
        if current_task is None and not printer_queue.is_empty():
            current_task = printer_queue.dequeue()
            arrival_time, pages = current_task
            task_end_time = current_time + (pages / pages_per_minute)
            print(f"   Час {current_time}: Початок друку {pages} сторінок")
        
        # Перевіряємо, чи завершилось поточне завдання
        if current_task and current_time >= task_end_time:
            print(f"   Час {task_end_time:.1f}: Друк завершено")
            current_task = None
        
        current_time += 1
        
        # Виходимо, якщо всі завдання оброблені
        if task_index >= len(tasks) and printer_queue.is_empty() and current_task is None:
            break


# Демонстрація використання
if __name__ == "__main__":
    print("=== Тестування Queue ===\n")
    
    # Створення черги
    queue = Queue()
    
    # Тест 1: Базові операції
    print("1. Базові операції:")
    print(f"   Черга порожня? {queue.is_empty()}")
    print(f"   Розмір: {queue.size()}")
    
    queue.enqueue("First")
    queue.enqueue("Second")
    queue.enqueue("Third")
    queue.enqueue("Fourth")
    print(f"   Після enqueue('First', 'Second', 'Third', 'Fourth'):")
    print(f"   {queue}")
    print(f"   Розмір: {queue.size()}")
    print(f"   Використання len(): {len(queue)}")
    
    # Тест 2: Dequeue операція
    print("\n2. Dequeue операції:")
    dequeued = queue.dequeue()
    print(f"   dequeue() повернув: '{dequeued}'")
    print(f"   {queue}")
    
    # Тест 3: Peek операція
    print("\n3. Peek операція:")
    front = queue.peek()
    print(f"   peek() повернув: '{front}'")
    print(f"   Черга не змінилась: {queue}")
    
    # Тест 4: Пошук елемента
    print("\n4. Пошук елемента:")
    print(f"   contains('Third')? {queue.contains('Third')}")
    print(f"   contains('Fifth')? {queue.contains('Fifth')}")
    
    # Тест 5: Clear операція
    print("\n5. Clear операція:")
    queue.clear()
    print(f"   Після clear(): {queue}")
    print(f"   Черга порожня? {queue.is_empty()}")
    
    # Тест 6: PriorityQueue
    print("\n=== Тестування PriorityQueue ===\n")
    
    pq = PriorityQueue()
    
    print("6. Операції з чергою пріоритетів:")
    pq.enqueue("Низький пріоритет", 3)
    pq.enqueue("Високий пріоритет", 1)
    pq.enqueue("Середній пріоритет", 2)
    pq.enqueue("Найвищий пріоритет", 0)
    pq.enqueue("Ще один середній", 2)
    
    print(f"   Черга після додавання: {pq}")
    print(f"   Розмір: {pq.size()}")
    
    print("\n   Видаляємо елементи в порядку пріоритету:")
    while not pq.is_empty():
        print(f"   → {pq.dequeue()}")
    
    # Тест 7: Гра "Гаряча картопля"
    print("\n7. Приклад: Гра 'Гаряча картопля'")
    
    players = ["Анна", "Богдан", "Василь", "Галина", "Дмитро"]
    print(f"   Гравці: {players}")
    print(f"   Передача через кожні 3 кроки")
    
    winner = hot_potato(players, 3)
    print(f"   Переможець: {winner}")
    
    # Тест 8: Симуляція черги друку
    print("\n8. Приклад: Симуляція черги друку")
    
    # Формат: (час_надходження, кількість_сторінок)
    print_tasks = [
        (0, 5),    # Завдання 1: приходить на 0 хвилині, 5 сторінок
        (1, 3),    # Завдання 2: приходить на 1 хвилині, 3 сторінки
        (3, 2),    # Завдання 3: приходить на 3 хвилині, 2 сторінки
        (4, 8),    # Завдання 4: приходить на 4 хвилині, 8 сторінок
    ]
    
    simulate_printer_queue(print_tasks, pages_per_minute=2)
    
    # Тест 9: Обробка помилок
    print("\n9. Обробка помилок:")
    empty_queue = Queue()
    
    try:
        empty_queue.dequeue()
    except IndexError as e:
        print(f"   Спроба dequeue() з порожньої черги: {e}")
    
    try:
        empty_queue.peek()
    except IndexError as e:
        print(f"   Спроба peek() з порожньої черги: {e}")
    
    # Тест 10: Використання черги як булевого значення
    print("\n10. Використання черги в умовах:")
    queue1 = Queue()
    queue2 = Queue()
    queue2.enqueue("item")
    
    print(f"   Порожня черга: if queue → {bool(queue1)}")
    print(f"   Непорожня черга: if queue → {bool(queue2)}")
