SELECT 
    id,
    CASE 
        WHEN id%2 = 0 THEN LAG(student,1) OVER (ORDER BY id)
        ELSE ISNULL(LEAD(student,1) OVER (ORDER BY id), student)
    END AS student
FROM seat
ORDER BY id