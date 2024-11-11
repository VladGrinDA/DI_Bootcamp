-- database: ../ExerciseXP/olympics.db


-- Exercise 1

-- Task 1: Cross-season medalists
CREATE TEMPORARY TABLE cross_season_medalists AS
WITH SeasonMedals AS (
    SELECT 
        p.id as person_id,
        p.full_name,
        g.season,
        COUNT(ce.medal_id) as medal_count
    FROM person p
    JOIN games_competitor gc ON gc.person_id = p.id
    JOIN games g ON g.id = gc.games_id
    JOIN competitor_event ce ON ce.competitor_id = gc.id
    WHERE ce.medal_id IS NOT NULL
    GROUP BY p.id, p.full_name, g.season
)
SELECT 
    person_id,
    full_name,
    SUM(CASE WHEN season = 'Summer' THEN medal_count ELSE 0 END) as summer_medals,
    SUM(CASE WHEN season = 'Winter' THEN medal_count ELSE 0 END) as winter_medals,
    SUM(medal_count) as total_medals
FROM SeasonMedals
GROUP BY person_id, full_name
HAVING COUNT(DISTINCT season) = 2;

SELECT * FROM cross_season_medalists;

-- Task 2: Two-sport medalists
CREATE TEMPORARY TABLE two_sport_medalists AS
WITH SportMedals AS (
    SELECT 
        p.id as person_id,
        p.full_name,
        s.sport_name,
        COUNT(ce.medal_id) as medal_count
    FROM person p
    JOIN games_competitor gc ON gc.person_id = p.id
    JOIN competitor_event ce ON ce.competitor_id = gc.id
    JOIN event e ON e.id = ce.event_id
    JOIN sport s ON s.id = e.sport_id
    WHERE ce.medal_id IS NOT NULL
    GROUP BY p.id, p.full_name, s.sport_name
)
SELECT 
    person_id,
    full_name,
    GROUP_CONCAT(sport_name) as sports,
    SUM(medal_count) as total_medals
FROM SportMedals
GROUP BY person_id, full_name
HAVING COUNT(DISTINCT sport_name) = 2
ORDER BY total_medals DESC
LIMIT 3;

SELECT * FROM two_sport_medalists;


-- Exercise 2

-- Task 1: Top 5 regions by highest medal counts in single events
WITH CompetitorEventMedals AS (
    SELECT 
        p.id as person_id,
        nr.id as region_id,
        nr.region_name,
        e.event_name,
        COUNT(ce.medal_id) as medal_count
    FROM person p
    JOIN person_region pr ON pr.person_id = p.id
    JOIN noc_region nr ON nr.id = pr.region_id
    JOIN games_competitor gc ON gc.person_id = p.id
    JOIN competitor_event ce ON ce.competitor_id = gc.id
    JOIN event e ON e.id = ce.event_id
    WHERE ce.medal_id IS NOT NULL
    GROUP BY p.id, nr.id, nr.region_name, e.event_name
)
SELECT 
    region_name,
    COUNT(person_id) as medalist_count,
    SUM(medal_count) as total_medals
FROM CompetitorEventMedals
GROUP BY region_id, region_name
ORDER BY total_medals DESC
LIMIT 5;

-- Task 2: Multi-game participants without medals
DROP TABLE IF EXISTS non_medalist_veterans;

CREATE TEMPORARY TABLE non_medalist_veterans AS
SELECT 
    p.id as person_id,
    p.full_name,
    COUNT(DISTINCT gc.games_id) as games_participated
FROM person p
JOIN games_competitor gc ON gc.person_id = p.id
WHERE p.id NOT IN (
    SELECT DISTINCT gc2.person_id
    FROM games_competitor gc2
    JOIN competitor_event ce ON ce.competitor_id = gc2.id
    WHERE ce.medal_id IS NOT NULL AND ce.medal_id != 4
)
GROUP BY p.id, p.full_name
HAVING COUNT(DISTINCT gc.games_id) > 3
ORDER BY games_participated DESC;

SELECT * FROM non_medalist_veterans;
