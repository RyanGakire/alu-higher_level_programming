-- Creates the table id_not_null where the id has a default value
-- Create the table only when it is missing
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
