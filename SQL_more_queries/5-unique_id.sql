-- Creates the table unique_id where the id cannot be used twice
-- Create the table only when it is missing
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
