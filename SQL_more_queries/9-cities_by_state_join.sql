-- Display info of 2 tables
-- DML Query
SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id=states.id ORDER BY cities.id ASC;
