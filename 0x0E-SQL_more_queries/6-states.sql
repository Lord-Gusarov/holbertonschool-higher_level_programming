-- Write a script that creates the database hbtn_0d_usa and the table states. 
-- states description //id INT unique, auto generated, can’t be null and is a primary key //name VARCHAR(256) can’t be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Selecting Database
USE hbtn_0d_usa;
-- Creating table states
CREATE TABLE IF NOT EXISTS states(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL);
