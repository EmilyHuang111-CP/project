import pandas as pd

excel_file1 = "/Users/emilyhuang/Desktop/combined data/facility.xlsx"
df1 = pd.read_excel(excel_file1)  # Read Excel file into a DataFrame
df1.columns = df1.columns.str.strip()  # Strip leading and trailing whitespace from column names

excel_file2 = "/Users/emilyhuang/Desktop/combined data/institution.xlsx"
df2 = pd.read_excel(excel_file2)  # Read Excel file into a DataFrame
df2.columns = df2.columns.str.strip()  # Strip leading and trailing whitespace from column names

excel_file3 = "/Users/emilyhuang/Desktop/combined data/tempo_report.xlsx"
df3 = pd.read_excel(excel_file3)  # Read Excel file into a DataFrame
df3.columns = df3.columns.str.strip()  # Strip leading and trailing whitespace from column names

excel_file4 = "/Users/emilyhuang/Desktop/combined data/scheduler_job.xlsx"
df4 = pd.read_excel(excel_file4)  # Read Excel file into a DataFrame
df4.columns = df4.columns.str.strip()  # Strip leading and trailing whitespace from column names

column1_data = df2["id"]
column2_data = df2["institution_name"]
column13_data = df3["rr_rule"]
column14_data = df3["start_date"]
column21_data = df3["report_name"]
column2_data_df3 = df3["facility_id"]
column_16_df4 = df4["cron_expression"]


output_excel_file = "/Users/emilyhuang/Desktop/combined data/14.xlsx"

matched_institution_names = []
first_three_columns = df1.iloc[:, :3]
for index, row in df1.iterrows():
    institution_id = row["institution_id"]
    if institution_id in df2['id'].values:
        institution_name = df2.loc[df2['id'] == institution_id, 'institution_name'].values[0]
    else:
        institution_name = "No institution name available"
    matched_institution_names.append(institution_name)

# Add matched institution names to df1 as a new column
first_three_columns['institution_name'] = matched_institution_names


matched_rrules = []

for index, row in df1.iterrows():
    facility_id = row['id']

    # Check if facility_id exists in df3
    if facility_id in df3['facility_id'].values:
        # Retrieve corresponding rr_rule
        corresponding_rrule = df3.loc[df3['facility_id'] == facility_id, 'rr_rule'].values[0]
        matched_rrules.append(corresponding_rrule)
    else:
        matched_rrules.append("No corresponding rrule found")

first_three_columns['rrule'] = matched_rrules
first_three_columns.to_excel(output_excel_file, index=False)

matched_start_date = []

for index, row in df1.iterrows():
    facility_id = row['id']

    # Check if facility_id exists in df3
    if facility_id in df3['facility_id'].values:
        # Retrieve corresponding rr_rule
        corresponding_start_date = df3.loc[df3['facility_id'] == facility_id, 'start_date'].values[0]
        matched_start_date.append(corresponding_start_date)
    else:
        matched_start_date.append("No corresponding start date found")


first_three_columns['start_date'] = matched_start_date
first_three_columns.to_excel(output_excel_file, index=False)


matched_report_name = []
for index, row in df1.iterrows():
    facility_id = row['id']

    # Check if facility_id exists in df3
    if facility_id in df3['facility_id'].values:
        # Retrieve corresponding rr_rule
        corresponding_report_name = df3.loc[df3['facility_id'] == facility_id, 'report_name'].values[0]
        matched_report_name.append(corresponding_report_name)
    else:
        matched_report_name.append("No corresponding report name found")

first_three_columns['report-name'] = matched_report_name
first_three_columns.to_excel(output_excel_file, index=False)


matched_cron_expression = []
for index, row in df1.iterrows():
    facility_id = row['id']

    # Check if facility_id exists in df3
    if facility_id in df4['facility_id'].values:
        # Retrieve corresponding rr_rule
        corresponding_cron_expression = df4.loc[df4['facility_id'] == facility_id, 'cron_expression'].values[0]
        matched_cron_expression.append(corresponding_cron_expression)
    else:
        matched_cron_expression.append("No corresponding cron expression found")

first_three_columns['cron_expression'] = matched_cron_expression
first_three_columns.to_excel(output_excel_file, index=False)
