-- Execute this query to get the amount of month between two dates.

-- NOTE: To deal with negative date_time diffs, negatives values month were replaced by the maximum amount of month found (587). 

-- 1. Found the maximum amount of month.
SELECT
    MAX(mths_since_earlist_cr_line)
FROM(
SELECT
    earliest_cr_line,

    DATETIME(PARSE_TIMESTAMP("%b-%y", earliest_cr_line)) AS earliest_cr_line_dt,

    DATETIME(TIMESTAMP("2017–12–01 00:00:00+00")) AS dt_ref,

    DATETIME_DIFF(DATETIME(TIMESTAMP("2017–12–01 00:00:00+00")), DATETIME(PARSE_TIMESTAMP("%b-%y", earliest_cr_line)), MONTH) AS mths_since_earlist_cr_line
FROM
    `data-science-325423.lending_club.data_from_2007_2014`
)


-- 2. Execute this query to replace negative values by the maximum found in mths_since_earliest_cr_line column.
SELECT 
    *,
    IF (mths_since_earliest_cr_line < 0, 587, mths_since_earliest_cr_line) AS mths_since_earliest_cr_line_adj

FROM
(
  SELECT
    earliest_cr_line,

    DATETIME(PARSE_TIMESTAMP("%b-%y", earliest_cr_line)) AS earliest_cr_line_dt,

    DATETIME(TIMESTAMP("2017-12-01 00:00:00+00")) AS dt_ref,

    DATETIME_DIFF(DATETIME(TIMESTAMP("2017-12-01 00:00:00+00")), DATETIME(PARSE_TIMESTAMP("%b-%y", earliest_cr_line)), MONTH) AS mths_since_earliest_cr_line

FROM
    `data-science-325423.lending_club.data_from_2007_2014`  
)
