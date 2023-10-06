-- Retrieve the list of states (showing both the id and abbreviation) 
-- and their corresponding total area, 
-- not accounting for the counties that have more than 10000 population in the year of 2010, 
-- sorted by area in descending order.

-- 1.05 marks: < 11 operators
-- 1.0 marks: < 13 operators
-- 0.8 marks: correct answer

-- select the columns to display
SELECT id, abbr, SUM(sq_km) AS area FROM county

-- format the table
JOIN state ON (county.state=state.id)
JOIN countypopulation ON (county.fips=countypopulation.county)

-- check for county where year = 2010 and population <= 10000
WHERE year=2010 and population<=10000

-- condescing the table
GROUP BY state

-- sort in descending order
ORDER BY area DESC;
