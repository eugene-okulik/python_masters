import mysql.connector as mysql

"""
Все действия с базой данных из прошлого домашнего задания напишите с помощью Python.
При получении данных, распечатывайте эти данные.
"""

with mysql.connect(
        user='st5',
        password='AVNS_FT_L0boKoYMtLhsDsAC',
        host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
        database='st5',
        port=25060
) as db:
    cursor = db.cursor(dictionary=True)

    """
    --Задание
    --Создайте в базе данных полный набор информации о студенте, заполнив все таблички:
    --
    --Создайте студента (student)
    """
    fname = 'Draco'
    lname = 'Malfoy'
    create_user_query = 'INSERT INTO students (name, second_name) values (%s, %s)'
    cursor.execute(create_user_query, (fname, lname))
    student_id = cursor.lastrowid
    db.commit()
    print("Student Created\n")
    #
    # --Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
    create_book_query = 'INSERT INTO books (title, taken_by_student_id) values (%s, %s)'
    cursor.executemany(create_book_query, [
        ('The Standard Book of Spells', student_id),
        ('Quintessence: A Quest', student_id),
        ('The Dark Forces: A Guide to Self-Protection', student_id),
        ('Break with a Banshee', student_id),
        ('Gadding with Ghouls', student_id),
        ('Holidays with Hags', student_id),
        ('Travels with Trolls', student_id),
        ('Voyages with Vampires', student_id),
        ('Wanderings with Werewolves', student_id),
        ('Year with the Yeti', student_id),
        ('One Thousand Magical Herbs and Fungi', student_id),
        ('Winogrand\'s Wondrous Water Plants', student_id),
        ('Flesh-Eating Trees of the World', student_id),
        ('Magical Drafts and Potions', student_id),
        ('A Collection of Above Three Hundred Receipts in Cookery, Physick, and Surgery', student_id),
        ('A Guide to Advanced Transfiguration', student_id)
    ])
    book_id = cursor.lastrowid
    db.commit()
    print("Books Created\n")

    # --Создайте группу (group) и определите своего студента туда
    create_student_group_query = 'INSERT INTO `groups` (title, start_date, end_date) values (%s, %s, %s)'
    cursor.execute(create_student_group_query, ('Slytherin', '1st of September', '30th of June'))
    student_group_id = cursor.lastrowid
    db.commit()
    print("Student Group Created\n")

    set_student_to_group_query = 'UPDATE students SET group_id = %s where name like %s and second_name like %s'
    cursor.execute(set_student_to_group_query, (student_group_id, fname, lname))
    db.commit()
    print("Student assigned to Created Group\n")
    #
    # --Создайте несколько учебных предметов (subjects)
    # -- ATTENTION! The table has name 'SUBJETS' instead of 'subjeCts'!!! Letter 'C' is missing!!!
    create_subject_query = 'INSERT INTO subjets (title) VALUES (%s)'
    cursor.execute(create_subject_query, ('Quidditch',))
    subject_id1 = cursor.lastrowid
    print("Sunject 1 Created\n")
    cursor.execute(create_subject_query, ('Wizard\'s chess',))
    subject_id2 = cursor.lastrowid
    db.commit()
    print("Sunject 2 Created\n")

    # --Создайте по два занятия для каждого предмета (lessons)
    create_lessons_query = 'insert into lessons (title, subject_id) values (%s, %s)'
    cursor.executemany(create_lessons_query, [
        ('Monday 16.00', subject_id1),
        ('Thursday 16.00', subject_id1),
        ('Tuesday 16.00', subject_id2),
        ('Friday 16.00', subject_id2)
    ])
    lesson_id = cursor.lastrowid
    db.commit()
    print("Lessons Created\n")

    # --Поставьте своему студенту оценки (marks) для всех созданных вами занятий
    # -- Лучше испольщовать 'GRADES' для оценок!!!
    #
    lessons_id = []
    for lesson in range(lesson_id, lesson_id + 4):
        lessons_id.append(lesson)

    set_lesson_grade_querry = 'insert into marks (value, lesson_id, student_id) values (%s, %s, %s)'
    cursor.executemany(set_lesson_grade_querry, [
        ('Outstanding', lessons_id[0], student_id),
        ('Acceptable', lessons_id[1], student_id),
        ('Exceeds Expectations', lessons_id[2], student_id),
        ('Poor', lessons_id[3], student_id)
    ])
    db.commit()
    print("Grades Set up\n")

    # --Получите информацию из базы данных:
    # --Все оценки студента
    get_all_grades_query = 'select value from marks where student_id = %s'
    cursor.execute(get_all_grades_query, (student_id,))
    student_grades = cursor.fetchall()
    print(f'Student {fname} {lname} grades: {student_grades}')
    print()
    #
    # --Все книги, которые находятся у студента
    #
    get_all_student_books_query = 'select title from books where taken_by_student_id = %s'
    cursor.execute(get_all_student_books_query, (student_id,))
    student_books = cursor.fetchall()
    print(f'Student {fname} {lname} books: {student_books}')
    print()
    # --Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов
    # --(всё одним запросом с использованием Join)
    get_all_student_info = '''
       select * from students
    join `groups` on students.group_id = groups.id
    join books on students.id = books.taken_by_student_id
    join marks on marks.student_id = students.id
    join lessons on marks.lesson_id = lessons.id
    join subjets on lessons.subject_id = subjets.id
    where name like %s and second_name like %s'''
    cursor.execute(get_all_student_info, (fname, lname))
    all_student_info = cursor.fetchall()
    print(f'Student {fname} {lname} all info: {all_student_info}')
    print('Finished')
