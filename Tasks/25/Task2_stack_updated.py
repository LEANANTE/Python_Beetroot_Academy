"""
Task 2: Stack Implementation using Singly Linked List
Реалізація стека з використанням односпрямованого зв'язаного списку
Використовує клас Node з методами get_data() та set_next()
"""

from node import Node


class Stack:
    """
    Стек на основі односпрямованого зв'язаного списку
    LIFO (Last In, First Out) структура даних
    """
    
    def __init__(self):
        """Ініціалізація порожнього стека"""
        self._head = None  # Вершина стека
        self._size = 0     # Розмір стека
    
    def is_empty(self):
        """Перевіряє, чи стек порожній"""
        return self._head is None
    
    def push(self, item):
        """
        Додає елемент на вершину стека
        Часова складність: O(1)
        """
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp
        self._size += 1
    
    def pop(self):
        """
        Видаляє та повертає елемент з вершини стека
        Часова складність: O(1)
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        data = self._head.get_data()
        self._head = self._head.get_next()
        self._size -= 1
        return data
    
    def peek(self):
        """
        Повертає елемент з вершини стека без видалення
        Часова складність: O(1)
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        return self._head.get_data()
    
    def size(self):
        """Повертає кількість елементів у стеку"""
        return self._size
    
    def clear(self):
        """Очищує стек"""
        self._head = None
        self._size = 0
    
    def __repr__(self):
        """Представлення стека як рядка"""
        if self.is_empty():
            return "<Stack: empty>"
        
        representation = "<Stack (top to bottom): "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"
    
    def __len__(self):
        """Дозволяє використовувати len() для стека"""
        return self._size
    
    def __bool__(self):
        """Дозволяє перевірити стек на порожність через if stack:"""
        return not self.is_empty()


def is_balanced_parentheses(expression):
    """
    Функція для перевірки збалансованості дужок
    Приклад використання стека
    """
    stack = Stack()
    opening = "({["
    closing = ")}]"
    pairs = {"(": ")", "{": "}", "[": "]"}
    
    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.is_empty():
                return False
            if pairs[stack.pop()] != char:
                return False
    
    return stack.is_empty()


def reverse_string(string):
    """
    Функція для розвороту рядка за допомогою стека
    Приклад використання стека
    """
    stack = Stack()
    
    # Додаємо всі символи до стека
    for char in string:
        stack.push(char)
    
    # Витягуємо символи в зворотному порядку
    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()
    
    return reversed_str


def decimal_to_binary(decimal_num):
    """
    Функція для переведення десяткового числа в двійкове
    Приклад використання стека
    """
    if decimal_num == 0:
        return "0"
    
    stack = Stack()
    
    while decimal_num > 0:
        remainder = decimal_num % 2
        stack.push(remainder)
        decimal_num = decimal_num // 2
    
    binary_str = ""
    while not stack.is_empty():
        binary_str += str(stack.pop())
    
    return binary_str


# Демонстрація використання
if __name__ == "__main__":
    print("=== Тестування Stack ===\n")
    
    # Створення стека
    stack = Stack()
    
    # Тест 1: Базові операції
    print("1. Базові операції:")
    print(f"   Стек порожній? {stack.is_empty()}")
    print(f"   Розмір: {stack.size()}")
    
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    print(f"   Після push(10, 20, 30, 40): {stack}")
    print(f"   Розмір: {stack.size()}")
    print(f"   Використання len(): {len(stack)}")
    
    # Тест 2: Pop операція
    print("\n2. Pop операції:")
    popped = stack.pop()
    print(f"   pop() повернув: {popped}")
    print(f"   Стек після pop(): {stack}")
    
    # Тест 3: Peek операція
    print("\n3. Peek операція:")
    top = stack.peek()
    print(f"   peek() повернув: {top}")
    print(f"   Стек не змінився: {stack}")
    
    # Тест 4: Clear операція
    print("\n4. Clear операція:")
    stack.clear()
    print(f"   Після clear(): {stack}")
    print(f"   Стек порожній? {stack.is_empty()}")
    
    # Тест 5: Перевірка збалансованості дужок
    print("\n5. Приклад: перевірка збалансованості дужок")
    
    test_expressions = [
        "((()))",
        "({[]})",
        "((())",
        "({[}])",
        "{[()]}[]",
        "",
        "((a+b)*c)",
    ]
    
    for expr in test_expressions:
        result = is_balanced_parentheses(expr)
        status = "збалансовано ✓" if result else "не збалансовано ✗"
        print(f"   '{expr}' - {status}")
    
    # Тест 6: Розворот рядка
    print("\n6. Приклад: розворот рядка")
    
    test_strings = [
        "hello",
        "Python",
        "12345",
        "А роза упала на лапу Азора",
    ]
    
    for string in test_strings:
        reversed_str = reverse_string(string)
        print(f"   '{string}' → '{reversed_str}'")
    
    # Тест 7: Переведення в двійкову систему
    print("\n7. Приклад: переведення в двійкову систему")
    
    test_numbers = [0, 2, 10, 27, 256]
    
    for num in test_numbers:
        binary = decimal_to_binary(num)
        print(f"   {num} (десяткове) = {binary} (двійкове)")
    
    # Тест 8: Обробка помилок
    print("\n8. Обробка помилок:")
    empty_stack = Stack()
    
    try:
        empty_stack.pop()
    except IndexError as e:
        print(f"   Спроба pop() з порожнього стека: {e}")
    
    try:
        empty_stack.peek()
    except IndexError as e:
        print(f"   Спроба peek() з порожнього стека: {e}")
    
    # Тест 9: Використання стека як булевого значення
    print("\n9. Використання стека в умовах:")
    stack1 = Stack()
    stack2 = Stack()
    stack2.push(100)
    
    print(f"   Порожній стек: if stack → {bool(stack1)}")
    print(f"   Непорожній стек: if stack → {bool(stack2)}")
