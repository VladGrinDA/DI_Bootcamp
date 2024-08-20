-- Active: 1723968844525@@127.0.0.1@5432@hollywood@public

drop table if exists colors;
drop table if exists cars;
drop table if exists cars_cascade;
drop table if exists cars_set_default;

CREATE TABLE colors(
color_id SERIAL PRIMARY KEY,
color_name VARCHAR (50) NOT NULL);

CREATE TABLE cars(
car_id SERIAL PRIMARY KEY,
-- car_color INTEGER REFERENCES colors (color_id) ON DELETE RESTRICT,
car_color INTEGER REFERENCES colors (color_id) ON DELETE CASCADE,
car_name TEXT);

INSERT INTO colors (color_name)
VALUES ('red'),
    ('green'),
    ('blue'),
    ('yellow'),
    ('orange'),
    ('purple'),
    ('pink'),
    ('black'),
    ('white');

INSERT INTO cars (car_color, car_name)
VALUES (1, 'BMW'),
    (2, 'Volvo'),
    (3, 'Ferrari'),
    (4, 'Mercedes'),
    (5, 'Ford'),
    (6, 'Toyota');

SELECT cars.car_id, cars.car_name, colors.color_name as color
FROM cars
INNER JOIN colors
ON cars.car_color = colors.color_id;

DELETE FROM colors where color_name = 'yellow';

- EXERCISE IN CLASS:

-- 1 - Create a table called cars_set_default. It will have three columns: car_id (the primary key), car_name and car_color (CAR COLOR WILL BE SET DEFAULT): car_color INTEGER DEFAULT 1 REFERENCES colors (color_id) ON DELETE SET DEFAULT ON UPDATE SET DEFAULT

-- 2 - create a delete statement to delete from the colors table one color id.

-- 3 - select * from cars_set_default and analyse. What happened?

-- 1 - Create a table called cars_set_default. It will have three columns: 
-- car_id (the primary key), car_name and car_color (CAR COLOR WILL BE SET DEFAULT): 
-- car_color INTEGER DEFAULT 1 REFERENCES colors (color_id) ON DELETE SET DEFAULT ON UPDATE SET DEFAULT
-- INSERT data to the cars_set_default table:

drop table if exists cars_set_default;
CREATE TABLE cars_set_default(
    car_id SERIAL PRIMARY KEY,
    car_color_id INTEGER DEFAULT 1,
    car_name TEXT,
    FOREIGN KEY (car_color_id) REFERENCES colors (color_id) ON DELETE SET DEFAULT ON UPDATE SET DEFAULT
);

INSERT INTO cars_set_default (car_name, car_color_id) VALUES
('Toyota',1),
('Ford', 2),
('Honda', 3),
('Mazda', 2);

drop table if exists cars_cascade;
CREATE TABLE cars_cascade (
    car_id SERIAL PRIMARY KEY,
    car_name VARCHAR(50),
    car_color_id INTEGER REFERENCES colors (color_id) ON DELETE CASCADE ON UPDATE CASCADE
)

INSERT INTO cars_cascade (car_name, car_color_id) VALUES
('Toyota',1),
('Ford', 2),
('Honda', 3),
('Mazda', 2);

DELETE FROM colors WHERE color_id = 2; -- Allows to delete and deletes the whole row from the child

select * from cars_cascade;

select * from cars_set_default;



select * from movies;

-- alter table movies add COLUMN released_date date default '01/01/2000' not null;

CREATE TABLE movies (
  movie_id SERIAL,
  movie_title VARCHAR(45) NOT NULL,
  released_date date NOT NULL,
  PRIMARY KEY (movie_id)
);


/*
 one to one: a movie has one scenario
*/

CREATE TABLE scenarios (
  pk_movie_id INTEGER NOT NULL,
  scenario_story TEXT NOT NULL,
  PRIMARY KEY (pk_movie_id),
  CONSTRAINT fk_movie_id FOREIGN KEY (pk_movie_id) REFERENCES movies (movie_id)
);


