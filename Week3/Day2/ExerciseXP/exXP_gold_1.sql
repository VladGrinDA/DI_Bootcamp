-- Active: 1723968844525@@127.0.0.1@5432@dvdrental@public

# Exercise 1: DVD Rental
# Instructions
# You were hired to babysit your cousin and you want to find a few movies that he can watch with you.
#   Find out how many films there are for each rating.
select * from film;

select rating, count(*)
from film
group by rating;

#   Get a list of all the movies that have a rating of G or PG-13.
#       Filter this list further: look for only movies that are under 2 hours long, and whose rental price (rental_rate) is under 3.00. Sort the list alphabetically.
select *
from film
where rating in ('G', 'PG-13')
and "length" / 60 < 2
and rental_rate < 3
order by title;

#   Find a customer in the customer table, and change his/her details to your details, using SQL UPDATE.
select * from customer;
select * from customer where first_name ilike 'v%' and last_name ilike 'g%'

update customer 
set first_name = 'Vlad'
    , last_name = 'Grinberg'
    , email = 'vladgrin@mail.com'
where first_name = 'Virginia'
    and last_name = 'Green'
returning customer_id
;

#   Now find the customer’s address, and use UPDATE to change the address to your address (or make one up).
select * from customer 
where first_name = 'Vlad' 
and last_name = 'Grinberg'; -- 35

select * from city
join country using(country_id)
where country = 'Israel';

select * from "address" where address_id = 39;

update "address"
set "address" = 'Bezalel St 8'
    , district = 'Ramat Gan'
    , city_id = 533
    , last_update = now()
where address_id = (select address_id from customer where customer_id = 35);

