WITH
counts AS
(SELECT
    Email,
    COUNT(*) AS cnt
FROM Person
GROUP BY Email)
SELECT Email
FROM counts
WHERE cnt >= 2