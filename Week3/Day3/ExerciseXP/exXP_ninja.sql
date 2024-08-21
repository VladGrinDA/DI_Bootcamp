-- Exercise 1 : DVD Rentals
-- Instructions
-- We want to encourage families and kids to enjoy our movies.

-- Retrieve all films with a rating of G or PG, which are are not currently rented 
-- (they have been returned/have never been borrowed).
select DISTINCT rating
from film

select film.*
from film
left join inventory using (film_id)
left join rental USING (inventory_id)
where rating in ('G', 'PG', 'PG-13')
    and (return_date is not null or rental_id is null)


-- create index if not exists on children_film (film_id) 


-- Create a new table which will represent a waiting list for children’s movies. 
-- This will allow a child to add their name to the list until the DVD is available (has been returned). 
-- Once the child takes the DVD, their name should be removed from the waiting list (ideally using triggers, 
-- but we have not learned about them yet. Let’s assume that our Python program will manage this). 
-- Which table references should be included?

create table waiting_list (
    film_id INTEGER
    , first_name VARCHAR(255) not NULL
    , last_name VARCHAR(255) not NULL
    , added_dt timestamp default now()
    , PRIMARY KEY (film_id, first_name, last_name)
    , Foreign Key (film_id) REFERENCES film (film_id)
);

-- Trigger to check if a film is appropriate for children
create or replace function trgf_is_children_film()
returns trigger as $$
BEGIN
    if not exists (select 1 from film f where f.rating in ('G', 'PG', 'PG-13') and f.film_id = new.film_id) then
        raise EXCEPTION 'film with film_id % is not allowed for children to see', new.film_id;
    end if;
    return new;
end;
$$ language plpgsql;

create TRIGGER is_childer_film_trigger
before insert or UPDATE on waiting_list
for EACH row EXECUTE FUNCTION trgf_is_children_film();

insert into waiting_list (film_id, first_name, last_name)
values
    ((select film_id from film where rating in ('G', 'PG', 'PG-13') limit 1)
    , 'Vlad'
    , 'A child');

insert into waiting_list (film_id, first_name, last_name)
values
    ((select film_id from film where rating not in ('G', 'PG', 'PG-13') limit 1)
    , 'Vladimir'
    , 'A bad boy');

-- Trigger to check if film is available to rent
CREATE OR REPLACE FUNCTION trgf_delete_from_waiting_list()
RETURNS TRIGGER AS $$
DECLARE
    customer_rec RECORD;
    film_rec RECORD;
BEGIN
    -- Fetch the customer details
    SELECT c.customer_id, c.first_name, c.last_name 
    INTO customer_rec
    FROM customer c
    WHERE c.customer_id = NEW.customer_id;
    -- Fetch the film details
    SELECT f.film_id, i.inventory_id
    INTO film_rec
    FROM film f
    JOIN inventory i ON i.film_id = f.film_id
    WHERE i.inventory_id = NEW.inventory_id;
    -- Delete from the waiting list based on the film and customer information
    DELETE FROM waiting_list wl
    WHERE wl.film_id = film_rec.film_id
      AND wl.first_name = customer_rec.first_name
      AND wl.last_name = customer_rec.last_name;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

create trigger delete_from_waiting_list_trigger
after insert or update on rental
for each row execute function trgf_delete_from_waiting_list();


select * from waiting_list;

insert into customer (store_id, first_name, last_name, address_id)
values (1, 'Vlad', 'A child', (select address_id from address limit 1));


insert into rental (rental_date, inventory_id, customer_id, staff_id)
values 
    (now()::date
    , (select inventory_id from inventory join film using (film_id) where film_id = 98 limit 1)
    , (select customer_id from customer where (first_name, last_name) = ('Vlad', 'A child'))
    , (select staff_id from staff limit 1));

select * from waiting_list; -- row was deleted!

-- Retrieve the number of people waiting for each children’s DVD. Test this by adding rows to the table that you created in question 2 above.

insert into waiting_list (film_id, first_name, last_name)
values
    ((select film_id from film where rating in ('G', 'PG', 'PG-13') limit 1)
    , 'Vlad'
    , 'A manchild'),
    ((select film_id from film where rating in ('G', 'PG', 'PG-13') offset 1 limit 1)
    , 'Joe'
    , 'Salad'),
    ((select film_id from film where rating in ('G', 'PG', 'PG-13') offset 2 limit 1)
    , 'Harry'
    , 'Armpit'),
    ((select film_id from film where rating in ('G', 'PG', 'PG-13') offset 1 limit 1)
    , 'Harry'
    , 'Armpit');

select title, count(*)
from film
join waiting_list using (film_id)
GROUP BY film_id, title