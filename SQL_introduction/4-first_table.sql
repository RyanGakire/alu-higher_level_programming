-- Creates the table first_table in the current database
-- Create the table only when it is missing
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
