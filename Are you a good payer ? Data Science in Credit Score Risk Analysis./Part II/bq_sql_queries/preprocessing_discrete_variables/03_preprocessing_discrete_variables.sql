-- Preprocessing dummies variables with SQL. 

-- Dummies variables considered: grade, sub_grade, home_ownership, verification_status, loan_status, purpose, addr_state and initial_list_status

-- Step 1: Get the unique values for the categorical column given above.
-- Step 2: Implement a python script to generate the SQL query for each column.

-- With step 1 and step 2, it is possible to turn hard queries into simple ones. Following is presented an example for each step.


-- Step 1: Execute this sql script to display unique values for each column considered. (It was generated from i_python_script_sql_generator.py script file.)

SELECT
  *
FROM (
  SELECT
    'grade' AS variable,
    FORMAT("%T", ARRAY_AGG(grade)) AS dummies_categories
  FROM (
    SELECT
      DISTINCT grade AS grade,
    FROM
      `data-science-325423.lending_club.data_from_2007_2014`)
  UNION ALL
  SELECT
    'sub_grade' AS variable,
    FORMAT("%T", ARRAY_AGG(sub_grade)) AS dummies_categories
  FROM (
    SELECT
      DISTINCT sub_grade AS sub_grade,
    FROM
      `data-science-325423.lending_club.data_from_2007_2014`)
  UNION ALL
  SELECT
    'home_ownership' AS variable,
    FORMAT("%T", ARRAY_AGG(home_ownership)) AS dummies_categories
  FROM (
    SELECT
      DISTINCT home_ownership AS home_ownership,
    FROM
      `data-science-325423.lending_club.data_from_2007_2014`)
  UNION ALL
  SELECT
    'verification_status' AS variable,
    FORMAT("%T", ARRAY_AGG(verification_status)) AS dummies_categories
  FROM (
    SELECT
      DISTINCT verification_status AS verification_status,
    FROM
      `data-science-325423.lending_club.data_from_2007_2014`)
  UNION ALL
  SELECT
    'loan_status' AS variable,
    FORMAT("%T", ARRAY_AGG(loan_status)) AS dummies_categories
  FROM (
    SELECT
      DISTINCT loan_status AS loan_status,
    FROM
      `data-science-325423.lending_club.data_from_2007_2014`)
  UNION ALL
  SELECT
    'purpose' AS variable,
    FORMAT("%T", ARRAY_AGG(purpose)) AS dummies_categories
  FROM (
    SELECT
      DISTINCT purpose AS purpose,
    FROM
      `data-science-325423.lending_club.data_from_2007_2014`)
  UNION ALL
  SELECT
    'addr_state' AS variable,
    FORMAT("%T", ARRAY_AGG(addr_state)) AS dummies_categories
  FROM (
    SELECT
      DISTINCT addr_state AS addr_state,
    FROM
      `data-science-325423.lending_club.data_from_2007_2014`)
  UNION ALL
  SELECT
    'initial_list_status' AS variable,
    FORMAT("%T", ARRAY_AGG(initial_list_status)) AS dummies_categories
  FROM (
    SELECT
      DISTINCT initial_list_status AS initial_list_status,
    FROM
      `data-science-325423.lending_club.data_from_2007_2014`)
    )

-- OUTPUT EX: 	["A", "B", "C", "D", "E", "F", "G"]  | OBS: This array will be used as input for our python script sql generator.

-- Step 2: Run ii_python_script_sql_generator.py script file.

-- Finally, copy and paste the python script output (grade_sql.txt) to the following query:

SELECT -- [COLUMN],

    -- PASTE HERE

FROM `data-science-325423.lending_club.data_from_2007_2014`



-- Example:

SELECT grade,

CASE grade
	WHEN 'A' THEN 1
	ELSE 0
END AS grade_A,
CASE grade
	WHEN 'B' THEN 1
	ELSE 0
END AS grade_B,
CASE grade
	WHEN 'C' THEN 1
	ELSE 0
END AS grade_C,
CASE grade
	WHEN 'D' THEN 1
	ELSE 0
END AS grade_D,
CASE grade
	WHEN 'E' THEN 1
	ELSE 0
END AS grade_E,
CASE grade
	WHEN 'F' THEN 1
	ELSE 0
END AS grade_F,
CASE grade
	WHEN 'G' THEN 1
	ELSE 0
END AS grade_G,

FROM `data-science-325423.lending_club.data_from_2007_2014`

-- Do the same to the remaining (manual work of copy and paste here):

SELECT 

    CASE home_ownership
		WHEN 'MORTGAGE' THEN 1
		ELSE 0
	END AS home_ownership_MORTGAGE,
	CASE home_ownership
		WHEN 'RENT' THEN 1
		ELSE 0
	END AS home_ownership_RENT,
	CASE home_ownership
		WHEN 'OWN' THEN 1
		ELSE 0
	END AS home_ownership_OWN,
	CASE home_ownership
		WHEN 'OTHER' THEN 1
		ELSE 0
	END AS home_ownership_OTHER,
	CASE home_ownership
		WHEN 'NONE' THEN 1
		ELSE 0
	END AS home_ownership_NONE,
	CASE home_ownership
		WHEN 'ANY' THEN 1
		ELSE 0
	END AS home_ownership_ANY,


FROM `data-science-325423.lending_club.data_from_2007_2014`