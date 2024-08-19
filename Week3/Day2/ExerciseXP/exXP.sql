
-- 🌟 Exercise 1 : Items and customers
-- Instructions
-- We will work on the public database that we created yesterday.

-- Use SQL to get the following from the database:

-- All items, ordered by price (lowest to highest).
select * from items
order by price;


-- Items with a price above 80 (80 included), ordered by price (highest to lowest) 
select * from items
where price >= 80
ORDER BY price DESC

-- The first 3 customers in alphabetical order of the first name (A-Z) – exclude the primary key column from the results.
select first_name, last_name from customers
ORDER BY first_name

-- All last names (no other columns!), in reverse alphabetical order (Z-A)
select last_name from customers
ORDER BY first_name DESC


-- 🌟 Exercise 2 : dvdrental database
-- We will use the newly installed dvdrental database.

-- In the dvdrental database write a query to select all the columns from the “customer” table.
select * from customer;

-- Write a query to display the names (first_name, last_name) using an alias named “full_name”.
select (first_name, last_name) as full_name from customer;

-- Lets get all the dates that accounts were created. Write a query to select all the create_date from the “customer” table (there should be no duplicates).
select DISTINCT create_date from customer;

-- Write a query to get all the customer details from the customer table, it should be displayed in descending order by their first name.
select * from customer
order by first_name desc; 

-- Write a query to get the film ID, title, description, year of release and rental rate in ascending order according to their rental rate.
select film_id, title, description, release_year, rental_rate
from film
ORDER BY rental_rate;

-- Write a query to get the address, and the phone number of all customers living in the Texas district, these details can be found in the “address” table.
select "address", phone
from "address"
where district = 'Texas'

-- Write a query to retrieve all movie details where the movie id is either 15 or 150.
select * from film
where film_id in (15 ,150)

-- Write a query which should check if your favorite movie exists in the database. Have your query get the film ID, title, description, length and the rental rate, these details can be found in the “film” table.
select film_id, title, "description", "length", rental_rate
from film 
-- where title = 'Shrek' -- No Shrek movie :(
where title = 'Shrek License' -- Hope that Shrek License is also a great one 

-- No luck finding your movie? Maybe you made a mistake spelling the name. Write a query to get the film ID, title, description, length and the rental rate of all the movies starting with the two first letters of your favorite movie.
select * from film
where title ilike 'sh%'

-- Write a query which will find the 10 cheapest movies.
select * from film
order by rental_rate + replacement_cost -- I think it makes sense to consider both fields
limit 20;

-- Not satisfied with the results. Write a query which will find the next 10 cheapest movies.
-- Bonus: Try to not use LIMIT.
select * from film
order by rental_rate + replacement_cost
offset 10
fetch next 10 rows only; -- I found it by googling. As i understood it is a SQL standard analog of the LIMIT clause

-- Write a query which will join the data in the customer table and the payment table. You want to get the first 
-- name and last name from the curstomer table, as well as the amount and the date of every payment made by a customer, ordered by their id (from 1 to…).
select first_name, last_name, amount, payment_date
from customer
join payment using(customer_id)
order by payment_id;

-- You need to check your inventory. Write a query to get all the movies which are not in inventory.
select * from film
where film_id not in (select film_id from inventory);

-- Write a query to find which city is in which country.
select city, country
from city
join country using(country_id)

-- Bonus You want to be able to see how your sellers have been doing? Write a query to get the customer’s id, names (first and last), the amount and the date of payment ordered by the id of the staff member who sold them the dvd.
select first_name, last_name, amount, payment_date
from payment
join customer using(customer_id)
order by staff_id