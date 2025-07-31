CREATE TABLE university_courses
(
    id            SERIAL PRIMARY KEY,
    course_name   VARCHAR(50),
    department_id INT
);


CREATE TABLE university_departments
(
    id              SERIAL PRIMARY KEY,
    department_name VARCHAR(50)
);

CREATE TABLE universities
(
    id       SERIAL PRIMARY KEY,
    uni_name VARCHAR(50)
);

INSERT INTO universities (uni_name)
SELECT 'Высшая Школа Экономики'
UNION
SELECT 'МГУ имени М. В. Ломоносова'
UNION
SELECT 'МГТУ имени Н. Э. Баумана'
;


INSERT INTO university_departments(department_name)
SELECT 'Математика'
UNION
SELECT 'Искусство'
UNION
SELECT 'Экономика'
UNION
SELECT 'Философия';

DROP TABLE university_courses;

INSERT INTO university_courses(course_name, department_id)
SELECT 'Античное искусство', 1
UNION
SELECT 'Современное искусство', 1
UNION
SELECT 'Макроэкономика', 2
UNION
SELECT 'Православная экономика', 2
UNION
SELECT 'Античная философия', 3
UNION
SELECT 'Прогрессивная философия', 3
UNION
SELECT 'Примитивная математика', 4
UNION
SELECT 'Высшая математика', 4


CREATE TABLE students
(
    id            SERIAL PRIMARY KEY,
    full_name     VARCHAR(100),
    uni_course_id INT
);

-- Чат гпт сгенерил - мне лень было все придумывать студентов, но он тоже заленился =)
INSERT INTO students (full_name, uni_course_id)
VALUES
-- Для курса 1
('Студент 1 курса 1', 1),
('Студент 2 курса 1', 1),
('Студент 3 курса 1', 1),
-- Для курса 2
('Студент 1 курса 2', 2),
('Студент 2 курса 2', 2),
('Студент 3 курса 2', 2),
-- Для курса 3
('Студент 1 курса 3', 3),
('Студент 2 курса 3', 3),
('Студент 3 курса 3', 3),
-- Для курса 4
('Студент 1 курса 4', 4),
('Студент 2 курса 4', 4),
('Студент 3 курса 4', 4),
-- Для курса 5
('Студент 1 курса 5', 5),
('Студент 2 курса 5', 5),
('Студент 3 курса 5', 5),
-- Для курса 6
('Студент 1 курса 6', 6),
('Студент 2 курса 6', 6),
('Студент 3 курса 6', 6),
-- Для курса 7
('Студент 1 курса 7', 7),
('Студент 2 курса 7', 7),
('Студент 3 курса 7', 7),
-- Для курса 8
('Студент 1 курса 8', 8),
('Студент 2 курса 8', 8),
('Студент 3 курса 8', 8);


BEGIN;
DROP TABLE students;
DROP TABLE universities;
DROP TABLE university_courses;
DROP TABLE university_departments;
COMMIT;

-- Новая попытка
-- Таблицы словарей
CREATE TABLE d_universities
(
    id   SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);


CREATE TABLE d_departments
(
    id   SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE d_courses
(
    id   SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE d_students
(
    id        SERIAL PRIMARY KEY,
    full_name VARCHAR(100)
);

-- Заполняем
INSERT INTO d_universities (name)
SELECT 'Высшая Школа Экономики'
UNION
SELECT 'МГУ имени М. В. Ломоносова'
UNION
SELECT 'МГТУ имени Н. Э. Баумана';

INSERT INTO d_departments(name)
SELECT 'Математика'
UNION
SELECT 'Искусство'
UNION
SELECT 'Экономика'
UNION
SELECT 'Философия';

INSERT INTO d_courses(name)
SELECT 'Античное искусство'
UNION
SELECT 'Современное искусство'
UNION
SELECT 'Макроэкономика'
UNION
SELECT 'Православная экономика'
UNION
SELECT 'Античная философия'
UNION
SELECT 'Прогрессивная философия'
UNION
SELECT 'Примитивная математика'
UNION
SELECT 'Высшая математика';

INSERT INTO d_students (full_name)
VALUES
-- Для курса 1
('Студент 1 курса 1'),
('Студент 2 курса 1'),
('Студент 3 курса 1'),
-- Для курса 2
('Студент 1 курса 2'),
('Студент 2 курса 2'),
('Студент 3 курса 2'),
-- Для курса 3
('Студент 1 курса 3'),
('Студент 2 курса 3'),
('Студент 3 курса 3'),
-- Для курса 4
('Студент 1 курса 4'),
('Студент 2 курса 4'),
('Студент 3 курса 4'),
-- Для курса 5
('Студент 1 курса 5'),
('Студент 2 курса 5'),
('Студент 3 курса 5'),
-- Для курса 6
('Студент 1 курса 6'),
('Студент 2 курса 6'),
('Студент 3 курса 6'),
-- Для курса 7
('Студент 1 курса 7'),
('Студент 2 курса 7'),
('Студент 3 курса 7'),
-- Для курса 8
('Студент 1 курса 8'),
('Студент 2 курса 8'),
('Студент 3 курса 8');


-- Таблицы фактов
CREATE TABLE f_university_departments
(
    uni_id  INT REFERENCES d_universities (id),
    dept_id INT REFERENCES d_departments (id),
    PRIMARY KEY (uni_id, dept_id)
);


CREATE TABLE f_department_courses
(
    dept_id   INT REFERENCES d_departments (id),
    course_id INT REFERENCES d_courses (id),
    PRIMARY KEY (dept_id, course_id)
);

CREATE TABLE f_course_students
(
    course_id   INT REFERENCES d_courses (id),
    students_id INT REFERENCES d_students (id),
    PRIMARY KEY (course_id, students_id)
);

-- Заполняем таблицы фактов
INSERT INTO f_university_departments(uni_id, dept_id)
SELECT 1, 1
UNION
SELECT 1, 2
UNION
SELECT 1, 3
UNION
SELECT 1, 4
UNION
SELECT 2, 1
UNION
SELECT 2, 2
UNION
SELECT 2, 3
UNION
SELECT 2, 4
UNION
SELECT 3, 1
UNION
SELECT 3, 2
UNION
SELECT 3, 3
UNION
SELECT 3, 4;

INSERT INTO f_department_courses(dept_id, course_id)
SELECT 1, 6
UNION
SELECT 1, 8
UNION
SELECT 2, 2
UNION
SELECT 2, 7
UNION
SELECT 3, 2
UNION
SELECT 3, 4
UNION
SELECT 4, 3
UNION
SELECT 4, 5;

INSERT INTO f_course_students (course_id, students_id)
SELECT
    CAST(SUBSTRING(full_name FROM 'курса (\d+)') AS INT) AS course_num,
    id AS students_id
FROM d_students
WHERE full_name LIKE 'Студент % курса %';



SELECT d_students.id AS student_id, d_students.full_name AS student_name, d_courses.name AS course_name
FROM d_students
         JOIN f_course_students ON f_course_students.students_id = d_students.id
         JOIN d_courses ON d_courses.id = f_course_students.course_id;

SELECT d_students.id AS student_id, d_students.full_name AS student_name, d_courses.name AS course_name
FROM d_students
         JOIN f_course_students ON d_students.id = f_course_students.students_id
         JOIN d_courses ON f_course_students.course_id = d_courses.id;

SELECT d_students.id AS student_id
from d_students
join f_course_students on d_students.id = f_course_students.students_id;

SELECT d_students.full_name AS student_name, d_universities.name AS uni_name
FROM d_students
         JOIN f_course_students ON d_students.id = f_course_students.students_id
         JOIN d_courses ON f_course_students.course_id = d_courses.id
         JOIN f_department_courses ON f_department_courses.course_id = d_courses.id
         JOIN d_departments ON f_department_courses.course_id = d_departments.id
         JOIN f_university_departments ON d_departments.id = f_university_departments.dept_id
         JOIN d_universities ON f_university_departments.dept_id = d_universities.id;


