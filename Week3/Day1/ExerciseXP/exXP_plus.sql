-- Active: 1723968844525@@127.0.0.1@5432@bootcamp@public
-- 🌟 Exercise 1 : Bootcamp
-- Instructions
-- For this exercise, you will have to find some requests on your own!

-- Create
-- Create a database called bootcamp.
-- Create a table called students.

CREATE DATABASE bootcamp;

CREATE TABLE students ();

-- Add the following columns:
-- id
-- last_name
-- first_name
-- birth_date
-- The id must be auto_incremented.
-- Make sure to choose the correct data type for each column.

ALTER TABLE students
ADD COLUMN id SERIAL PRIMARY KEY,
ADD COLUMN last_name VARCHAR(255) NOT NULL,
ADD COLUMN first_name VARCHAR(255) NOT NULL,
ADD COLUMN birth_date DATE;

TRUNCATE students RESTART IDENTITY;

INSERT INTO students (last_name, first_name, birth_date)
VALUES ('Benichou', 'Marc', '02/11/1998'),
    ('Cohen', 'Yoan', '03/12/2010'),
    ('Benichou', 'Lea', '27/07/1987'),
    ('Dux', 'Amelia', '07/04/1996'),
    ('Grez', 'David', '14/06/2003'),
    ('Simpson', 'Omer', '03/10/1980');


-- Fetch all of the data from the table.
select * from students;

-- Fetch all of the students first_names and last_names.
select first_name, last_name from students;

-- For the following questions, only fetch the first_names and last_names of the students.
-- Fetch the student which id is equal to 2.
select first_name, last_name from students where id = 2;

-- Fetch the student whose last_name is Benichou AND first_name is Marc.
select first_name, last_name 
from students 
where last_name = 'Benichou' and first_name = 'Marc';

-- Fetch the students whose last_names are Benichou OR first_names are Marc.
select first_name, last_name 
from students 
where last_name = 'Benichou' or first_name = 'Marc';

-- Fetch the students whose first_names contain the letter a.
select first_name, last_name 
from students 
where first_name ilike '%a%';

-- Fetch the students whose first_names start with the letter a.
select first_name, last_name 
from students 
where first_name ilike 'a%';

-- Fetch the students whose first_names end with the letter a.
select first_name, last_name 
from students 
where first_name ilike '%a';

-- Fetch the students whose second to last letter of their first_names are a (Example: Leah).
select first_name, last_name 
from students 
where first_name like '%a%';

-- Fetch the students whose id’s are equal to 1 AND 3 .
select first_name, last_name 
from students 
where id = 1 or id = 3;

-- Fetch the students whose birth_dates are equal to or come after 1/01/2000. (show all their info).
select *
from students 
where birth_date >= '01/01/2000';

