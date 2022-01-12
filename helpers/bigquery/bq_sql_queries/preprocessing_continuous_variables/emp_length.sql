-- 1. Check unique values for column 'emp_length';
SELECT
    DISTINCT(emp_length)
FROM
    `data-science-325423.lending_club.data_from_2007_2014` 


-- 2. Replace each unique value by the correspondent numeric value.
SELECT emp_length,
    CASE emp_length
        WHEN '10+ years' THEN 10
        WHEN '9 years'   THEN 9
        WHEN '8 years'   THEN 8
        WHEN '7 years'   THEN 7
        WHEN '6 years'   THEN 6
        WHEN '5 years'   THEN 5
        WHEN '4 years'   THEN 4
        WHEN '3 years'   THEN 3
        WHEN '2 years'   THEN 2
        WHEN '1 year'    THEN 1
        WHEN '< 1 year'  THEN 0
        ELSE 0
    END AS emp_length_int,
FROM 
    `data-science-325423.lending_club.data_from_2007_2014`


-- That's all for emp_length column.