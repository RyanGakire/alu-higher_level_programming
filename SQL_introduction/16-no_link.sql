-- Lists the records of second_table that have a name
-- Skip the rows without a name and sort by descending score
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
