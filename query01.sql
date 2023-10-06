-- Retrieve the abbreviations of states that have over 150 counties 
-- which have an employment rate of at least 90% for each county in 2008, 
-- ordered by the number of counties in each state in descending order.

-- 1.05 marks: <8 operators
-- 1.0 marks: <10 operators
-- 0.8 marks: correct answer

-- select the data ju want to display
SELECT abbr FROM county
-- join state table onto county state.id
JOIN state ON (county.state=state.id)
-- join countylabourstats table onto county.fips
JOIN countylabourstats ON (county.fips=countylabourstats.county)

-- check emplyement rate for each county and if it is in 2008
WHERE employed / labour_force >= 0.9 AND year=2008

-- condenscing the columns based by grouping them into unique states
GROUP BY state

-- check number of counties in a state
HAVING COUNT(state) >= 150
 

