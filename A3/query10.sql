-- Retrieve the abbreviations of states containing at least 5 counties
-- and their ratio of snow per square megameter.
-- Order by area. 
-- Use ROUND() to round the result to 2 decimal places, eg., ROUND(1.2345, 2) = 1.23. 
-- (1 sq kilometer = 0.000001 sq megameter)

-- 1.05 marks: < 7 operators
-- 1.0 marks: < 8 operators
-- 0.8 marks: correct answer

SELECT abbr, (ROUND(SUM(snow)/SUM(sq_km)*1000000, 2)) AS snowAreaRatio FROM county
JOIN state ON (county.state=state.id)

GROUP BY state

HAVING COUNT(state)>=5

ORDER BY SUM(sq_km) ASC