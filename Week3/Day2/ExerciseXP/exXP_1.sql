-- Active: 1723968844525@@127.0.0.1@5432@public@public

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

