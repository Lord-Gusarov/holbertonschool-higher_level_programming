-- Write a script that creates the database hbtn_0d_2 and the user user_0d_2.
-- User_0d_2 should have only SELECT privilege in the database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Creating User
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- SELECT Privilige for new user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
