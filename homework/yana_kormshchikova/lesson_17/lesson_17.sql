--Создайте в базе данных полный набор информации о студенте, заполнив все таблички:
--Создайте студента (student)
INSERT INTO students (name, second_name) VALUES ('John', 'Doe')


--Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
INSERT INTO books (title, taken_by_student_id) VALUES ('Мастер и Маргарита', 54)
INSERT INTO books (title, taken_by_student_id) VALUES ('Алые паруса', 54)


--Создайте группу (group) и определите своего студента туда
INSERT INTO `groups` (title, start_date, end_date) VALUES('santsib', '1 of March', '30 of April')
UPDATE students SET group_id =30  WHERE id =54

--Создайте несколько учебных предметов (subjects)
INSERT INTO subjets (title) VALUES
('Astronomy'),
('Economy'),
('Physics')

--Создайте по два занятия для каждого предмета (lessons)
INSERT INTO lessons (title, subject_id) VALUES
('Monday - 8 a.m.', 63),
('Wednesday - 4 p.m.', 63),
('Tuesday - 10 a.m.', 64),
('Friday - 1 p.m.', 64),
('Thursday - 7 p.m.', 65),
('Saturday - 2 p.m.', 65)

--Поставьте своему студенту оценки (marks) для всех созданных вами занятий
INSERT INTO marks (value, lesson_id, student_id) VALUES
('A (Excellent)', 63, 54),
('C (Satisfactory)', 64, 54),
('B (Good)', 65, 54)

--Получите информацию из базы данных:
--Все оценки студента
SELECT value FROM marks WHERE student_id = 54

--Все книги, которые находятся у студента
SELECT title FROM books WHERE taken_by_student_id = 54
--Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий
-- и предметов (всё одним запросом с использованием Join)

SELECT *
FROM students
JOIN books ON students.id=books.taken_by_student_id
JOIN `groups` ON students.group_id = groups.id
JOIN marks ON marks.student_id = students.id
JOIN lessons ON marks.lesson_id = lessons.id
JOIN subjets ON lessons.subject_id = subjets.id
WHERE name = 'John' AND second_name = 'Doe';