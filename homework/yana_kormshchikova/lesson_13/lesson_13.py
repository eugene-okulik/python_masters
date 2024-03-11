class Book:
    def __init__(self, author, title, pages_number, isbn, text=True, pages_material='бумага'):
        self.pages_material = pages_material
        self.text = text
        self.title = title
        self.author = author
        self.pages_number = pages_number
        self.isbn = isbn
        self.reservation = False

    def is_reserved(self):
        self.reservation = True

    def book_info(self):
        if self.reservation:
            print(f'Название: {self.title}, автор: {self.author}, количество страниц: {self.pages_number}, '
                  f'материал: {self.pages_material}, зарезервирована')
        else:
            print(f'Название: {self.title}, автор: {self.author}, количество страниц: {self.pages_number}, '
                  f'материал: {self.pages_material}')


book_1 = Book('Булгаков Михаил Афанасьевич', 'Мастер и Маргарита', 512, '978-5-17-149175-8')
book_2 = Book('Достоевский Федор Михайлович', 'Преступление и наказание', 672, '978-5-17-090630-7')
book_3 = Book('Джейн Остин', 'Гордость и предубеждение', 400, '978-5-392-40306-6')
book_4 = Book('Уайльд Оскар', 'Портрет Дориана Грея', 368, '978-5-389-04564-4')
book_5 = Book('Пушкин Александр Сергеевич', 'Евгений Онегин', 448, '978-5-389-04903-1')

book_2.is_reserved()
book_5.is_reserved()

book_1.book_info()
book_2.book_info()
book_3.book_info()
book_4.book_info()
book_5.book_info()


class SchoolBook(Book):

    def __init__(self, author, title, pages_number, isbn, subject, school_class, text=True, pages_material='бумага'):
        super().__init__(author, title, pages_number, isbn, text=True, pages_material='бумага')
        self.subject = subject
        self.school_class = school_class
        self.has_tasks = False

    def has_exercise(self):
        self.has_tasks = True

    def school_book_info(self):
        if self.reservation:
            print(f'Название: {self.title}, автор: {self.author}, страниц: {self.pages_number}, '
                  f'предмет: {self.subject}, класс: {self.school_class}, зарезервирована')
        else:
            print(f'Название: {self.title}, автор: {self.author}, страниц: {self.pages_number}, '
                  f'предмет: {self.subject}, класс: {self.school_class}')


school_book_1 = SchoolBook('Поляков, Мерзляк', 'Алгебра и начала математического анализа', 480,
                           '978-5-360-12203-6', 'Алгебра', '10')
school_book_2 = SchoolBook('И. Л. Андреев ', 'История России. Конец XVII-XVIII век', 269,
                           '9785090878456', 'История', '8')
school_book_3 = SchoolBook('Пасечник В. В., Каменский А. А.', 'Биология', 208,
                           '978-5-09-088223-1', 'Биология', '9')

school_book_1.is_reserved()

school_book_1.school_book_info()
school_book_2.school_book_info()
school_book_3.school_book_info()
