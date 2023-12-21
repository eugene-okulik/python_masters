class Book:
    def __init__(self, material, has_text, title, author, num_pages, isbn, reserved):
        self.material = material
        self.has_text = has_text
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.reserved = reserved


# Создание экземпляров книг
book1 = Book(
    "Бумага",
    True,
    "Война и мир",
    "Лев Толстой",
    1225,
    "978-5-699-31457-7",
    False,
)
book2 = Book(
    "Бумага",
    True,
    "Преступление и наказание",
    "Федор Достоевский",
    671,
    "978-5-699-31457-8",
    False,
)
book3 = Book(
    "Электронный",
    True,
    "1984",
    "Джордж Оруэлл",
    328,
    "978-5-699-31457-9",
    False,
)
book4 = Book(
    "Бумага",
    True,
    "Мастер и Маргарита",
    "Михаил Булгаков",
    384,
    "978-5-699-31457-0",
    False,
)
book5 = Book(
    "Бумага",
    True,
    "Анна Каренина",
    "Лев Толстой",
    864,
    "978-5-699-31457-1",
    False,
)

# Пометка одной книги как зарезервированной
book3.reserved = True


# Функция для печати деталей о книге
def print_book_details(book):
    reserved_status = "зарезервирована" if book.reserved else ""
    print(
        f"Название: {book.title}, Автор: {book.author}, страниц: {book.num_pages}, "
        f"материал: {book.material}, {reserved_status}"
    )


print_book_details(book1)
print_book_details(book2)
print_book_details(book3)
print_book_details(book4)
print_book_details(book5)
