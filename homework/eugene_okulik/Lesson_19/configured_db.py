import mysql.connector as mysql
import creds


with mysql.connect(
    user=creds.user,
    passwd=creds.passwd,
    host=creds.host,
    port=creds.port,
    database=creds.database
) as db:
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM students')
    data1 = cursor.fetchall()
    print(data1)
    for line in data1:
        print(line['second_name'])
