-- Lists all the cities with the name of their state
-- Join the two tables on the state id
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
