SELECT FirstName, LastName, City, State
FROM person AS p
LEFT JOIN address AS a 
ON p.personId = a.personId