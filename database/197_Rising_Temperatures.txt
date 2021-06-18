/* 
Works and is accepted but rather slow
Runtime: 2989 ms, faster than 5.54% 

WITH 
lags AS(
    SELECT
        id, recordDate, Temperature,
        LAG(Temperature,1) OVER (ORDER BY recordDate) AS TemperatureLag1,
        LAG(recordDate,1) OVER (ORDER BY recordDate) AS recordDateLag1
    FROM Weather)
SELECT  id
FROM    lags
WHERE   
    Temperature > TemperatureLag1
    AND DATEADD(DAY,-1,recordDate) = recordDateLag1*/
    
--Runtime: 917 ms, faster than 82.44% 
SELECT w1.Id
FROM Weather AS w1
JOIN Weather AS w2
    ON DATEADD(DAY,-1,w1.recordDate) = w2.recordDate
WHERE 
    w1.Temperature > w2.Temperature