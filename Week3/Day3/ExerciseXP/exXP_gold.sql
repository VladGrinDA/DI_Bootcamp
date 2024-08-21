-- Active: 1723968844525@@127.0.0.1@5432@dvdrental@public
-- Exercise 1 : DVD Rentals
-- Instructions
-- Get a list of all rentals which are out (have not been returned). How do we identify these films in the database?
select film.*
from rental
join inventory using (inventory_id)
join film using (film_id)
where return_date is null;

-- Get a list of all customers who have not returned their rentals. Make sure to group your results.
select DISTINCT customer.*
from rental
join customer using (customer_id)
where return_date is null;

-- Get a list of all the Action films with Joe Swank.
-- Before you start, could there be a shortcut to getting this information? Maybe a view?
select string_agg(title, ', ')
from film
join film_actor USING (film_id)
join actor using (actor_id)
where first_name = 'Joe'
    and last_name = 'Swank'
GROUP BY actor_id;


select  film_info
from actor_info
where first_name = 'Joe'
    and last_name = 'Swank';


-- Exercise 2 – Happy Halloween
-- Instructions
-- There is a zombie plague approaching! The DVD rental company is offering to lend all 
-- of its DVDs to the local shelters, so that the citizens can watch the movies together in the
--  shelters until the zombies are destroyed by the armed forces. Prepare tables with the following data:

-- How many stores there are, and in which city and country they are located.
select ctr.country, c.city, count(*)
from store s
join address a on a.address_id = s.address_id
join city c on c.city_id = a.city_id
join country ctr on c.country_id = ctr.country_id
GROUP BY ctr.country, c.city;

-- How many hours of viewing time there are in total in each store – in other words, the sum of the length of every inventory item in each store.
select s.store_id, sum(f."length") as view_time_min
from store s
join customer using (store_id)
join rental using (customer_id)
join inventory using (inventory_id)
join film f using (film_id)
group by s.store_id

-- Make sure to exclude any inventory items which are not yet returned. (Yes, even in the time of zombies there are people who do not return their DVDs)
-- A list of all customers in the cities where the stores are located.
select distinct c.city, customer.*
from store s
join customer using (store_id)
join rental using (customer_id)
join inventory using (inventory_id)
join address a on a.address_id = s.address_id
join city c on c.city_id = a.city_id
where rental_date is not NULL

-- A list of all customers in the countries where the stores are located.
select distinct ctr.country, customer.*
from store s
join customer using (store_id)
join rental using (customer_id)
join inventory using (inventory_id)
join address a on a.address_id = s.address_id
join city c on c.city_id = a.city_id
join country ctr on c.country_id = ctr.country_id
where rental_date is not NULL;

-- Some people will be frightened by watching scary movies while zombies walk the streets. 
-- Create a '%safe list%' of all movies which do not include the '%Horror%' category, or contain
--  the words '%beast%', '%monster%', '%ghost%', '%dead%', '%zombie%', or '%undead%' in their titles or descriptions… 
-- Get the sum of their viewing time (length).
-- Hint : use the CHECK contraint
create temp table tt_safe_list as
select f.*, cat."name" as category_name
from film as f
join film_category using (film_id)
join category as cat using (category_id)
where not (title ilike any(array['%beast%', '%monster%', '%ghost%', '%dead%', '%zombie%', '%undead%'])
    or description ilike any(array['%beast%', '%monster%', '%ghost%', '%dead%', '%zombie%', '%undead%'])
    or cat."name" = 'Horror')
;

select * from category;

-- Check if film to category is a one to one relationship
select film_id, count(*)
from film
join film_category using (film_id)
join category using (category_id)
group by film_id
having count(*) > 1

select sum("length") from tt_safe_list;

-- For both the '%general%' and the '%safe%' lists above, also calculate the time in hours and days (not just minutes).
