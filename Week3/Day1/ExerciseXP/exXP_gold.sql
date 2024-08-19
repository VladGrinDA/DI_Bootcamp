-- Active: 1723968844525@@127.0.0.1@5432@bootcamp@public
-- For the following questions, you have to fetch the first_names, last_names and birth_dates of the students.

-- Fetch the first four students. You have to order the four students alphabetically by last_name.
-- Fetch the details of the youngest student.
-- Fetch three students skipping the first two students.

select * from students;

select first_name, last_name, birth_date
from students
ORDER BY last_name ASC
limit 4;

select first_name, last_name, birth_date
from students
ORDER BY birth_date ASC
limit 1;

select first_name, last_name, birth_date
from students
ORDER BY birth_date ASC
LIMIT 3 OFFSET 2;
