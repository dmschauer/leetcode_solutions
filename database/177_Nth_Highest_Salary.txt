CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    DECLARE @res INT;
    
    WITH
    ranks AS
        (SELECT
            Salary, 
            DENSE_RANK() OVER (ORDER BY Salary DESC) as rank
        FROM Employee),
    result AS
        (SELECT Salary AS SecondHighestSalary
        FROM ranks
        WHERE rank = @N)
   SELECT @res = (SELECT ISNULL(
            (SELECT TOP 1 SecondHighestSalary FROM result),
            NULL) AS SecondHighestSalary);

    RETURN(@res);
END
