-- Active: 1723968844525@@127.0.0.1@5432@hollywood@public

-- Instructions
-- In this exercise we will be using the actors table from todays lesson.
-- 1. Count how many actors are in the table.
select * from actors;

select count(*)
from actors;

-- 2. Try to add a new actor with some blank fields. What do you think the outcome will be ?
-- There are not null constraint on all columns so we will get an error
-- But we can use empty string for first_name and last_name without any problems

insert into actors (birthdate)
values ('2022-01-01');

insert into actors (first_name, last_name)
values ('John', 'Doe', NULL);

insert into actors (first_name, last_name, birthdate, number_oscars)
values ('', '', '2022-01-01', 0);

select * from actors;

