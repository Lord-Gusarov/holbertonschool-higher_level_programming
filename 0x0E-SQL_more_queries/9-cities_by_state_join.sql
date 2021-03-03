-- Task: Write a script that lists all cities contained in the database hbtn_0d_usa.
-- Each record should display: cities.id - cities.name - states.name
-- Results must be sorted in ascending order by cities.id
SELECT *
FROM cities
NATURAL JOIN states
ORDER BY cities.id;
