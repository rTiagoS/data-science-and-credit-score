-- Execute the query below to calculate the amount of months for each row since 2017-12-01.

SELECT
    issue_d,

    DATETIME(PARSE_TIMESTAMP("%b-%y", issue_d)) AS issue_d_dt,

    DATETIME(TIMESTAMP("2017-12-01 00:00:00+00")) AS dt_ref,

    DATETIME_DIFF(DATETIME(TIMESTAMP("2017-12-01 00:00:00+00")), DATETIME(PARSE_TIMESTAMP("%b-%y", issue_d)), MONTH) AS mths_since_issue_d

FROM
    `data-science-325423.lending_club.data_from_2007_2014` 

-- That's all.