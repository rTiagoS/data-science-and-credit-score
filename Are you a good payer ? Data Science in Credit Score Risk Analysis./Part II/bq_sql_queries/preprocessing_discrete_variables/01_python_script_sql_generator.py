# Part I) SQL Script to display unique values for each column considered.
columns = "grade sub_grade home_ownership verification_status loan_status purpose addr_state initial_list_status".split()


sql_script = []

for col in columns:
    sql_script.append(f'SELECT \'{col}\' AS variable, FORMAT(\"%T\", ARRAY_AGG({col})) AS dummies_categories FROM (SELECT DISTINCT {col} AS {col}, FROM `data-science-325423.lending_club.data_from_2007_2014`) UNION ALL ')


f = open("unique_values_per_column.txt", "w+")
for line in sql_script:
    f.write(line)
f.close()



