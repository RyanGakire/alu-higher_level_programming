-- Creates the user user_0d_1 with all the privileges on the server
-- Create the user only when it is missing, with its password
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Give the user every privilege on every database
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
