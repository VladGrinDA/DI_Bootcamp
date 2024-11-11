-- database: ./olympics.db

SELECT * FROM 
sqlite_master WHERE type='table' ORDER BY name;

-- Exercise 1

-- Task 1: Average age of medalists by medal type
SELECT 
    m.medal_name,
    AVG(gc.age) AS average_age
FROM medal m
JOIN competitor_event ce ON ce.medal_id = m.id
JOIN games_competitor gc ON gc.id = ce.competitor_id
WHERE m.medal_name IS NOT NULL
GROUP BY m.medal_name;

-- Task 2: Top 5 regions with most competitors in >3 events
SELECT 
    nr.region_name,
    COUNT(DISTINCT gc.person_id) AS competitor_count
FROM noc_region nr
JOIN person_region pr ON pr.region_id = nr.id
JOIN games_competitor gc ON gc.person_id = pr.person_id
WHERE gc.person_id IN (
    SELECT competitor_id 
    FROM competitor_event 
    GROUP BY competitor_id
    HAVING COUNT(DISTINCT event_id) > 3
)
GROUP BY nr.region_name
ORDER BY competitor_count DESC
LIMIT 5;

-- Task 3: Temporary table for multiple medalists
DROP TABLE IF EXISTS competitor_medals;

CREATE TEMPORARY TABLE competitor_medals AS
SELECT 
    gc.person_id,
    p.full_name,
    COUNT(ce.medal_id) FILTER (WHERE ce.medal_id IS NOT NULL AND ce.medal_id != 4) as medal_count
FROM person p
LEFT JOIN games_competitor gc ON gc.person_id = p.id
LEFT JOIN competitor_event ce ON ce.competitor_id = gc.id
GROUP BY gc.person_id, p.full_name;

SELECT * FROM competitor_medals WHERE medal_count > 2;
SELECT * FROM competitor_medals WHERE medal_count = 0;

-- Task 4: Delete non-medalists from temporary table
DELETE FROM competitor_medals
WHERE person_id IN (
    SELECT gc.person_id
    FROM games_competitor gc
    LEFT JOIN competitor_event ce ON ce.competitor_id = gc.id
    WHERE ce.medal_id IS NULL OR ce.medal_id = 4
);

SELECT gc.person_id
    FROM games_competitor gc
LEFT JOIN competitor_event ce ON ce.competitor_id = gc.id
WHERE ce.medal_id IS NULL OR ce.medal_id = 4;

SELECT * FROM competitor_medals WHERE medal_count = 0;

-- Exercise 2

-- Task 1: Update heights based on regional averages
UPDATE person
SET height = (
    SELECT AVG(p2.height)
    FROM person p2
    JOIN person_region pr2 ON pr2.person_id = p2.id
    WHERE pr2.region_id = (
        SELECT pr3.region_id 
        FROM person_region pr3 
        WHERE pr3.person_id = person.id
    )
    AND p2.height IS NOT NULL
)
WHERE height IS NULL;

SELECT * FROM person WHERE height IS NULL;

-- Task 2: Create temp table for multi-event participants
DROP TABLE IF EXISTS multi_event_participants;

CREATE TEMPORARY TABLE multi_event_participants AS
SELECT 
    gc.person_id,
    p.full_name,
    gc.games_id,
    COUNT(DISTINCT ce.event_id) as event_count
FROM games_competitor gc
JOIN person p ON p.id = gc.person_id
JOIN competitor_event ce ON ce.competitor_id = gc.id
GROUP BY gc.person_id, p.full_name, gc.games_id
HAVING COUNT(DISTINCT ce.event_id) > 1;

SELECT * FROM multi_event_participants;

-- Task 3: Regions with above-average medal counts
WITH RegionMedalAvg AS (
    SELECT 
        nr.id,
        nr.region_name,
        COUNT(ce.medal_id) * 1.0 / COUNT(DISTINCT gc.person_id) as medals_per_competitor
    FROM noc_region nr
    JOIN person_region pr ON pr.region_id = nr.id
    JOIN games_competitor gc ON gc.person_id = pr.person_id
    LEFT JOIN competitor_event ce ON ce.competitor_id = gc.id
    GROUP BY nr.id, nr.region_name
)
SELECT *
FROM RegionMedalAvg
WHERE medals_per_competitor > (
    SELECT AVG(medals_per_competitor)
    FROM RegionMedalAvg
);

-- Task 4: Track cross-season participants
DROP TABLE IF EXISTS season_participants;

CREATE TEMPORARY TABLE season_participants AS
SELECT 
    gc.person_id,
    p.full_name,
    GROUP_CONCAT(DISTINCT g.season) as seasons,
    COUNT(DISTINCT g.season) as season_count
FROM games_competitor gc
JOIN person p ON p.id = gc.person_id
JOIN games g ON g.id = gc.games_id
GROUP BY gc.person_id, p.full_name
HAVING COUNT(DISTINCT g.season) > 1;

SELECT * FROM season_participants;