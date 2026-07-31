-- Creates the database hbtn_0d_2 and a user that can only read it
-- Create the database only when it is missing
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create the user only when it is missing, with its password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Give the user the right to read that database only
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
