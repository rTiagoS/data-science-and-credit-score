-- Check missing values distribution along the dataset columns
SELECT
    column_name,
    COUNT(1) AS nulls_count
FROM `data-science-325423.lending_club.data_from_2007_2014` AS lending_club_data,
     UNNEST(REGEXP_EXTRACT_ALL(TO_JSON_STRING(lending_club_data), r'"(\w+)":null')) column_name
GROUP BY column_name
ORDER BY nulls_count DESC



SELECT 
    total_rev_hi_lim, 
    IFNULL(total_rev_hi_lim, funded_amnt) AS total_rev_hi_lim_clean,
    funded_amnt
FROM 
    `data-science-325423.lending_club.data_from_2007_2014`

SELECT 
    annual_inc, 
    CAST(IFNULL(annual_inc, (SELECT AVG(annual_inc) FROM `data-science-325423.lending_club.data_from_2007_2014`)) AS INT64) as annual_inc_cleaned,
FROM 
    `data-science-325423.lending_club.data_from_2007_2014`






SELECT 

    -- IFNULL(mths_since_earliest_cr_line, 0) AS mths_since_earliest_cr_line,
    IFNULL(acc_now_delinq, 0) AS acc_now_delinq_cl,
    IFNULL(total_acc, 0) AS total_acc_cl,
    IFNULL(pub_rec, 0) AS pub_rec_cl,
    IFNULL(open_acc, 0) AS open_acc_cl,
    IFNULL(inq_last_6mths, 0) AS inq_last_6mths_cl,
    IFNULL(delinq_2yrs, 0) AS delinq_2yrs,
    -- IFNULL(emp_length_int, 0) AS emp_length_int_cl    



FROM 
    `data-science-325423.lending_club.data_from_2007_2014`