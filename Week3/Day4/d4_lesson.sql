-- Active: 1723968844525@@127.0.0.1@5432@hollywood@public


-- COPY [Table Name](Optional Columns)
-- FROM '[Absolute Path to File]'
-- DELIMITER '[Delimiter Character]' CSV [HEADER];

-- \copy actors (first_name, last_name, birthdate, number_oscars) from 'C:\Users\Vlad\developers_institute\practice\Week3\Day4\csv_example.csv' DELIMITER ',' csv header;

-- \copy actors(actor_id, first_name, last_name, birthdate, number_oscars) TO 'C:\Users\Vlad\developers_institute\practice\Week3\Day4\export_db_actors.csv' DELIMITER ',' CSV HEADER;

select * from actors;









