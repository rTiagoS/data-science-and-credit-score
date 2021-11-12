-- 1. Check unique values for column 'term'
SELECT
    DISTINCT(term)
FROM
    `data-science-325423.lending_club.data_from_2007_2014` 




-- 2. Replace each unique value by the correspondent numeric value.

SELECT 
    CASE term
        WHEN ' 36 months' THEN 36
        WHEN ' 60 months' THEN 60
        ELSE 0
    END AS term_int,
FROM
    `data-science-325423.lending_club.data_from_2007_2014`

-- That's all here.