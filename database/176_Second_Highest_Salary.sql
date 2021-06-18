WITH
ranks AS
(SELECT
    Salary, 
    RANK() OVER (ORDER BY Salary DESC) as rank
FROM Employee),
result AS
(SELECT Salary AS SecondHighestSalary
FROM ranks
WHERE rank = 2)
SELECT ISNULL(
        (SELECT TOP 1 SecondHighestSalary FROM result),
        NULL) AS SecondHighestSalary