-- Active: 1723968844525@@127.0.0.1@5432@public@public
-- Part I
-- Create 2 tables : Customer and Customer profile. They have a One to One relationship.
-- A customer can have only one profile, and a profile belongs to only one customer
-- The Customer table should have the columns : id, first_name, last_name NOT NULL
create table customer (
    customer_id serial PRIMARY KEY
    , first_name VARCHAR(255) NOT NULL
    , last_name VARCHAR(255) NOT NULL
);

-- The Customer profile table should have the columns : id, isLoggedIn DEFAULT false (a Boolean),
--  customer_id (a reference to the Customer table)
create table customer_profile (
    customer_profile_id SERIAL PRIMARY KEY
    , "isLoggedIn" BOOLEAN DEFAULT false
    , customer_id INTEGER UNIQUE REFERENCES customer (customer_id) 
    -- unique constraint for the one to one relationship
);

INSERT INTO customer (first_name, last_name)
VALUES ('John', 'Doe'),
    ('Jerome', 'Lalu'),
    ('Lea', 'Rive');

select * from customer;

-- Insert those customer profiles, use subqueries
-- truncate table customer_profile;
insert into customer_profile ("isLoggedIn", customer_id) 
VALUES
-- John is loggedIn
    (DEFAULT, (select customer_id from customer where first_name = 'John'))
-- Jerome is not loggedIn
    , (true, (select customer_id from customer where first_name = 'Jerome'))
;
select * from customer_profile;

-- Use the relevant types of Joins to display:

-- The first_name of the LoggedIn customers
select first_name
from customer
join customer_profile USING (customer_id)
where "isLoggedIn";

-- All the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.
select first_name, "isLoggedIn"
from customer
left join customer_profile USING (customer_id);

-- The number of customers that are not LoggedIn
select count(*)
from customer
left join customer_profile USING (customer_id)
where not "isLoggedIn"
or "isLoggedIn" is NULL -- use to include customers without profile
;


-- Part II:

-- Create a table named Book, with the columns : book_id SERIAL PRIMARY KEY, title NOT NULL, author NOT NULL
create table book (
    book_id serial PRIMARY KEY
    , title VARCHAR(550) NOT NULL
    , author VARCHAR(255) NOT NULL
);

insert into book (title, author)
VALUES
    ('Alice In Wonderland', 'Lewis Carroll'),
    ('Harry Potter', 'J.K Rowling'),
    ('To kill a mockingbird', 'Harper Lee');

-- Create a table named Student, with the columns : student_id SERIAL PRIMARY KEY, name NOT NULL UNIQUE, age.
--  Make sure that the age is never bigger than 15 (Find an SQL method);
create table student (
    student_id SERIAL PRIMARY KEY
    , "name" VARCHAR(255) NOT NULL
    , "age" INTEGER CHECK ("age" <= 15)
)

INSERT INTO student ("name", "age") VALUES
    ('John', 12),
    ('Lera', 11),
    ('Patrick', 10),
    ('Bob', 14)
;

select * from student

-- Create a table named Library, with the columns :
-- book_fk_id ON DELETE CASCADE ON UPDATE CASCADE
-- student_id ON DELETE CASCADE ON UPDATE CASCADE
-- borrowed_date
-- This table, is a junction table for a Many to Many relationship with the Book and Student tables
create table library (
    book_id INTEGER REFERENCES book (book_id) ON DELETE CASCADE ON UPDATE CASCADE
    , student_id INTEGER REFERENCES student (student_id) ON DELETE CASCADE ON UPDATE CASCADE
    , borrowed_date DATE DEFAULT CURRENT_DATE
    , PRIMARY KEY (book_id, student_id)
)


-- Add 4 records in the junction table, use subqueries.
insert into library (student_id, book_id, borrowed_date)
values 
-- the student named John, borrowed the book Alice In Wonderland on the 15/02/2022
    ((select student_id from student where name = 'John')
    , (select book_id from book where title = 'Alice In Wonderland')
    , '15/02/2022'),
-- the student named Bob, borrowed the book To kill a mockingbird on the 03/03/2021
    ((select student_id from student where name = 'Bob')
    , (select book_id from book where title = 'To kill a mockingbird')
    , '03/03/2021'),
-- the student named Lera, borrowed the book Alice In Wonderland on the 23/05/2021
    ((select student_id from student where name = 'Lera')
    , (select book_id from book where title = 'Alice In Wonderland')
    , '23/05/2021'),
-- the student named Bob, borrowed the book Harry Potter the on 12/08/2021
    ((select student_id from student where name = 'Bob')
    , (select book_id from book where title = 'Harry Potter')
    , '12/08/2021')

-- Display the data
-- Select all the columns from the junction table
select * from library;

-- Select the name of the student and the title of the borrowed books
select name
    , title
from library
join book using (book_id)
join student using (student_id)
;

-- Select the average age of the children, that borrowed the book Alice in Wonderland
select avg("age") as avg_age
from library
join book using (book_id)
join student using (student_id)
where title = 'Alice In Wonderland'
;

-- Delete a student from the Student table, what happened in the junction table ?
-- Answer: It also deleted rows wiht that student from library table 
delete from student
where name = 'John';

select *
from library
join student USING (student_id)
where name = 'John' -- Empty