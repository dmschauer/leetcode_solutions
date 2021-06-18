DELETE p1
FROM Person AS p1
JOIN Person AS p2
    ON p1.Email = p2.Email
    AND p1.Id > P2.Id
