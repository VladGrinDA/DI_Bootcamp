-- Active: 1723968844525@@127.0.0.1@5432@bootcamp@public

-- Exercise 2: students table
-- Instructions
-- Continuation of the Day1 Exercise XPGold : students table

-- Update
-- ‘Lea Benichou’ and ‘Marc Benichou’ are twins, they should have the same birth_dates. Update both their birth_dates to 02/11/1998.
update students
set birth_date = '02/11/1998'
where concat(first_name, ' ', last_name) in ('Lea Benichou', 'Marc Benichou')
returning *;

-- Change the last_name of David from ‘Grez’ to ‘Guez’.
update students
set last_name = 'Guez'
where first_name = 'David' and last_name = 'Grez'
returning *;

select * from students;

-- Delete
-- Delete the student named ‘Lea Benichou’ from the table.
delete from students
where first_name = 'Lea' and last_name = 'Benichou'
returning *;

-- Count
-- Count how many students are in the table.
select count(*) from students;

-- Count how many students were born after 1/01/2000.
select count(*) from students where birth_date >= '01/01/2000'

-- Insert / Alter
-- Add a column to the student table called math_grade.
alter table students add column math_grade integer;

-- Add 80 to the student which id is 1.
update students
set math_grade = 80
where id = 1;

-- Add 90 to the students which have ids of 2 or 4.
update students
set math_grade = 90
where id in (2, 4);

-- Add 40 to the student which id is 6.
update students
set math_grade = 40
where id = 6;

-- Count how many students have a grade bigger than 83
select count(*)
from students
where math_grade > 83;

-- Add another student named ‘Omer Simpson’ with the same birth_date as the one already in the table. Give him a grade of 70.
insert into students (first_name, last_name, birth_date, math_grade)
values (
    'Omer'
    , 'Simpson'
    , (select birth_date from students order by random() limit 1)
    , 70
);

-- Now, in the table, ‘Omer Simpson’ should appear twice. It’s the same student, although he received 2 different grades because he retook the math exam.

-- Bonus: Count how many grades each student has.
select first_name, last_name, count(*) as total_grade
from students
GROUP BY first_name, last_name;

-- Find the sum of all the students grades.
select sum(math_grade) as total_grade_sum
from students;

