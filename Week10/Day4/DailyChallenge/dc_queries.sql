-- database: ./database.sqlite


SELECT name 
FROM sqlite_master 
WHERE type='table';

SELECT * FROM sqlite_master WHERE type='table' ORDER BY name;


-- Query 1: Select All Columns from Player's Table
SELECT * FROM Player_Match;

-- Query 2: Batsman vs Runs
SELECT 
    p.Player_Name,
    SUM(bs.Runs_Scored) as Total_Runs
FROM Ball_by_Ball bb
JOIN Batsman_Scored bs ON bb.Match_Id = bs.Match_Id 
    AND bb.Over_Id = bs.Over_Id 
    AND bb.Ball_Id = bs.Ball_Id
    AND bb.Innings_No = bs.Innings_No
JOIN Player p ON bb.Striker = p.Player_Id
GROUP BY p.Player_Id, p.Player_Name
ORDER BY Total_Runs DESC;

-- Query 3: Fifties and Hundreds
WITH BatsmanInnings AS (
    SELECT 
        p.Player_Id,
        p.Player_Name,
        bb.Match_Id,
        SUM(bs.Runs_Scored) as Innings_Runs
    FROM Ball_by_Ball bb
    JOIN Batsman_Scored bs ON bb.Match_Id = bs.Match_Id 
        AND bb.Over_Id = bs.Over_Id 
        AND bb.Ball_Id = bs.Ball_Id
        AND bb.Innings_No = bs.Innings_No
    JOIN Player p ON bb.Striker = p.Player_Id
    GROUP BY p.Player_Id, p.Player_Name, bb.Match_Id
)
SELECT 
    Player_Name,
    COUNT(CASE WHEN Innings_Runs >= 50 AND Innings_Runs < 100 THEN 1 END) as Fifties,
    COUNT(CASE WHEN Innings_Runs >= 100 THEN 1 END) as Hundreds
FROM BatsmanInnings
GROUP BY Player_Id, Player_Name
HAVING Fifties > 0 OR Hundreds > 0
ORDER BY Hundreds DESC, Fifties DESC;

-- Query 4: Best Bowling Figures
WITH BowlingFigures AS (
    SELECT 
        p.Player_Id,
        p.Player_Name,
        bb.Match_Id,
        COUNT(wt.Player_Out) as Wickets,
        SUM(COALESCE(bs.Runs_Scored, 0)) as Runs_Conceded
    FROM Ball_by_Ball bb
    LEFT JOIN Wicket_Taken wt ON bb.Match_Id = wt.Match_Id 
        AND bb.Over_Id = wt.Over_Id 
        AND bb.Ball_Id = wt.Ball_Id
        AND bb.Innings_No = wt.Innings_No
    LEFT JOIN Batsman_Scored bs ON bb.Match_Id = bs.Match_Id 
        AND bb.Over_Id = bs.Over_Id 
        AND bb.Ball_Id = bs.Ball_Id
        AND bb.Innings_No = bs.Innings_No
    JOIN Player p ON bb.Bowler = p.Player_Id
    GROUP BY p.Player_Id, p.Player_Name, bb.Match_Id
),
BestSpells AS (
    SELECT 
        Player_Id,
        Player_Name,
        Wickets,
        Runs_Conceded,
        ROW_NUMBER() OVER (PARTITION BY Player_Id ORDER BY Wickets DESC, Runs_Conceded) as spell_rank
    FROM BowlingFigures
)
SELECT 
    Player_Name,
    Wickets as Best_Wickets,
    Runs_Conceded as Runs_In_Best_Spell
FROM BestSpells
WHERE spell_rank = 1 AND Wickets > 0
ORDER BY Best_Wickets DESC, Runs_In_Best_Spell;

-- Query 5: Comprehensive Career Metrics
WITH PlayerStats AS (
    -- Batting Stats
    SELECT 
        p.Player_Id,
        p.Player_Name,
        COUNT(DISTINCT bb.Match_Id) as Matches_Played,
        SUM(bs.Runs_Scored) as Total_Runs,
        COUNT(wt.Player_Out) as Times_Out,
        ROUND(CAST(SUM(bs.Runs_Scored) AS FLOAT) / NULLIF(COUNT(wt.Player_Out), 0), 2) as Batting_Average,
        -- Bowling Stats
        COUNT(DISTINCT CASE WHEN bb.Bowler = p.Player_Id THEN bb.Match_Id END) as Matches_Bowled,
        COUNT(CASE WHEN bb.Bowler = p.Player_Id THEN wt.Player_Out END) as Wickets_Taken,
        SUM(CASE WHEN bb.Bowler = p.Player_Id THEN bs.Runs_Scored END) as Runs_Conceded
    FROM Player p
    LEFT JOIN Ball_by_Ball bb ON p.Player_Id IN (bb.Striker, bb.Bowler)
    LEFT JOIN Batsman_Scored bs ON bb.Match_Id = bs.Match_Id 
        AND bb.Over_Id = bs.Over_Id 
        AND bb.Ball_Id = bs.Ball_Id
        AND bb.Innings_No = bs.Innings_No
    LEFT JOIN Wicket_Taken wt ON bb.Match_Id = wt.Match_Id 
        AND bb.Over_Id = wt.Over_Id 
        AND bb.Ball_Id = wt.Ball_Id
        AND bb.Innings_No = wt.Innings_No
    GROUP BY p.Player_Id, p.Player_Name
)
SELECT 
    Player_Name,
    Matches_Played,
    Total_Runs,
    Batting_Average,
    Wickets_Taken,
    CASE 
        WHEN Wickets_Taken > 0 THEN ROUND(CAST(Runs_Conceded AS FLOAT) / Wickets_Taken, 2)
        ELSE NULL
    END as Bowling_Average
FROM PlayerStats
WHERE Total_Runs > 0 OR Wickets_Taken > 0
ORDER BY Total_Runs DESC, Wickets_Taken DESC;