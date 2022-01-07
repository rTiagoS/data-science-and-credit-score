CREATE DATABASE IF NOT EXISTS LendingClub;

CREATE TABLE IF NOT EXISTS `LendingClub`.`src_loan_data_2007_2014` (
    `member_id` VARCHAR(255),
    `loan_amnt` VARCHAR(255),
    `funded_amnt` VARCHAR(255),
    `funded_amnt_inv` VARCHAR(255),
    `grade` VARCHAR(10),
    `sub_grade` VARCHAR(10),
    `int_rate` VARCHAR(255),
    `annual_inc` VARCHAR(255),
    `issue_d` VARCHAR(255),
    `loan_status` VARCHAR(255),
    `addr_state` VARCHAR(10),
    `mths_since_last_delinq` VARCHAR(255),
    `recoveries` VARCHAR(255),
    `annual_inc_joint` VARCHAR(255),
    `tot_coll_amt` VARCHAR(255), 
	`emp_length` VARCHAR(255),
    `earliest_cr_line`  VARCHAR(255),
    `term` VARCHAR(255),
    PRIMARY KEY(`member_id`)
    )
ENGINE = InnoDB;

DROP TABLE `LendingClub`.`src_loan_data_2007_2014`;

SELECT * FROM `LendingClub`.`src_loan_data_2007_2014`;

SHOW VARIABLES LIKE 'max_allowed_packet';

SET GLOBAL max_allowed_packet=524288000;

SELECT
	*
FROM
	`LendingClub`.`src_loan_data_2007_2014`
LIMIT 100



SELECT
	COUNT(*)
FROM
	`LendingClub`.`src_loan_data_2007_2014` t1
WHERE
	t1.loan_status IN(
		SELECT
			loan_status
		FROM
			`LendingClub`.`src_loan_data_2007_2014`
		WHERE
			loan_status IN ('Charged Off', 'Default','Does not meet the credit policy. Status:Charged Off','Late (31-120 days)')
	)


SELECT
	t1_0.grade,
    nr_bad_clients,
    nr_good_clients,
    *
FROM(


(SELECT
	COUNT(DISTINCT(member_id)) AS nr_bad_clients,
    SUM(COUNT(member_id)),
    grade
FROM
	`LendingClub`.`src_loan_data_2007_2014` t1
WHERE
	t1.loan_status IN ('Charged Off', 'Default','Does not meet the credit policy. Status:Charged Off','Late (31-120 days)')
GROUP BY
	grade) t1_0

LEFT JOIN

(SELECT
	COUNT(DISTINCT(member_id)) AS nr_good_clients,
    SUM(COUNT(member_id)),
    grade
FROM
	`LendingClub`.`src_loan_data_2007_2014` t2
WHERE
	t2.loan_status NOT IN ('Charged Off', 'Default','Does not meet the credit policy. Status:Charged Off','Late (31-120 days)')
GROUP BY
	grade) t2_0
ON
	t1_0.grade = t2_0.grade
)

SELECT
	COUNT(DISTINCT(member_id))
FROM
	`LendingClub`.`src_loan_data_2007_2014` t2
WHERE
	t2.loan_status NOT IN ('Charged Off', 'Default','Does not meet the credit policy. Status:Charged Off','Late (31-120 days)')
GROUP BY
	grade


SELECT
	loan_amnt AS bad_payers_loan_amnt
FROM
	`LendingClub`.`src_loan_data_2007_2014` t2
WHERE
	t2.loan_status NOT IN ('Charged Off', 'Default','Does not meet the credit policy. Status:Charged Off','Late (31-120 days)')
ORDER BY
	RAND()
LIMIT 10000



SELECT
	*
FROM(

SELECT
	annual_inc,
    'Good Payers' AS label
FROM
	`LendingClub`.`src_loan_data_2007_2014` t2
WHERE
	t2.loan_status NOT IN ('Charged Off', 'Default','Does not meet the credit policy. Status:Charged Off','Late (31-120 days)')
ORDER BY
	RAND()
LIMIT 10000
) AS A

UNION ALL

SELECT
	*
FROM(
SELECT
	 annual_inc,
    'Bad Payers' AS label
FROM
	`LendingClub`.`src_loan_data_2007_2014` t1
WHERE
	t1.loan_status IN ('Charged Off', 'Default','Does not meet the credit policy. Status:Charged Off','Late (31-120 days)')
ORDER BY
	RAND()
LIMIT 10000
) AS B
    
