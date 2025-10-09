# Підрахунок унікальних слів у реченні
def count_words(sentence):
    """
    Приймає речення (рядок) і повертає словник з унікальними словами
    як ключами та кількістю їх входжень як значеннями.
    """
    # Розбиваємо речення на слова та приводимо до нижнього регістру
    words = sentence.lower().split()

    # Створюємо словник для підрахунку
    word_count = {}
    for word in words:
        # Видаляємо розділові знаки з кінців слова
        word = word.strip('.,!?;:"')
        if word:  # Якщо слово не порожнє
            word_count[word] = word_count.get(word, 0) + 1

    return word_count

# Тестування Task 1
print("=" * 50)
print("TASK 1 - Підрахунок слів у реченні")
print("=" * 50)
test_sentence = "Hello world! This is a test. Hello, this is another test."
result1 = count_words(test_sentence)
print(f"Речення: {test_sentence}")
print(f"Результат: {result1}")
print()