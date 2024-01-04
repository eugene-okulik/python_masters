class SchoolTextbook:
    def __init__(self, title, author, pages, subject, school_class, has_exercises):
        self.title = title
        self.author = author
        self.pages = pages
        self.subject = subject
        self.school_class = school_class
        self.has_exercises = has_exercises

# Создание нескольких экземпляров учебников
textbook1 = SchoolTextbook("Алгебра", "Иванов", 200, "Математика", 9, True)
textbook2 = SchoolTextbook("История", "Петров", 150, "История", 10, False)
textbook3 = SchoolTextbook("География", "Сидоров", 180, "География", 8, True)

# Пометить один учебник как зарезервированный
textbook1.is_reserved = True

# Печать деталей каждого учебника
textbooks = [textbook1, textbook2, textbook3]
for textbook in textbooks:
    if hasattr(textbook, 'is_reserved') and textbook.is_reserved:
        print(f"Название: {textbook.title}, Автор: {textbook.author}, Страниц: {textbook.pages}, "
              f"Предмет: {textbook.subject}, Класс: {textbook.school_class}, Зарезервирована")
    else:
        print(f"Название: {textbook.title}, Автор: {textbook.author}, Страниц: {textbook.pages}, "
              f"Предмет: {textbook.subject}, Класс: {textbook.school_class}")