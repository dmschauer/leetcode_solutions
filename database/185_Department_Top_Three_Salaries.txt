WITH 
ranks AS(
    SELECT
        d.Name AS Department, 
        e.Name AS Employee, 
        e.Salary AS Salary,
        DENSE_RANK() OVER (PARTITION BY d.Id ORDER BY e.Salary DESC) AS rank
    FROM Employee AS e
    LEFT JOIN Department AS d
        ON e.DepartmentId = d.Id)
SELECT 
    Department, 
    Employee,
    Salary
FROM ranks
WHERE
    rank <= 3
    AND Department IS NOT NULL