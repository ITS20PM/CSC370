-- Retrieve all states that have their abbreviartion names starting with 'A' 
-- and contain at least 20 counties,
-- ordered by the total area. 

-- 1.05 marks: < 7 operators
-- 1.0 marks: < 8 operators
-- 0.8 marks: correct answer

-- display the output
SELECT abbr FROM county

-- format the table
JOIN state ON (county.state=state.id)

-- check if the first char in abbr value = A
WHERE LEFT(abbr, 1)='A'

-- organize the table by their unique state column
GROUP BY state

-- check for the number of counties in each state >= 20
HAVING COUNT(state)>=20