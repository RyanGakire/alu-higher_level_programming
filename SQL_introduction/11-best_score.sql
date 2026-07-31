-- Lists the records of second_table with a score of 10 or more
-- Select the score and the name, ordered from the highest score
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
