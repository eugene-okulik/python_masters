import mysql.connector as mysql


with mysql.connect(
    user='st5',
    passwd='AVNS_FT_L0boKoYMtLhsDsAC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st5'
) as db:
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM students')
    data1 = cursor.fetchall()
    # print(data1)
    # for line in data1:
    #     print(line['second_name'])

    cursor.execute('select * FROM students WHERE id = 4')
    data2 = cursor.fetchone()
    # print(data2)
    # print(data2['second_name'])

    # cursor = db.cursor(dictionary=True)
    # query = 'SELECT * FROM students LIMIT {0}, {1}'
    # limit, offset = 2, 0
    # while True:
    #     cursor.execute(query.format(offset, limit))
    #     data3 = cursor.fetchall()
    #     if not data3:
    #         break
    #     print(offset, data3)
    #     offset = offset + limit

    # user, password = 'admin', 'qwety'
    # f'SELECT * FROM users WHERE login = {user} and password = {password}'

    # name = input('enter name: ')
    # last_name = input('enter last name: ')
    # # query_student = f"SELECT * FROM students WHERE name = '{name}' and second_name = '{last_name}'"
    # query_student = f"SELECT * FROM students WHERE name = %s and second_name = %s"
    # cursor.execute(query_student, (name, last_name))
    # print(cursor.fetchall())

    insert_query = 'INSERT INTO students (name, second_name) VALUES (%s, %s)'
    cursor.execute(insert_query, ('Ivan', 'Ivanov'))
    student_id = cursor.lastrowid
    db.commit()
    print(student_id)
    cursor.executemany(
        insert_query,
        [
            ('Petr', 'Petrov'),
            ('Sidor', 'Sidorova')
        ]
    )
    db.commit()

query = '''
SELECT * from students s
left join `groups` g
on s.group_id = g.id
left JOIN books b
on s.id = b.taken_by_student_id
WHERE g.title = 'QT42'
'''
