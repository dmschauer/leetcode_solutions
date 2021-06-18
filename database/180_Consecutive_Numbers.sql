WITH
LogsOrdered AS
(SELECT
    Num,
    LAG(Num,1) OVER (ORDER BY Id) AS NumLag1,
    LAG(Num,2) OVER (ORDER BY Id) AS NumLag2
FROM Logs)
SELECT DISTINCT Num AS ConsecutiveNums
FROM LogsOrdered
WHERE 
    Num = NumLag1 
    AND Num = NumLag2