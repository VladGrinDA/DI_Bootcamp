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

