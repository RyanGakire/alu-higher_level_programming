-- Lists all the cities of California, without using JOIN
-- Find the id of California first, then the cities that use it
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id;
