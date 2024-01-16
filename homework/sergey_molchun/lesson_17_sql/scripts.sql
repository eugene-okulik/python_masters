--Задание
--Создайте в базе данных полный набор информации о студенте, заполнив все таблички:
--
--Создайте студента (student)
INSERT INTO students (name, second_name) values ('Harry', 'Potter')


--Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
INSERT INTO books (title, taken_by_student_id) values ('Defence magic', 19)
INSERT INTO books (title, taken_by_student_id) values ('Offence magic', 19)
INSERT INTO books (title, taken_by_student_id) values ('Heal magic', 19)
INSERT INTO books (title, taken_by_student_id) values ('Curse magic', 19)
INSERT INTO books (title, taken_by_student_id) values ('Animal language potion', 19)
INSERT INTO books (title, taken_by_student_id) values ('Water breath potion', 19)
INSERT INTO books (title, taken_by_student_id) values ('Water magic', 19)

--Создайте группу (group) и определите своего студента туда
INSERT INTO `groups` (title, start_date, end_date) values ('Gryffindor', '1st of September', '30th of June')
UPDATE students SET group_id = 7 where name like 'Harry' and second_name like 'Potter'

--Создайте несколько учебных предметов (subjects)
-- ATTENTION! The table has name 'SUBJETS' instead of 'subjeCts'!!! Letter 'C' is missing!!!
INSERT INTO subjets (title)
VALUES
    ('Astronomy'),
    ('Charms'),
    ('Defence Against the Dark Arts'),
    ('Herbology'),
    ('History of Magic'),
    ('Potions'),
    ('Transfiguration'),
    ('Arithmancy'),
    ('Care of Magical Creatures'),
    ('Divination'),
    ('Muggle Studies'),
    ('Study of Ancient Runes'),
    ('Advanced Arithmancy Studies'),
    ('Alchemy'),
    ('Apparition'),
    ('Dark Arts'),
    ('Flying'),
    ('Art'),
    ('Field Studies'),
    ('Ghoul Studies'),
    ('Magical Theory'),
    ('Muggle Art'),
    ('Muggle Music'),
    ('Music'),
    ('Xylomancy');

--Создайте по два занятия для каждого предмета (lessons)
insert into lessons (title, subject_id)
values
    ('Monday 8.00', 1),
    ('Thursday 8.00', 1),
    ('Monday 9.00', 2),
    ('Thursday 9.00', 2),
    ('Monday 10.00', 3),
    ('Thursday 10.00', 3),
    ('Monday 11.00', 4),
    ('Thursday 11.00', 4),
    ('Monday 12.00', 5),
    ('Thursday 12.00', 5),
    ('Monday 13.00', 6),
    ('Thursday 13.00', 6),
    ('Monday 14.00', 7),
    ('Thursday 14.00', 7),
    ('Monday 15.00', 8),
    ('Thursday 15.00', 8);

insert into lessons (title, subject_id)
values
    ('Tuesday 8.00', 9),
    ('Friday 8.00', 9),
    ('Tuesday 9.00', 10),
    ('Friday 9.00', 10),
    ('Tuesday 10.00', 11),
    ('Friday 10.00', 11),
    ('Tuesday 11.00', 12),
    ('Friday 11.00', 12),
    ('Tuesday 12.00', 13),
    ('Friday 12.00', 13),
    ('Tuesday 13.00', 14),
    ('Friday 13.00', 14),
    ('Tuesday 14.00', 15),
    ('Friday 14.00', 15),
    ('Tuesday 15.00', 16),
    ('Friday 15.00', 16);

insert into lessons (title, subject_id)
values
    ('Wednesday 8.00', 17),
    ('Saturday 8.00', 17),
    ('Wednesday 9.00', 18),
    ('Saturday 9.00', 18),
    ('Wednesday 10.00', 19),
    ('Saturday 10.00', 19),
    ('Wednesday 11.00', 20),
    ('Saturday 11.00', 20),
    ('Wednesday 12.00', 21),
    ('Saturday 12.00', 21),
    ('Wednesday 13.00', 22),
    ('Saturday 13.00', 22),
    ('Wednesday 14.00', 23),
    ('Saturday 14.00', 23),
    ('Wednesday 15.00', 24),
    ('Saturday 15.00', 24),
    ('Wednesday 16.00', 25),
    ('Saturday 16.00', 25);


--Поставьте своему студенту оценки (marks) для всех созданных вами занятий
-- Лучше испольщовать 'GRADES' для оценок!!!

insert into marks (value, lesson_id, student_id)
    values
    ('Outstanding', 1, 19),
    ('Exceeds Expectations', 2, 19),
    ('Outstanding', 3, 19),
    ('Acceptable', 4, 19),
    ('Exceeds Expectations', 5, 19),
    ('Outstanding', 6, 19),
    ('Poor', 7, 19),
    ('Exceeds Expectations', 8, 19),
    ('Outstanding', 9, 19),
    ('Acceptable', 10, 19),
    ('Outstanding', 11, 19),
    ('Poor', 12, 19),
    ('Outstanding', 13, 19),
    ('Exceeds Expectations', 14, 19),
    ('Outstanding', 15, 19),
    ('Dreadful', 16, 19),
    ('Acceptable', 17, 19),
    ('Outstanding', 18, 19),
    ('Exceeds Expectations', 19, 19),
    ('Outstanding', 20, 19),
    ('Acceptable', 21, 19),
    ('Dreadful', 22, 19),
    ('Exceeds Expectations', 23, 19),
    ('Outstanding', 24, 19),
    ('Troll', 25, 19),
    ('Acceptable', 26, 19),
    ('Outstanding', 27, 19),
    ('Exceeds Expectations', 28, 19),
    ('Outstanding', 29, 19),
    ('Acceptable', 30, 19),
    ('Dreadful', 31, 19),
    ('Outstanding', 32, 19),
    ('Exceeds Expectations', 33, 19),
    ('Outstanding', 34, 19),
    ('Acceptable', 35, 19),
    ('Outstanding', 36, 19),
    ('Exceeds Expectations', 37, 19),
    ('Outstanding', 38, 19),
    ('Troll', 39, 19),
    ('Exceeds Expectations', 40, 19),
    ('Acceptable', 41, 19),
    ('Dreadful', 42, 19),
    ('Outstanding', 43, 19),
    ('Outstanding', 44, 19),
    ('Exceeds Expectations', 45, 19),
    ('Acceptable', 46, 19),
    ('Poor', 47, 19),
    ('Outstanding', 48, 19),
    ('Acceptable', 49, 19),
    ('Exceeds Expectations', 45, 19);


--Получите информацию из базы данных:
--
--Все оценки студента
select value from marks where student_id = 19

--Все книги, которые находятся у студента
select title from books where taken_by_student_id = 19

--Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов
--(всё одним запросом с использованием Join)
   select * from students
join `groups` on students.group_id = groups.id
join books on students.id = books.taken_by_student_id
join marks on marks.student_id = students.id
join lessons on marks.lesson_id = lessons.id
join subjets on lessons.subject_id = subjets.id
where name like 'Harry' and second_name like 'Potter'

--Все запросы, которые сделаете, сохраняйте в файлик с расширением .txt или .sql, и сдавайте как обычно.

