WITH
StadiumOrdered AS(
    SELECT
        id,
        visit_date,
        people,
        LAG(people,1) OVER (ORDER BY id) AS peopleLag1,
        LAG(people,2) OVER (ORDER BY id) AS peopleLag2
    FROM Stadium),
ids AS(
    SELECT 
        id
    FROM StadiumOrdered
    WHERE 
        people >= 100
        AND peopleLag1 >= 100
        AND peopleLag2 >= 100)
SELECT
    id,
    visit_date,
    people
FROM Stadium
WHERE 
    id IN (SELECT id FROM ids)
    OR id IN (SELECT id-1 FROM ids)
    OR id IN (SELECT id-2 FROM ids)
ORDER BY
    visit_date