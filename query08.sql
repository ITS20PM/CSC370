-- Retrieve the list of counties sorted by the ratio 
-- between male and female population for each county 
-- in descending order or the aforementioned ratio, and then in the ascending order of county FIP.
-- Exclude tuples with ratio of 1:1 from returned result.

-- 1.05 marks: < 7 operators
-- 1.0 marks: < 8 operators
-- 0.8 marks: correct answer

SELECT male.county AS county, male.population/female.population AS ratio 
FROM genderbreakdown AS male
JOIN genderbreakdown AS female ON male.county = female.county

WHERE male.gender='male'
AND female.gender='female'
AND male.population/female.population!=1

ORDER BY ratio DESC, male.county ASC