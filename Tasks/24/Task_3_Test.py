# Тест для Stack
def test_stack_get():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)

    print("Stack до:", s)

    # Знаходимо елемент 2
    found = s.get_from_stack(2)
    print(f"Знайдено: {found}")
    print("Stack після:", s)

    # Спроба знайти неіснуючий елемент
    try:
        s.get_from_stack(10)
    except ValueError as e:
        print(f"Помилка: {e}")


# Тест для Queue
def test_queue_get():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)

    print("Queue до:", q)

    # Знаходимо елемент 3
    found = q.get_from_queue(3)
    print(f"Знайдено: {found}")
    print("Queue після:", q)

    # Спроба знайти неіснуючий елемент
    try:
        q.get_from_queue(10)
    except ValueError as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    test_stack_get()
    print("\n" + "=" * 50 + "\n")
    test_queue_get()