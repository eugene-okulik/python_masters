import csv
import os
import mysql.connector as mysql
import dotenv

dotenv.load_dotenv()

''' TODO:
В папке /homework/eugene_okulik/Lesson_19/hw_data
лежит csv файл. Файл никуда не копируйте и не переносите.
Прочитайте этот файл с помощью модуля csv и проверьте есть ли те данные,
которые там перечислены, в нашей базе данных.'''

current_path = os.path.dirname(__file__)
root_path = os.path.dirname(os.path.dirname(current_path))
file_path = os.path.join(root_path, 'eugene_okulik', 'Lesson_19', 'hw_data', 'db_data.csv')

with open(file_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    content = []
    for row in file_data:
        content.append(row)

'''
При подключении к базе данных не прописывайте данные подключения в коде,
а воспользуйтесь подходом .env c такими переменными:
DB_USER,
DB_PASSW,
DB_HOST,
DB_PORT,
DB_NAME.
Я на своем компе уже настроил этим переменные, так что, если все сделаем одинаковые названия,
будет работать всё универсально'''

with mysql.connect(
        user=os.getenv('DB_USER'),
        passwd=os.getenv('DB_PASSW'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        database=os.getenv('DB_NAME')
) as db:
    cursor = db.cursor(dictionary=True)

    '''
    В результате сравнения, если обнаружится, что каких-то данных, которые есть в файле, нет в базе данных,
    распечатайте строки csv файла, данные из которых не были найдены.
    '''

    for record in content:
        fname = record['name']
        lname = record['second_name']
        group = record['group_title']
        book = record['book_title']
        subject = record['subject_title']
        lesson = record['lesson_title']
        grade = record['mark_value']

        print(f"\033[0;37;40m Checking: {fname} {lname}, {group}, {book}, {subject}, {lesson}, {grade}")

        # TODO: Name check
        name_check_query = 'select * from students WHERE name like %s and second_name like %s'
        cursor.execute(name_check_query, (fname, lname))
        name_request = cursor.fetchall()
        try:
            student_fname = name_request[0]['name']
            student_lname = name_request[0]['second_name']
        except IndexError:
            print(f"\033[1;31;40m Not found: {fname} {lname} in DB!")
            continue

        # TODO: Group check
        group_check_query = 'select * from `groups` where id = %s'
        user_group_id = name_request[0]['group_id']
        cursor.execute(group_check_query, (user_group_id,))
        group_request = cursor.fetchall()
        try:
            group_name = group_request[0]['title']
        except IndexError:
            print(f"\033[1;31;40m No record for {fname} {lname} been a member of group '{group}' in DB!")

        # TODO: Book borrowing check
        book_taken_query = 'select * from books where title like %s and taken_by_student_id like %s'
        student_id = name_request[0]['id']
        cursor.execute(book_taken_query, (book, student_id))
        book_request = cursor.fetchall()
        try:
            borrowed_book_id = book_request[0]['id']
        except IndexError:
            print(f"\033[1;31;40m There is no record that '{book}' has been taken by {fname} {lname}!")

        # TODO: Subject check
        subject_check_query = 'select * from subjets where title like %s'
        cursor.execute(subject_check_query, (subject,))
        subject_request = cursor.fetchall()
        try:
            subject_id = subject_request[0]['id']
        except IndexError:

            print(f"\033[1;31;40m There is no subject '{subject}' in DB!")

        # TODO: Lesson check
        lesson_check_query = 'select * from lessons where title = %s and subject_id = %s'
        cursor.execute(lesson_check_query, (lesson, subject_id))
        lesson_request = cursor.fetchall()
        try:
            lesson_id = lesson_request[0]['id']
        except IndexError:
            print(f"\033[1;31;40m There is no specified lesson '{lesson}' for {subject} in DB!")

        # TODO: Grade check
        grade_check_query = 'select * from marks where value like %s and lesson_id like %s and student_id like %s'
        cursor.execute(grade_check_query, (grade, lesson_id, student_id))
        student_grade = cursor.fetchall()
        try:
            lesson_grade = student_grade[0]['value']
        except IndexError:
            print(f"\033[1;31;40m There is no such grade as '{grade}' "
                  f"for {lesson} of {subject} of {fname} {lname} in DB!")

        print("\033[1;32;40m Ok\n")
    print("\033[1;34;40m Check finished.")
