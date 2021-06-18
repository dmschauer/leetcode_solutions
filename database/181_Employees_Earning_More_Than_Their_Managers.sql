SELECT e.Name AS Employee 
FROM Employee AS e
LEFT JOIN Employee AS m 
    ON e.ManagerId = m.Id
WHERE
    e.Salary > m.Salary