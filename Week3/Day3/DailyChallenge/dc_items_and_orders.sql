-- Active: 1723968844525@@127.0.0.1@5432@public@public

drop TABLE if EXISTS product_orders;
drop TABLE if EXISTS products;

-- Create a table called product_orders and a table called items. You decide which fields should
--  be in each table, although make sure the items table has a column called price.
create table product_orders (
    order_id SERIAL PRIMARY KEY
    , ordered_at TIMESTAMP DEFAULT now() NOT NULL
);

create table products (
    product_id serial PRIMARY KEY
    , product_name VARCHAR(255) NOT NULL
    , price NUMERIC NOT NULL CHECK(price >= 0)
    , quantity INTEGER NOT NULL
    , order_id INTEGER REFERENCES product_orders (order_id) on update CASCADE on delete CASCADE
);


insert into product_orders (ordered_at)
values (default);

-- There should be a one to many relationship between the product_orders table and the items table. An order can have many items, but an item can belong to only one order.
insert into products (product_name, price, quantity, order_id)
values
    ('iPhone', 999.99, 1, 1),
    ('Samsung TV', 1999.99, 2, 1),
    ('MacBook', 1299.99, 1, 2),
    ('Nike Shoes', 79.99, 3, 2),
    ('PlayStation5', 499.99, 1, 3),
    ('Xbox Series X', 499.99, 2, 4),
    ('Apple Watch', 249.99, 5, 5);

-- Create a function that returns the total price for a given order.
create or REPLACE function order_total_price (tgt_order_id int)
RETURNS numeric AS $$
BEGIN
    return (select sum(quantity * price) from products where order_id = tgt_order_id);
END;
$$ LANGUAGE PLPGSQL;

select order_id
    , ordered_at
    , order_total_price(order_id) as total_price
from product_orders

-- Bonus :
-- Create a table called users.
-- There should be a one to many relationship between the users table and the product_orders table.
alter table product_orders add column customer_id integer;
alter table product_orders add FOREIGN key (customer_id) REFERENCES customers (customer_id) on update CASCADE on delete CASCADE;

-- Create a function that returns the total price for a given order of a given user.
-- We can use previous function order_total_price because given order could be connected only with one user.
