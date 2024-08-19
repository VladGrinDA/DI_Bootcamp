-- Active: 1723968844525@@127.0.0.1@5432@hollywood@public

-- Get the average number of oscars in the table
select avg(number_oscars) as avg_number_oscars from actors;

-- Get distinct actors depending on their number of oscars
select DISTINCT first_name, last_name, number_oscars from actors;

-- Get the actors born after 01/01/1970
select * from actors
where birthdate >= '01/01/1970';

-- Get the actors which names are 'David', 'Morgan' or 'Will'
select * from actors
where first_name in ('David', 'Morgan', 'Will');

select * from actors;

update actors set first_name = 'Matt' where last_name = 'Damon';

CREATE TABLE movies(
movie_id SERIAL,
movie_title VARCHAR (50) NOT NULL,
movie_story TEXT,
actor_playing_id INTEGER,
PRIMARY KEY (movie_id),
FOREIGN KEY (actor_playing_id) REFERENCES actors (actor_id)
);

INSERT INTO movies (movie_title, movie_story, actor_playing_id) VALUES
    ( 'Good Will Hunting', 
    'Written by Affleck and Damon, the film follows 20-year-old South Boston janitor Will Hunting',
    (SELECT actor_id from actors WHERE first_name='Matt' AND last_name='Damon')),
    ( 'Oceans Eleven', 
    'American heist film directed by Steven Soderbergh and written by Ted Griffin.', 
    (SELECT actor_id from actors WHERE first_name='Matt' AND last_name='Damon'));

SELECT actors.first_name, actors.last_name, movies.movie_title
FROM actors
INNER JOIN movies
ON actors.actor_id = movies.actor_playing_id;



-- Create another table producers, with a foreign key : the id of a movie. The producers table is linked to the movies table
create table producers (
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    movie_id INTEGER,
    PRIMARY KEY (first_name, last_name, movie_id),
    FOREIGN KEY (movie_id) REFERENCES movies (movie_id)
);

-- Insert some record
INSERT INTO producers (first_name, last_name, movie_id) VALUES
    ('Lawrence', 'Bender', 1),
    ('Bob', 'Weinstein', 1),
    ('Harvey', 'Weinstein', 1),
    ('Jerry', 'Weintraub', 2),
    ('Susan', 'Ekins', 2);

-- Display with INNER JOIN

select * from movies
join producers using(movie_id);


-- Create another table, called countries, with two fields : country_id and coutry_name. It has no foreign key. It's a table to test the PostgreSQL Joins.
create table cointries (
    country_id SERIAL PRIMARY KEY,
    country_name VARCHAR(64)
);

insert into cointries (country_name)
VALUES ('USA'),
    ('Israel'),
    ('Russia'),
    ('Spain'),
    ('France')
;

-- Use INNER JOIN, LEFT OUTER JOIN, RIGHT OUTER JOIN, and FULL OUTER JOIN to join the table countries 
-- with the table actors, depending on the comparaison of their primary key
select *
from actors
join cointries on actor_id = country_id;

select *
from actors
left join cointries on actor_id = country_id;

select *
from actors
right join cointries on actor_id = country_id;

select *
from actors
full outer join cointries on actor_id = country_id;
