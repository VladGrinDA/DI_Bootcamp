-- Active: 1723968844525@@127.0.0.1@5432@public@public
--  Exercise 1 : Items and customers

CREATE DATABASE public;

CREATE TABLE items();

CREATE TABLE customers();

-- Creating items table and adding items to it
ALTER TABLE items
ADD COLUMN items_id SERIAL PRIMARY KEY,
ADD COLUMN item_name VARCHAR(255) NOT NULL,
ADD COLUMN price NUMERIC NOT NULL;

INSERT INTO items (item_name, price)
VALUES ('Small Desk', 100),
    ('Large desk', 300),
    ('Fan', 80);

select * from items;

-- Creating customers table and adding customers to it
ALTER TABLE customers
ADD COLUMN customer_id SERIAL PRIMARY KEY,
ADD COLUMN first_name VARCHAR(255) NOT NULL,
ADD COLUMN last_name VARCHAR(255) NOT NULL;

INSERT INTO customers (first_name, last_name)
VALUES ('Greg', 'Jones'),
    ('Sandra', 'Jones'),
    ('Scott', 'Scott'),
    ('Trevor', 'Green'),
    ('Melanie', 'Johnson');


-- Use SQL to fetch the following data from the database:

-- All the items.
select * from items;

-- All the items with a price above 80 (80 not included).
select *
from items
where price > 80;

-- All the items with a price below 300. (300 included)
select *
from items
where price <= 300;

-- All customers whose last name is ‘Smith’ (What will be your outcome?).
select *
from customers
where last_name = 'Smith';

-- All customers whose last name is ‘Jones’.
select *
from customers
where last_name = 'Jones';

-- All customers whose firstname is not ‘Scott’.
select *
from customers
where first_name != 'Scott';

