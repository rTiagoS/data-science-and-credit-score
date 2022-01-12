# Part II) SQL script to transform unique values into dummies categories.

# unique values for each column considered.
addr_state	        = ["CT", "CA", "IL", "WV", "MD", "TX", "NJ", "NV", "NY", "AR", "RI", "MA", "OH", "FL", "PA", "WI", "VA", "MN", "NC", "MI", "MO", "CO", "GA", "UT", "HI", "AZ", "LA", "WA", "SD", "KY", "SC", "OK", "AL", "DE", "NM", "KS", "OR", "MT", "NH", "AK", "DC", "IA", "IN", "NE", "VT", "TN", "WY", "MS", "ID", "ME"]			
initial_list_status	= ["f", "w"]			
grade	            = ["A", "B", "C", "D", "E", "F", "G"]			
loan_status	        = ["Fully Paid", "Charged Off", "Does not meet the credit policy. Status:Fully Paid", "Current", "Late (31-120 days)", "In Grace Period", "Does not meet the credit policy. Status:Charged Off", "Late (16-30 days)", "Default"]			
purpose	            = ["major_purchase", "debt_consolidation", "car", "small_business", "credit_card", "other", "home_improvement", "renewable_energy", "medical", "vacation", "moving", "house", "wedding", "educational"]			
sub_grade	        = ["A1", "A2", "A3", "A4", "A5", "B1", "B2", "B3", "B4", "B5", "C1", "C2", "C3", "C4", "C5", "D1", "D2", "D3", "D4", "D5", "E1", "E2", "E3", "E4", "E5", "F1", "F2", "F3", "F4", "F5", "G1", "G2", "G3", "G4", "G5"]			
verification_status	= ["Not Verified", "Source Verified", "Verified"]			
home_ownership	    = ["MORTGAGE", "RENT", "OWN", "OTHER", "NONE", "ANY"]					


variables = dict({'addr_state' : addr_state, 
                  'initial_list_status' : initial_list_status,
                  'grade' : grade,
                  'loan_status' : loan_status,
                  'purpose' : purpose,
                  'sub_grade' : sub_grade,
                  'verification_status' : verification_status,
                  'home_ownership' : home_ownership})


for var, _ in variables.items():

    # main step for sql script generator
    sql_script = []

    for cat in variables[var]:
        sql_script.append(f'CASE {var}\n\tWHEN \'{cat}\' THEN 1\n\tELSE 0\nEND AS `{var}_{cat}`,\n')

    # Save 
    f = open(f"{var}_sql.txt", "w+")
    for line in sql_script:
        f.write(line)
    f.close()
