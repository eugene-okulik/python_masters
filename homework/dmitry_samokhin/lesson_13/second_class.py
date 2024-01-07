import first_class


class SchoolBook(first_class.Book):
    def __init__(
        self,
        material,
        has_text,
        title,
        author,
        num_pages,
        isbn,
        reserved,
        subject,
        school_class,
        has_exercises,
    ):
        super().__init__(material, has_text, title, author, num_pages, isbn, reserved)
        self.subject = subject
        self.school_class = school_class
        self.has_exercises = has_exercises


school_book_1 = SchoolBook(
    "Бумага",
    True,
    "Математика 5 класс",
    "Иванов",
    200,
    "978-5-699-31457-2",
    False,
    "Математика",
    5,
    True,
)
school_book_2 = SchoolBook(
    "Бумага",
    True,
    "История 7 класс",
    "Петров",
    180,
    "978-5-699-31457-3",
    False,
    "История",
    7,
    False,
)
school_book_3 = SchoolBook(
    "Бумага",
    True,
    "География 9 класс",
    "Сидоров",
    250,
    "978-5-699-31457-4",
    False,
    "География",
    9,
    True,
)
school_book_4 = SchoolBook(
    "Бумага",
    True,
    "Физика 10 класс",
    "Кузнецов",
    220,
    "978-5-699-31457-5",
    False,
    "Физика",
    10,
    True,
)
school_book_5 = SchoolBook(
    "Бумага",
    True,
    "Литература 8 класс",
    "Смирнова",
    190,
    "978-5-699-31457-6",
    False,
    "Литература",
    8,
    False,
)

school_book_5.reserved = True


def print_book_details(book):
    reserved_status = "зарезервирована" if book.reserved else ""
    print(
        f"Название: {book.title}, Автор: {book.author}, страниц: {book.num_pages}, "
        f"материал: {book.material}, предмет: {book.subject}, {reserved_status}"
    )


print_book_details(school_book_1)
print_book_details(school_book_2)
print_book_details(school_book_3)
print_book_details(school_book_4)
print_book_details(school_book_5)
