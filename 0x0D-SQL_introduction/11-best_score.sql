-- Task: List all records from second_table, showing just score and name.. ordered by score
-- Selecting the rows with scores >= 10 and how to order them
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
