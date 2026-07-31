-- Creates the database hbtn_0d_usa and the table states
-- Create the database only when it is missing
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Work inside that database
USE hbtn_0d_usa;
-- Create the table only when it is missing
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
