from stack import Stack


def reverse_string_with_stack():
    """Читає послідовність символів і виводить їх у зворотному порядку"""
    s = Stack()

    # Читаємо введення від користувача
    text = input("Введіть послідовність символів: ")

    # Додаємо кожен символ у стек
    for char in text:
        s.push(char)

    # Виводимо символи у зворотному порядку
    reversed_text = ""
    while not s.is_empty():
        reversed_text += s.pop()

    print(f"Зворотний порядок: {reversed_text}")
    return reversed_text


if __name__ == "__main__":
    reverse_string_with_stack()