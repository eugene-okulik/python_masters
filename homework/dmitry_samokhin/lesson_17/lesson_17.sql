-- Создайте студента (student)
INSERT INTO students(name, second_name) VALUES('Dmitriy', 'Samohin')

-- Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
INSERT INTO books(title, taken_by_student_id) VALUES('Разработка в системе «1С:Предприятие 8.3»', 20)
INSERT INTO books(title, taken_by_student_id) VALUES('Изучаем Python» — Марк Лутц', 20)
INSERT INTO books(title, taken_by_student_id) VALUES('ремонт ваз 2114', 20)

-- Создайте группу (group) и определите своего студента туда
INSERT INTO "groups"(title, start_date, end_date) VALUES('Чуднашки', '1 декабря', '31 декабря')
UPDATE students SET group_id = 8 WHERE id = 20

-- Создайте несколько учебных предметов (subjects)
INSERT INTO subjets(title) VALUES('Инфоциганство'), ('Питон за 3 часа до профессионала'), ('Читаем рэп')

-- Создайте по два занятия для каждого предмета (lessons)
INSERT INTO lessons(title, subject_id) VALUES
  -> ('Понедельник 10:00', 26),
  -> ('Вторник 10:00', 26),
  -> ('Понедельник 11:00', 27),
  -> ('Вторник 11:00', 27),
  -> ('Понедельник 12:00', 28),
  -> ('Вторник 12:00', 28);

-- Поставьте своему студенту оценки (marks) для всех созданных вами занятий
INSERT INTO marks(value, lesson_id, student_id) VALUES('Отлично', 26, 20), ('Нормально', 27, 20), ('Лучший', 28, 20)

-- Все оценки студента
SELECT * FROM marks WHERE student_id = 20

-- Все книги, которые находятся у студента
SELECT * FROM books WHERE taken_by_student_id = 20

-- Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов (всё одним -- запросом с использованием Join)

 SELECT *
  -> FROM students
  -> JOIN books ON students.id=books.taken_by_student_id
  -> JOIN "groups" ON students.group_id = groups.id
  -> JOIN marks ON marks.student_id = students.id
  -> JOIN lessons ON marks.lesson_id = lessons.id
  -> JOIN subjets ON lessons.subject_id = subjets.id
  -> WHERE name = 'Dmitriy' AND second_name = 'Samohin';
