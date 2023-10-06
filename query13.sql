-- Retrieve names of top 10 counties and 
-- their growth ratio in terms of population compared between the latest census year and the oldest census year, 
-- in an descending order by their growth ratio.

-- 1.05 marks: < 15 operators
-- 1.0 marks: < 17 operators
-- 0.9 marks: < 19 operators
-- 0.8 marks: correct answer

SELECT name, newest.population/oldest.population AS popGrowthRatio 
FROM countypopulation AS oldest
JOIN county ON (oldest.county = county.fips)
JOIN countypopulation AS newest ON oldest.county = newest.county

WHERE oldest.year=(
	SELECT MIN(censusyear.year)
    FROM censusyear
)
AND newest.year=(
	SELECT MAX(censusyear.year)
    FROM censusyear
)

ORDER BY popGrowthRatio DESC
LIMIT 10
