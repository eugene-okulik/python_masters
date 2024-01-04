class Book:
    def __init__(self, material, has_text, title, author, num_pages, isbn):
        self.material = material
        self.has_text = has_text
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.reserved = False

    def reserve(self):
        self.reserved = True

    def get_details(self):
        if self.reserved:
            print(f"Название: {self.title}, Автор: {self.author}, Страниц: {self.num_pages}, Материал: {self.material}, Зарезервирована")
        else:
            print(f"Название: {self.title}, Автор: {self.author}, Страниц: {self.num_pages}, Материал: {self.material}")


book1 = Book("Бумага", True, "Идиот", "Достоевский", 500, "978-5-17-043917-8")
book2 = Book("Бумага", True, "Преступление и наказание", "Достоевский", 400, "978-5-17-112406-5")
book3 = Book("Электронная", True, "1984", "Джордж Оруэлл", 328, "978-5-9902700-1-7")
book4 = Book("Бумага", False, "Алиса в стране чудес", "Льюис Кэрролл", 96, "978-5-389-08156-2")
book5 = Book("Электронная", True, "Великий Гэтсби", "Фрэнсис Скотт Фицджералд", 218, "978-5-9909495-9-6")

book1.reserve()
book1.get_details()
book2.get_details()
book3.get_details()
book4.get_details()
book5.get_details()
