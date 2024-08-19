-- Active: 1723968844525@@127.0.0.1@5432@public@public

-- Exercise 3 : Items and customers
-- Instructions
-- We will work on the public database that we created yesterday.

-- Part I

-- Create a table named purchases. It should have 3 columns :
-- id : the primary key of the table
-- customer_id : this column references the table customers
-- item_id : this column references the table items
-- quantity_purchased : this column is the quantity of items purchased by a certain customer

create table purchases (
    purchase_id SERIAL PRIMARY KEY
    , customer_id INTEGER NOT NULL
    , item_id INTEGER NOT NULL
    , quantity_purchased INTEGER NOT NULL
    , FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
    , FOREIGN KEY (item_id) REFERENCES items (item_id)
);

select * from items;
select * from customers;

-- Insert purchases for the customers, use subqueries:
-- Scott Scott bought one fan
-- Melanie Johnson bought ten large desks
-- Greg Jones bougth two small desks
INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES
    (
        (SELECT customer_id FROM customers WHERE first_name='Scott' AND last_name='Scott'),
        (SELECT item_id FROM items WHERE item_name='Fan'),
        1
    ),
    (
        (SELECT customer_id FROM customers WHERE first_name='Melanie' AND last_name='Johnson'),
        (SELECT item_id FROM items WHERE item_name='Large Desk'),
        10
    ),
    (
        (SELECT customer_id FROM customers WHERE first_name='Greg' AND last_name='Jones'),
        (SELECT item_id FROM items WHERE item_name='Small Desk'),
        2
    )
;

-- Part II

-- Use SQL to get the following from the database:
-- All purchases. Is this information useful to us?
-- Not in this form
select * from purchases;

-- All purchases, joining with the customers table.
select * from purchases join customers using (customer_id);

-- Purchases of the customer with the ID equal to 5.
select * from purchases where customer_id = 5;

-- Purchases for a large desk AND a small desk
select * from purchases 
where item_id in (select item_id from items where item_name in ('Large Desk', 'Small Desk'));

-- Use SQL to show all the customers who have made a purchase. Show the following fields/columns:
-- Customer first name
-- Customer last name
-- Item name
select first_name, last_name, item_name
from customers 
join purchases using (customer_id)
join items using (item_id);

-- Add a row which references a customer by ID, but does not reference an item by ID (leave it blank). Does this work? Why/why not?
-- I used NOT NULL constraint on items_id when creating the table. However, by default FOREIGN KEY could be a NULL 
INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES
    ((SELECT customer_id FROM customers WHERE first_name='Scott' AND last_name='Scott'),
    NULL,
    10);