import mysql.connector

with mysql.connector.connect(
    user="st5",
    passwd="AVNS_FT_L0boKoYMtLhsDsAC",
    host="db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com",
    port=25060,
    database="st5",
) as mydb:
    # Создание студента
    mycursor = mydb.cursor()
    mycursor.execute(
        "INSERT INTO students(name, second_name) VALUES('Dmitriy', 'Samohin')"
    )
    mydb.commit()

    # Создание книг и привязка их к студенту
    books = [
        ("Разработка в системе «1С:Предприятие 8.3»", 20),
        ("Изучаем Python» — Марк Лутц", 20),
        ("ремонт ваз 2114", 20),
    ]
    mycursor.executemany(
        "INSERT INTO books(title, taken_by_student_id) VALUES(%s, %s)", books
    )
    mydb.commit()

    # Создание группы и привязка студента к группе
    mycursor.execute(
        """INSERT INTO "groups"(title, start_date, end_date) VALUES('Чуднашки', '1 декабря', '31 декабря')"""
    )
    mydb.commit()
    mycursor.execute("UPDATE students SET group_id = 8 WHERE id = 20")
    mydb.commit()

    # Создание учебных предметов
    subjects = [
        ("Инфоциганство",),
        ("Питон за 3 часа до профессионала",),
        ("Читаем рэп",),
    ]
    mycursor.executemany("INSERT INTO subjets(title) VALUES(%s)", subjects)
    mydb.commit()

    # Создание занятий для каждого предмета
    lessons = [
        ("Понедельник 10:00", 26),
        ("Вторник 10:00", 26),
        ("Понедельник 11:00", 27),
        ("Вторник 11:00", 27),
        ("Понедельник 12:00", 28),
        ("Вторник 12:00", 28),
    ]
    mycursor.executemany(
        "INSERT INTO lessons(title, subject_id) VALUES(%s, %s)", lessons
    )
    mydb.commit()

    # Поставить студенту оценки для всех созданных занятий
    marks = [("Отлично", 26, 20), ("Нормально", 27, 20), ("Лучший", 28, 20)]
    mycursor.executemany(
        "INSERT INTO marks(value, lesson_id, student_id) VALUES(%s, %s, %s)", marks
    )
    mydb.commit()

    # Получить все оценки студента
    mycursor.execute("SELECT * FROM marks WHERE student_id = 20")
    marks_result = mycursor.fetchall()
    for mark in marks_result:
        print(mark)

    # Получить все книги, которые находятся у студента
    mycursor.execute("SELECT * FROM books WHERE taken_by_student_id = 20")
    books_result = mycursor.fetchall()
    for book in books_result:
        print(book)

    # Получить всю информацию о студенте: группа, книги, оценки с названиями занятий и предметов
    mycursor.execute(
        """
        SELECT *
        FROM students
        JOIN books ON students.id=books.taken_by_student_id
        JOIN "groups" ON students.group_id = groups.id
        JOIN marks ON marks.student_id = students.id
        JOIN lessons ON marks.lesson_id = lessons.id
        JOIN subjets ON lessons.subject_id = subjets.id
        WHERE name = 'Dmitriy' AND second_name = 'Samohin';
        """
    )
    student_info = mycursor.fetchall()
    for info in student_info:
        print(info)
