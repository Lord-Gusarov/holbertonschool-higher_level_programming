-- Write a script that creates the table force_name
-- If the table exists, the script should'nt fail
CREATE TABLE IF NOT EXISTS force_name(
	id INT,
	name VARCHAR(256) NOT NULL);
