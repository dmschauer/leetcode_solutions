SELECT 
    t.Request_At AS Day,
    ROUND(1.0 - CONVERT(NUMERIC,SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END)) / 
    CONVERT(NUMERIC,COUNT(*)),2)  AS 'Cancellation Rate'
FROM
    Trips AS t
JOIN Users AS c
    ON t.Client_Id = c.Users_Id
    AND c.Role = 'client'
    AND c.Banned = 'No'
JOIN Users AS d
    ON t.Driver_id = d.Users_Id
    AND d.Role = 'driver'
    AND d.Banned = 'No'
WHERE
    t.Request_At BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY 
    t.Request_At