import mysql.connector as mysql
import os
import dotenv

dotenv.load_dotenv()


with mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
) as db:
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM students')
    data1 = cursor.fetchall()
    print(data1)
    for line in data1:
        print(line['second_name'])
