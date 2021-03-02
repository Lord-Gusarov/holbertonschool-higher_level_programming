-- Task: Write a script that converts hbtn_0c_0 database to UTF8
-- Converting Database to utf8
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
-- Selecting database
USE hbtn_0c_0;
-- Converting table first_table to utf8
ALTER TABLE first_table CONVERT TO
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
-- Converting field `name` in first_table
ALTER TABLE first_table
MODIFY name VARCHAR(256)
COLLATE utf8mb4_unicode_ci;
