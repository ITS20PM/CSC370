-- Out of those counties with temperature of more than 60, 
-- retrieve the pair that had the largest absolute difference in temperature
-- and their corresponding temperatures.
-- The second county in the pair has a temperature larger than the first county's temperature. 
-- If multiple pairs exist, retrieve the pair with the smallest FIP of the first county in the pair.


-- 1.05 marks: < 10 operators
-- 1.0 marks: < 12 operators
-- 0.8 marks: correct answer

SELECT lower.name, lower.temp, higher.name, higher.temp
FROM county AS lower
JOIN county AS higher

WHERE lower.temp > 60 
AND higher.temp > lower.temp

ORDER BY (higher.temp-lower.temp) DESC, lower.fips ASC
LIMIT 1
