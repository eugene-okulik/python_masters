import mysql.connector as mysql

with mysql.connect(
        user='st5',
        passwd='AVNS_FT_L0boKoYMtLhsDsAC',
        host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
        port=25060,
        database='st5'
) as db:
    cursor = db.cursor(dictionary=True)

    #  Создайте студента (student)

    create_user_query = 'INSERT INTO students (name, second_name) VALUES (%s, %s)'
    cursor.execute(create_user_query, ('Ann', 'Doe'))
    student_id = cursor.lastrowid
    db.commit()

    #  Создайте несколько книг (books) и укажите, что ваш созданный студент взял их

    create_book_query = 'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)'
    cursor.executemany(create_book_query, [
        ('Дневник Анны Франк', student_id),
        ('451° по Фаренгейту', student_id),
        ('Голодные игры', student_id),
        ('Ромео и Джульетта', student_id),
        ('Маленький принц', student_id)
    ])
    book_id = cursor.lastrowid
    db.commit()

    # Создайте группу (group) и определите своего студента туда

    create_group = 'INSERT INTO `groups` (title, start_date, end_date) VALUES(%s, %s, %s)'
    cursor.execute(create_group, ('new_group', '10 of March', '20 of May'))
    group_id = cursor.lastrowid
    db.commit()

    set_group_id_to_student = 'UPDATE students SET group_id = %s  WHERE id = %s'
    cursor.execute(set_group_id_to_student, (group_id, student_id))
    db.commit()

    # Создайте несколько учебных предметов (subjects)
    create_subjects = 'INSERT INTO subjets (title) VALUES (%s)'
    cursor.execute(create_subjects, ('Philosophy',))
    subj_1 = cursor.lastrowid
    cursor.execute(create_subjects, ('Maths',))
    subj_2 = cursor.lastrowid
    db.commit()

    # Создайте по два занятия для каждого предмета (lessons)

    create_lessons = 'INSERT INTO lessons (title, subject_id) VALUES (%s, %s)'
    cursor.executemany(create_lessons, [
        ('Monday - 10:05 a.m.', 66),
        ('Tuesday - 11:30 a.m.', 67),
        ('Thursday - 7:15 p.m.', 66),
        ('Saturday - 1:10 p.m.', 67)
    ])
    lesson_id = cursor.lastrowid
    print(lesson_id)
    db.commit()

    # Поставьте своему студенту оценки (marks) для всех созданных вами занятий

    create_marks = 'INSERT INTO marks (value, lesson_id, student_id) VALUES(%s, %s, %s)'
    cursor.executemany(create_marks, [
        ('A (Excellent)', lesson_id, student_id),
        ('C (Satisfactory)', lesson_id+1, student_id),
        ('B (Good)', lesson_id+2, student_id),
        ('B (Good)', lesson_id+3, student_id)
    ])
    db.commit()

    # Получите информацию из базы данных:
    # Все оценки студента

    get_student_grades = 'SELECT value FROM marks WHERE student_id = %s'
    cursor.execute(get_student_grades, (student_id,))
    grades = cursor.fetchall()
    print(grades)

    # Все книги, которые находятся у студента
    get_all_books = 'SELECT title FROM books WHERE taken_by_student_id = %s'
    cursor.execute(get_all_books, (student_id,))
    books = cursor.fetchall()
    print(books)

    # Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов (всё одним запросом с использованием Join)

    get_student_info = '''
    SELECT *
    FROM students
    JOIN books ON students.id = books.taken_by_student_id
    JOIN `groups` ON students.group_id = groups.id
    JOIN marks ON marks.student_id = students.id
    JOIN lessons ON marks.lesson_id = lessons.id
    JOIN subjets ON lessons.subject_id = subjets.id
    WHERE name = %s AND second_name = %s;
    '''
    cursor.execute(get_student_info, ('Ann', 'Doe'))
    student_info = cursor.fetchall()
    print(student_info)