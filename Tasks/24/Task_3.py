class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []  # ВИПРАВЛЕНО!

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[len(self._items) - 1]

    def size(self):
        return len(self._items)

    def get_from_stack(self, element):
        """
        Шукає та повертає елемент зі стека.
        Інші елементи залишаються у стеку зі збереженням порядку.
        Якщо елемент не знайдено - викидає ValueError
        """
        temp_stack = Stack()
        found = False
        result = None

        # Шукаємо елемент, переміщуючи все у тимчасовий стек
        while not self.is_empty():
            current = self.pop()
            if current == element and not found:
                result = current
                found = True
                break
            else:
                temp_stack.push(current)

        # Повертаємо елементи назад у початковий стек
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

        if not found:
            raise ValueError(f"Element '{element}' not found in stack")

        return result

    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()