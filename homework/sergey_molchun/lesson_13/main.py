"""Библиотека
Первый класс
Создайте класс book с атрибутами:

материал страниц
наличие текста
название книги
автор
кол-во страниц
ISBN

флаг зарезервирована ли книга или нет (True/False).
Какие-то из атрибутов будут общими для всех книг (материал, наличие текста), какие-то индивидуальными.
"""


class Book:
    def __init__(self, title, author, total_pages, isbn=0, paper_material="150mg", text_is_present=True,
                 is_reserved=False):
        self.page_binding = "Number_7"
        self.title = title
        self.author = author
        if not isinstance(total_pages, int):
            raise ValueError("total_pages must be an integer")
        self.total_pages = total_pages
        self.ISBN = isbn
        self.paper_material = paper_material
        self.text_is_present = text_is_present
        self.is_reserved = is_reserved


"""Создайте несколько (штук 5) экземпляров разных книг."""

book1 = Book("The Hobbit", "J.R.R. Tolkien", 300, 9780007525508)
book2 = Book("LOTR, Fellowship of the ring", "J.R.R. Tolkien", 600, 9780007525510, '200mg')
book3 = Book("LOTR, Two towers", "J.R.R. Tolkien", 550, 9780007525512, '200mg')
book4 = Book("LOTR, Return of the king", "J.R.R. Tolkien", 650, 9780007525514, '200mg')
book5 = Book("Silmarillion", "J.R.R. Tolkien", 900, 9780007525516, '180mg')

"""
После создания пометьте одну книгу как зарезервированную.
"""
book5.is_reserved = True

library = [book1, book2, book3, book4, book5]

"""
Распечатайте детали о каждой книге в таком виде:
Если книга зарезервирована:
Название: Идиот, Автор: Достоевский, страниц: 500, материал: бумага, зарезервирована
"""
"""
если не зарезервирована:
Название: Идиот, Автор: Достоевский, страниц: 500,  материал: бумага
"""
print('\nSchool hobby library:')

for book in library:
    if book.is_reserved:
        print(f"Title: {book.title}, Author: {book.author}, Pages: {book.total_pages}, "
              f"Page material: {book.paper_material}, Reserved!")
    else:
        print(f"Title: {book.title}, Author: {book.author}, Pages: {book.total_pages}, "
              f"Page material: {book.paper_material}.")

"""
Второй класс
Создайте дочерний класс для первого. Это будет класс для школьных учебников. В нем будут дополнительные атрибуты:
предмет (типа математика, история, география),
класс (школьный класс, для которого этот учебник)(осторожно с названием переменной. class - зарезервированное слово),
наличие заданий (bool)
"""
print('\nSchool textbook library:')


class SchoolBook(Book):
    def __init__(self, title, grade, author, total_pages, isbn=0, paper_material="150mg", text_is_present=True,
                 exercises=True, is_reserved=False):
        super().__init__(title, author, total_pages, isbn=0, paper_material="150mg", text_is_present=True,
                         is_reserved=False)
        # self.subject = subject
        self.grade = grade
        self.exercises = exercises


"""
Создайте несколько экземпляров учебников.
После создания пометьте один учебник как зарезервированный.
"""
school_book1 = SchoolBook("Algebra", 11, "Puankare", 200, 1234567890)
school_book2 = SchoolBook("History", 10, "Morozov", 350, 1234567891)
school_book3 = SchoolBook("Geography", 8, "Domeiko", 150, 1234567892)
school_book4 = SchoolBook("Geometry", 9, "Evklid", 300, 1234567893)

school_books = [school_book1, school_book2, school_book3, school_book4]

school_book3.is_reserved = True
school_book4.is_reserved = True

"""
Распечатайте детали о каждом учебнике в таком виде: Если учебник зарезервирован:
Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9, зарезервирована
если не зарезервирован:

Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9"""

for book in school_books:
    if book.is_reserved:
        print(f"Title: {book.title}, Grade: {book.grade}, Author: {book.author}, Pages: {book.total_pages}, "
              f"Reserved!")
    else:
        print(f"Title: {book.title}, Grade: {book.grade}, Author: {book.author}, Pages: {book.total_pages}")

print(school_book1.page_binding)
