-- Active: 1723968844525@@127.0.0.1@5432@dvdrental@public

-- 🌟 Exercise 1: DVD Rental
-- Instructions
-- Get a list of all the languages, from the language table.
select * from "language";

-- Get a list of all films joined with their languages – select the following details : film title, description, and language name.
select f.title, f."description", l."name"
from film f
left join "language" l using(language_id)

-- Get all languages, even if there are no films in those languages – select the following details : film title, description, and language name.
select f.title, f."description", l."name"
from film f
right join "language" l using(language_id)

-- Create a new table called new_film with the following columns : id, name. Add some new films to the table.
create table new_film (
    film_id serial primary key
    , title VARCHAR(255) not null
);

insert into new_film (title)
values
    ('Shrek')
    , ('Shrek 2')
    , ('Shrek the Third')
    , ('Shrek Forever After')
;

-- Create a new table called customer_review, which will contain film reviews that customers will make.
-- Think about the DELETE constraint: if a film is deleted, its review should be automatically deleted.
-- It should have the following columns:
-- review_id – a primary key, non null, auto-increment.
-- film_id – references the new_film table. The film that is being reviewed.
-- language_id – references the language table. What language the review is in.
-- title – the title of the review.
-- score – the rating of the review (1-10).
-- review_text – the text of the review. No limit on the length.
-- last_update – when the review was last updated.
create table customer_review (
    review_id serial primary key
    , film_id integer references new_film (film_id) on delete cascade on update cascade
    , language_id integer references "language" (language_id) on delete set null
    , title varchar(255) -- should be long enough
    , score INTEGER
    , review_text text
    , last_update timestamp default now()
    , check (score between 1 and 10)
);

-- Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
insert into customer_review (film_id, language_id, title, score, review_text)
values
    ((select film_id from new_film where title = 'Shrek')
    , (select language_id from "language" where "name" = 'English')
    , 'Best movie ever', 10, 'I love this movie'),
    ((select film_id from new_film where title = 'Shrek Forever After')
    , (select language_id from "language" where "name" = 'English')
    , 'Worst movie ever', 1, 'I hate this movie')
;

-- Test the check constraint
insert into customer_review (film_id, language_id, title, score, review_text)
values
    ((select film_id from new_film where title = 'Shrek 2')
    , (select language_id from "language" where "name" = 'English')
    , 'Second best movie ever', null, 'I love this movie')
; -- OK

insert into customer_review (film_id, language_id, title, score, review_text)
values
    ((select film_id from new_film where title = 'Shrek the Third')
    , (select language_id from "language" where "name" = 'English')
    , 'Pivotal moment', 0, 'Why?')
; -- Error


-- Delete a film that has a review from the new_film table, what happens to the customer_review table?
delete from new_film
where title = 'Shrek Forever After';

select * from customer_review
where film_id in (select film_id from new_film where title = 'Shrek Forever After');


-- Exercise 2 : DVD Rental
-- Instructions
-- Use UPDATE to change the language of some films. Make sure that you use valid languages.

-- Check query for getting list of random films
select * from film as f 
where f.film_id in (select film_id from film order by random() limit 5);

-- Ensure that expression will give a uniform distribution of numbers between 1 and 10
with sq as(
    select least(floor(random() * 10 + 1), 10) as rand_int
    from generate_series(1, 1e6)
) -- subquery for generating random numbers from 1 to 10
select rand_int, count(*), round(COUNT(*) / 1e6, 3) as proportion
from sq
GROUP BY rand_int;

-- Update 50 random films with random language value
update film 
set language_id = least(floor(random() * 6 + 1), 6)
where film_id in (select film_id from film order by random() limit 50)
returning *
;

-- Which foreign keys (references) are defined for the customer table? How does this affect the 
-- way in which we INSERT into the customer table?
-- Answer: In customers table properties it states that there is one
-- FK customer_address_id_fkey with CASCADE on update and RESTRICT on delete rules.
-- So when inserting we must ensure that address_id in present in the address table.

-- We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?
-- It has FK for the new_film table so it is a child table and there shouldn't be any problems droping it.
drop table customer_review;

-- Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
select count(*) from rental
where return_date is null;

-- Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
select DISTINCT film_id
    , title
    , rental_rate
from rental
    join inventory using (inventory_id)
    join film as f using (film_id)
where return_date is null
ORDER BY rental_rate desc
limit 30;

-- Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, 
-- but he can’t remember their names. Can you help him find which movies he wants to rent?
-- The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
select *
from film
join film_actor USING (film_id)
join actor using (actor_id)
where first_name = 'Penelope' 
    and last_name = 'Monroe'
    and "description" ilike '%sumo%'
    and "description" ilike '%wrestler%'
;

-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.
select *
from film
where rating = 'R'
    and "length" < 60
;

-- The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental,
--  and he returned it between the 28th of July and the 1st of August, 2005.
select f.*
from rental
join inventory using (inventory_id)
join film f using (film_id)
join customer as c using (customer_id)
where c.first_name = 'Matthew'
    and c.last_name = 'Mahan'
    and rental_rate > 4
    and return_date BETWEEN '2005-07-28' and '2005-08-01'

-- The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.
select f.*
from film f
join inventory using (film_id)
join rental using (inventory_id)
join customer as c using (customer_id)
where true 
    and c.first_name = 'Matthew'
    and c.last_name = 'Mahan'
    and ("description" ilike '%boat%'
        or title ilike '%boat%')
order by replacement_cost desc
;