-- Lists how many records share the same score in second_table
-- Group the rows by score and sort by the number of rows
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;
