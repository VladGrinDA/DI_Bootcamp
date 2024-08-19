-- Active: 1723968844525@@127.0.0.1@5432@public@public

drop table if exists firsttab;

CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
);

INSERT INTO FirstTab 
VALUES (5,'Pawan'),
    (6,'Sharlee'),
    (7,'Krish'),
    (NULL,'Avtaar');

SELECT * FROM FirstTab;

CREATE TABLE SecondTab (
    id integer 
);

INSERT INTO SecondTab
 VALUES (5),
    (NULL);


SELECT * FROM SecondTab;

-- Prediction: Count rows from FirstTab where id is not NULL. So it shoud return 3
SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN (SELECT id FROM SecondTab WHERE id IS NULL) -- 0

-- Prediction: Last one was a suprise. If condition including null returns null then the output shold be 2
SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 ) -- 2

-- Prediction: i hope it's 4
SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab ) -- 0

-- OKAY. NOW I SEE
select 6 in (NULL); -- NULL;
select 6 in (5, NULL); -- NULL
select 5 in (5, NULL); -- true
select 5 not in (5, NULL); -- false

select 5 + NULL; -- NULL

-- Prediction: At that point I feel like you must have abilities to see the future. I've acquired some so the answer is 2
SELECT COUNT(*) 
FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL ) -- 2