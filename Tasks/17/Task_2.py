class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name, year, author):
        """Створює нову книгу та додає її до бібліотеки"""
        book = Book(name, year, author)
        self.books.append(book)

        # Додаємо автора до списку, якщо його ще немає
        if author not in self.authors:
            self.authors.append(author)

        return book

    def group_by_author(self, author):
        """Повертає всі книги певного автора"""
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        """Повертає всі книги певного року"""
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return f"Library(name='{self.name}', books={len(self.books)}, authors={len(self.authors)})"

    def __str__(self):
        return f"Library '{self.name}' with {len(self.books)} books and {len(self.authors)} authors"


class Book:
    total_books = 0  # Класова змінна для підрахунку всіх книг

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

        # Додаємо книгу до списку книг автора
        author.books.append(self)

        # Збільшуємо лічильник загальної кількості книг
        Book.total_books += 1

    def __repr__(self):
        return f"Book(name='{self.name}', year={self.year}, author='{self.author.name}')"

    def __str__(self):
        return f"'{self.name}' by {self.author.name} ({self.year})"


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f"Author(name='{self.name}', country='{self.country}', birthday='{self.birthday}')"

    def __str__(self):
        return f"{self.name} ({self.country}, born {self.birthday}) - {len(self.books)} books"


# Тестування
if __name__ == "__main__":
    # Створюємо авторів
    author1 = Author("J.K. Rowling", "UK", "1965-07-31")
    author2 = Author("Stephen King", "USA", "1947-09-21")

    # Створюємо бібліотеку
    library = Library("City Library")

    # Додаємо книги
    book1 = library.new_book("Harry Potter and the Philosopher's Stone", 1997, author1)
    book2 = library.new_book("Harry Potter and the Chamber of Secrets", 1998, author1)
    book3 = library.new_book("The Shining", 1977, author2)
    book4 = library.new_book("It", 1986, author2)

    print(library)
    print(f"Total books created: {Book.total_books}")
    print(f"\nBooks by {author1.name}:")
    for book in library.group_by_author(author1):
        print(f"  - {book}")

    print(f"\nBooks from 1997:")
    for book in library.group_by_year(1997):
        print(f"  - {book}")