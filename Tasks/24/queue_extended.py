class Queue:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []  # ВИПРАВЛЕНО!

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    def get_from_queue(self, element):  # Виправлена назва методу!
        """
        Шукає та повертає елемент з черги.
        Інші елементи залишаються у черзі зі збереженням порядку.
        Якщо елемент не знайдено - викидає ValueError
        """
        temp_queue = Queue()
        found = False
        result = None

        # Шукаємо елемент, переміщуючи все у тимчасову чергу
        while not self.is_empty():
            current = self.dequeue()
            if current == element and not found:
                result = current
                found = True
            else:
                temp_queue.enqueue(current)

        # Повертаємо елементи назад у початкову чергу
        while not temp_queue.is_empty():
            self.enqueue(temp_queue.dequeue())

        if not found:
            raise ValueError(f"Element '{element}' not found in queue")

        return result

    def __repr__(self):
        representation = "<Queue>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()