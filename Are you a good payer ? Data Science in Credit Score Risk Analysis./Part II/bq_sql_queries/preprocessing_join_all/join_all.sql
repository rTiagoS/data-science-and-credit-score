SELECT 
    * EXCEPT(emp_length_int, mths_since_earliest_cr_line),
    IFNULL(mths_since_earliest_cr_line, 0) AS mths_since_earliest_cr_line_cl,
    IFNULL(emp_length_int, 0) AS emp_length_int_cl


FROM(

SELECT 
    id,
    member_id,

    -- * * * * * * * * * * * * * * * * * * * * * * * * Continuous Variables Preprocessing * * * * * * * * * * * * * * * * * * * * * * * * ---
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

    CASE term
        WHEN ' 36 months' THEN 36
        WHEN ' 60 months' THEN 60
        ELSE 0
    END AS term_int,

    DATETIME_DIFF(DATETIME(TIMESTAMP("2017-12-01 00:00:00+00")), DATETIME(PARSE_TIMESTAMP("%b-%y", issue_d)), MONTH) AS mths_since_issue_d,

    IF(
        (DATETIME_DIFF(DATETIME(TIMESTAMP("2017-12-01 00:00:00+00")), DATETIME(PARSE_TIMESTAMP("%b-%y", earliest_cr_line)), MONTH) < 0),
         587,
        (DATETIME_DIFF(DATETIME(TIMESTAMP("2017-12-01 00:00:00+00")), DATETIME(PARSE_TIMESTAMP("%b-%y", earliest_cr_line)), MONTH))
    ) AS mths_since_earliest_cr_line,


    -- * * * * * * * * * * * * * * * * * * * * * * * * Discrete Variables Preprocessing * * * * * * * * * * * * * * * * * * * * * * * * ---

    
    -- * * * * * * * * * * * * * * * * * * * * * * * * GRADE AND SUBGRADE * * * * * * * * * * * * * * * * * * * * * * * * ---
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


    CASE sub_grade
        WHEN 'A1' THEN 1
        ELSE 0
    END AS sub_grade_A1,
    CASE sub_grade
        WHEN 'A2' THEN 1
        ELSE 0
    END AS sub_grade_A2,
    CASE sub_grade
        WHEN 'A3' THEN 1
        ELSE 0
    END AS sub_grade_A3,
    CASE sub_grade
        WHEN 'A4' THEN 1
        ELSE 0
    END AS sub_grade_A4,
    CASE sub_grade
        WHEN 'A5' THEN 1
        ELSE 0
    END AS sub_grade_A5,
    CASE sub_grade
        WHEN 'B1' THEN 1
        ELSE 0
    END AS sub_grade_B1,
    CASE sub_grade
        WHEN 'B2' THEN 1
        ELSE 0
    END AS sub_grade_B2,
    CASE sub_grade
        WHEN 'B3' THEN 1
        ELSE 0
    END AS sub_grade_B3,
    CASE sub_grade
        WHEN 'B4' THEN 1
        ELSE 0
    END AS sub_grade_B4,
    CASE sub_grade
        WHEN 'B5' THEN 1
        ELSE 0
    END AS sub_grade_B5,
    CASE sub_grade
        WHEN 'C1' THEN 1
        ELSE 0
    END AS sub_grade_C1,
    CASE sub_grade
        WHEN 'C2' THEN 1
        ELSE 0
    END AS sub_grade_C2,
    CASE sub_grade
        WHEN 'C3' THEN 1
        ELSE 0
    END AS sub_grade_C3,
    CASE sub_grade
        WHEN 'C4' THEN 1
        ELSE 0
    END AS sub_grade_C4,
    CASE sub_grade
        WHEN 'C5' THEN 1
        ELSE 0
    END AS sub_grade_C5,
    CASE sub_grade
        WHEN 'D1' THEN 1
        ELSE 0
    END AS sub_grade_D1,
    CASE sub_grade
        WHEN 'D2' THEN 1
        ELSE 0
    END AS sub_grade_D2,
    CASE sub_grade
        WHEN 'D3' THEN 1
        ELSE 0
    END AS sub_grade_D3,
    CASE sub_grade
        WHEN 'D4' THEN 1
        ELSE 0
    END AS sub_grade_D4,
    CASE sub_grade
        WHEN 'D5' THEN 1
        ELSE 0
    END AS sub_grade_D5,
    CASE sub_grade
        WHEN 'E1' THEN 1
        ELSE 0
    END AS sub_grade_E1,
    CASE sub_grade
        WHEN 'E2' THEN 1
        ELSE 0
    END AS sub_grade_E2,
    CASE sub_grade
        WHEN 'E3' THEN 1
        ELSE 0
    END AS sub_grade_E3,
    CASE sub_grade
        WHEN 'E4' THEN 1
        ELSE 0
    END AS sub_grade_E4,
    CASE sub_grade
        WHEN 'E5' THEN 1
        ELSE 0
    END AS sub_grade_E5,
    CASE sub_grade
        WHEN 'F1' THEN 1
        ELSE 0
    END AS sub_grade_F1,
    CASE sub_grade
        WHEN 'F2' THEN 1
        ELSE 0
    END AS sub_grade_F2,
    CASE sub_grade
        WHEN 'F3' THEN 1
        ELSE 0
    END AS sub_grade_F3,
    CASE sub_grade
        WHEN 'F4' THEN 1
        ELSE 0
    END AS sub_grade_F4,
    CASE sub_grade
        WHEN 'F5' THEN 1
        ELSE 0
    END AS sub_grade_F5,
    CASE sub_grade
        WHEN 'G1' THEN 1
        ELSE 0
    END AS sub_grade_G1,
    CASE sub_grade
        WHEN 'G2' THEN 1
        ELSE 0
    END AS sub_grade_G2,
    CASE sub_grade
        WHEN 'G3' THEN 1
        ELSE 0
    END AS sub_grade_G3,
    CASE sub_grade
        WHEN 'G4' THEN 1
        ELSE 0
    END AS sub_grade_G4,
    CASE sub_grade
        WHEN 'G5' THEN 1
        ELSE 0
    END AS sub_grade_G5,

    -- * * * * * * * * * * * * * * * * * * * * * * * * ADDRESS STATE * * * * * * * * * * * * * * * * * * * * * * * * ---
    CASE addr_state
        WHEN 'CT' THEN 1
        ELSE 0
    END AS addr_state_CT,
    CASE addr_state
        WHEN 'CA' THEN 1
        ELSE 0
    END AS addr_state_CA,
    CASE addr_state
        WHEN 'IL' THEN 1
        ELSE 0
    END AS addr_state_IL,
    CASE addr_state
        WHEN 'WV' THEN 1
        ELSE 0
    END AS addr_state_WV,
    CASE addr_state
        WHEN 'MD' THEN 1
        ELSE 0
    END AS addr_state_MD,
    CASE addr_state
        WHEN 'TX' THEN 1
        ELSE 0
    END AS addr_state_TX,
    CASE addr_state
        WHEN 'NJ' THEN 1
        ELSE 0
    END AS addr_state_NJ,
    CASE addr_state
        WHEN 'NV' THEN 1
        ELSE 0
    END AS addr_state_NV,
    CASE addr_state
        WHEN 'NY' THEN 1
        ELSE 0
    END AS addr_state_NY,
    CASE addr_state
        WHEN 'AR' THEN 1
        ELSE 0
    END AS addr_state_AR,
    CASE addr_state
        WHEN 'RI' THEN 1
        ELSE 0
    END AS addr_state_RI,
    CASE addr_state
        WHEN 'MA' THEN 1
        ELSE 0
    END AS addr_state_MA,
    CASE addr_state
        WHEN 'OH' THEN 1
        ELSE 0
    END AS addr_state_OH,
    CASE addr_state
        WHEN 'FL' THEN 1
        ELSE 0
    END AS addr_state_FL,
    CASE addr_state
        WHEN 'PA' THEN 1
        ELSE 0
    END AS addr_state_PA,
    CASE addr_state
        WHEN 'WI' THEN 1
        ELSE 0
    END AS addr_state_WI,
    CASE addr_state
        WHEN 'VA' THEN 1
        ELSE 0
    END AS addr_state_VA,
    CASE addr_state
        WHEN 'MN' THEN 1
        ELSE 0
    END AS addr_state_MN,
    CASE addr_state
        WHEN 'NC' THEN 1
        ELSE 0
    END AS addr_state_NC,
    CASE addr_state
        WHEN 'MI' THEN 1
        ELSE 0
    END AS addr_state_MI,
    CASE addr_state
        WHEN 'MO' THEN 1
        ELSE 0
    END AS addr_state_MO,
    CASE addr_state
        WHEN 'CO' THEN 1
        ELSE 0
    END AS addr_state_CO,
    CASE addr_state
        WHEN 'GA' THEN 1
        ELSE 0
    END AS addr_state_GA,
    CASE addr_state
        WHEN 'UT' THEN 1
        ELSE 0
    END AS addr_state_UT,
    CASE addr_state
        WHEN 'HI' THEN 1
        ELSE 0
    END AS addr_state_HI,
    CASE addr_state
        WHEN 'AZ' THEN 1
        ELSE 0
    END AS addr_state_AZ,
    CASE addr_state
        WHEN 'LA' THEN 1
        ELSE 0
    END AS addr_state_LA,
    CASE addr_state
        WHEN 'WA' THEN 1
        ELSE 0
    END AS addr_state_WA,
    CASE addr_state
        WHEN 'SD' THEN 1
        ELSE 0
    END AS addr_state_SD,
    CASE addr_state
        WHEN 'KY' THEN 1
        ELSE 0
    END AS addr_state_KY,
    CASE addr_state
        WHEN 'SC' THEN 1
        ELSE 0
    END AS addr_state_SC,
    CASE addr_state
        WHEN 'OK' THEN 1
        ELSE 0
    END AS addr_state_OK,
    CASE addr_state
        WHEN 'AL' THEN 1
        ELSE 0
    END AS addr_state_AL,
    CASE addr_state
        WHEN 'DE' THEN 1
        ELSE 0
    END AS addr_state_DE,
    CASE addr_state
        WHEN 'NM' THEN 1
        ELSE 0
    END AS addr_state_NM,
    CASE addr_state
        WHEN 'KS' THEN 1
        ELSE 0
    END AS addr_state_KS,
    CASE addr_state
        WHEN 'OR' THEN 1
        ELSE 0
    END AS addr_state_OR,
    CASE addr_state
        WHEN 'MT' THEN 1
        ELSE 0
    END AS addr_state_MT,
    CASE addr_state
        WHEN 'NH' THEN 1
        ELSE 0
    END AS addr_state_NH,
    CASE addr_state
        WHEN 'AK' THEN 1
        ELSE 0
    END AS addr_state_AK,
    CASE addr_state
        WHEN 'DC' THEN 1
        ELSE 0
    END AS addr_state_DC,
    CASE addr_state
        WHEN 'IA' THEN 1
        ELSE 0
    END AS addr_state_IA,
    CASE addr_state
        WHEN 'IN' THEN 1
        ELSE 0
    END AS addr_state_IN,
    CASE addr_state
        WHEN 'NE' THEN 1
        ELSE 0
    END AS addr_state_NE,
    CASE addr_state
        WHEN 'VT' THEN 1
        ELSE 0
    END AS addr_state_VT,
    CASE addr_state
        WHEN 'TN' THEN 1
        ELSE 0
    END AS addr_state_TN,
    CASE addr_state
        WHEN 'WY' THEN 1
        ELSE 0
    END AS addr_state_WY,
    CASE addr_state
        WHEN 'MS' THEN 1
        ELSE 0
    END AS addr_state_MS,
    CASE addr_state
        WHEN 'ID' THEN 1
        ELSE 0
    END AS addr_state_ID,
    CASE addr_state
        WHEN 'ME' THEN 1
        ELSE 0
    END AS addr_state_ME,

    -- * * * * * * * * * * * * * * * * * * * * * * * * HOME OWNERSHIP * * * * * * * * * * * * * * * * * * * * * * * * ---
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


    -- * * * * * * * * * * * * * * * * * * * * * * * * INITIAL LIST STATUS * * * * * * * * * * * * * * * * * * * * * * * * ---
    CASE initial_list_status
        WHEN 'f' THEN 1
        ELSE 0
    END AS initial_list_status_f,
    CASE initial_list_status
        WHEN 'w' THEN 1
        ELSE 0
    END AS initial_list_status_w,

    -- * * * * * * * * * * * * * * * * * * * * * * * * PURPOSE * * * * * * * * * * * * * * * * * * * * * * * * ---
    CASE purpose
        WHEN 'major_purchase' THEN 1
        ELSE 0
    END AS purpose_major_purchase,
    CASE purpose
        WHEN 'debt_consolidation' THEN 1
        ELSE 0
    END AS purpose_debt_consolidation,
    CASE purpose
        WHEN 'car' THEN 1
        ELSE 0
    END AS purpose_car,
    CASE purpose
        WHEN 'small_business' THEN 1
        ELSE 0
    END AS purpose_small_business,
    CASE purpose
        WHEN 'credit_card' THEN 1
        ELSE 0
    END AS purpose_credit_card,
    CASE purpose
        WHEN 'other' THEN 1
        ELSE 0
    END AS purpose_other,
    CASE purpose
        WHEN 'home_improvement' THEN 1
        ELSE 0
    END AS purpose_home_improvement,
    CASE purpose
        WHEN 'renewable_energy' THEN 1
        ELSE 0
    END AS purpose_renewable_energy,
    CASE purpose
        WHEN 'medical' THEN 1
        ELSE 0
    END AS purpose_medical,
    CASE purpose
        WHEN 'vacation' THEN 1
        ELSE 0
    END AS purpose_vacation,
    CASE purpose
        WHEN 'moving' THEN 1
        ELSE 0
    END AS purpose_moving,
    CASE purpose
        WHEN 'house' THEN 1
        ELSE 0
    END AS purpose_house,
    CASE purpose
        WHEN 'wedding' THEN 1
        ELSE 0
    END AS purpose_wedding,
    CASE purpose
        WHEN 'educational' THEN 1
        ELSE 0
    END AS purpose_educational,



    -- * * * * * * * * * * * * * * * * * * * * * * * * VERIFICATION STATUS * * * * * * * * * * * * * * * * * * * * * * * * ---
    CASE verification_status
        WHEN 'Not Verified' THEN 1
        ELSE 0
    END AS `verification_status_Not_Verified`,
    CASE verification_status
        WHEN 'Source Verified' THEN 1
        ELSE 0
    END AS `verification_status_Source_Verified`,
    CASE verification_status
        WHEN 'Verified' THEN 1
        ELSE 0
    END AS `verification_status_Verified`,



    -- * * * * * * * * * * * * * * * * * * * * * * * * MISSING VALUES PREPROCESSING * * * * * * * * * * * * * * * * * * * * * * * * ---
    IFNULL(total_rev_hi_lim, funded_amnt) AS total_rev_hi_lim_cl,
    CAST(IFNULL(annual_inc, (SELECT AVG(annual_inc) FROM `data-science-325423.lending_club.data_from_2007_2014`)) AS INT64) as annual_inc_cl,
    IFNULL(acc_now_delinq, 0) AS acc_now_delinq_cl,
    IFNULL(total_acc, 0) AS total_acc_cl,
    IFNULL(pub_rec, 0) AS pub_rec_cl,
    IFNULL(open_acc, 0) AS open_acc_cl,
    IFNULL(inq_last_6mths, 0) AS inq_last_6mths_cl,
    IFNULL(delinq_2yrs, 0) AS delinq_2yrs,
    

FROM 
    `data-science-325423.lending_club.data_from_2007_2014`

)
