WITH customerIds AS
(SELECT DISTINCT c.ID
FROM Customers AS c
LEFT JOIN Orders AS o 
    ON c.Id = o.CustomerId
WHERE
    o.Id IS NULL)
SELECT Name AS Customers
FROM Customers
WHERE Id IN (SELECT Id From customerIds)