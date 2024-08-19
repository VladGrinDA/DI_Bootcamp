-- Active: 1723968844525@@127.0.0.1@5432@hollywood@public
CREATE TABLE actors(
 actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES ('Matt','Damon','08/10/1970', 5),
    ('George','Clooney','06/05/1961', 2),
    ('Angelina','Jolie','04/05/1975', 1),
    ('Will','Smith','25/04/1968', 3),
    ('Tom','Cruise','03/07/1962', 4)
;

select *
from actors;


select *
from actors
limit 4;

select *
from actors
order by last_name desc
limit 4;

select *
from actors
where last_name like '%e%';

select *
from actors
where number_oscars >= 5;

UPDATE actors 
SET age='1970-01-01' 
WHERE first_name='Matt' AND last_name='Damon'
RETURNING 
    actor_id,
    first_name, 
    last_name,
    age;


select * from actors;


update actors
set first_name = 'Maty'
where first_name = 'Matt';

update actors
set number_oscars = 4
where last_name = 'Clooney';

alter TABLE actors rename COLUMN age to birthdate;

DELETE FROM actors WHERE actor_id=4
RETURNING actor_id, first_name, last_name, number_oscars;
