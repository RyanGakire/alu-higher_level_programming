-- Creates the table force_name where a name is always needed
-- Create the table only when it is missing
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
