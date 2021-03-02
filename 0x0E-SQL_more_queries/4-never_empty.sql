-- Write a script that creates the table id_not_null 
-- id default value of  1, cant be NULL
CREATE TABLE IF NOT EXISTS id_not_null(
	id INT NOT NULL DEFAULT 1,
	name VARCHAR(256));
