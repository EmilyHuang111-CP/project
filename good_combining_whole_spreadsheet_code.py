import pandas as pd

excel_file1 = "/Users/emilyhuang/Desktop/combined data/facility.xlsx"
df1 = pd.read_excel(excel_file1).sort_values(by="id")  # Read Excel file into a DataFrame
df1.columns = df1.columns.str.strip()  # Strip leading and trailing whitespace from column names

excel_file2 = "/Users/emilyhuang/Desktop/combined data/institution.xlsx"
df2 = pd.read_excel(excel_file2)  # Read Excel file into a DataFrame
df2.columns = df2.columns.str.strip()  # Strip leading and trailing whitespace from column names

excel_file3 = "/Users/emilyhuang/Desktop/combined data/tempo_report.xlsx"
df3 = pd.read_excel(excel_file3).sort_values(by="facility_id")   # Read Excel file into a DataFrame
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
column2_df1 = df1["facility_name"]


valid_facility_ids = set(df1['id'])

df3_cleaned = df3[df3['facility_id'].isin(valid_facility_ids)].reset_index(drop=True)
df4_cleaned = df4[df4['facility_id'].isin(valid_facility_ids)].reset_index(drop=True)
combined_df = pd.concat([df3_cleaned, df4_cleaned], axis=0)

output_excel_file_combined = "/Users/emilyhuang/Desktop/combined data/combined_data28.xlsx"
combined_df.to_excel(output_excel_file_combined, index=False)


no_report_messages = []
for index, row in df1.iterrows():
    facility_id = row['id']
    if facility_id not in combined_df['facility_id'].values:
        no_report_messages.append(facility_id)
if no_report_messages:
    appended_df = pd.DataFrame({'facility_id': no_report_messages})
    combined_df_extended = pd.concat([combined_df, appended_df], ignore_index=True)
else:
    combined_df_extended = combined_df.copy()
matched_institution_ids = []
needed_columns = combined_df_extended.iloc[:, [1, 2]].copy()
for index, row in combined_df_extended.iterrows():
    facility_id = row["facility_id"]
    if facility_id in df1['id'].values:
        institution_id = df1.loc[df1['id'] == facility_id, 'institution_id'].values[0]
    else:
        institution_id = "No institution id available"
    matched_institution_ids.append(institution_id)


needed_columns['facility_id'] = needed_columns['facility_id'].astype(str)


# Add matched institution names to df1 as a new column
needed_columns['institution_id'] = matched_institution_ids

matched_facility_names = []
for index, row in combined_df_extended.iterrows():
    facility_id = row["facility_id"]
    if facility_id in df1['id'].values:
        facility_name = df1.loc[df1['id'] == facility_id, 'facility_name'].values[0]
    else:
        facility_name = "No facility name available"
    matched_facility_names.append(facility_name)

needed_columns['facility_name'] = matched_facility_names

matched_institution_names = []


for index, row in combined_df_extended.iterrows():
    institution_id = row["institution_id"]
    if institution_id in df2['id'].values:
        institution_name = df2.loc[df2['id'] == institution_id, 'institution_name'].values[0]
    else:
        institution_name = "No institution name available"
    matched_institution_names.append(institution_name)

needed_columns['institution_name'] = matched_institution_names

matched_cron_expression = []
for index, row in combined_df_extended.iterrows():
    facility_id = row['facility_id']

    if facility_id in df4_cleaned['facility_id'].values:
        # Retrieve corresponding rr_rule
        corresponding_cron_expression = df4_cleaned.loc[df4_cleaned['facility_id'] == facility_id, 'cron_expression'].values[0]
        matched_cron_expression.append(corresponding_cron_expression)
    else:
        matched_cron_expression.append("No corresponding cron expression found")

needed_columns['cron_expression'] = matched_cron_expression

matched_rr_rule = []
for index, row in combined_df_extended.iterrows():
    facility_id = row['facility_id']

    if facility_id in df3_cleaned['facility_id'].values:
        # Retrieve corresponding rr_rule
        corresponding_rr_rule = df3_cleaned.loc[df3_cleaned['facility_id'] == facility_id, 'rr_rule'].values[0]
        matched_rr_rule.append(corresponding_rr_rule)
    else:
        matched_rr_rule.append("No corresponding rrule found")

needed_columns['rrule'] = matched_rr_rule


matched_start_date = []
for index, row in combined_df_extended.iterrows():
    facility_id = row['facility_id']

    if facility_id in df3_cleaned['facility_id'].values:
        # Retrieve corresponding rr_rule
        corresponding_start_date = df3_cleaned.loc[df3_cleaned['facility_id'] == facility_id, 'start_date'].values[0]
        matched_start_date.append(corresponding_start_date)
    else:
        matched_start_date.append("No corresponding start date found")

needed_columns['start_date'] = matched_start_date


matched_report_name = []
for index, row in combined_df_extended.iterrows():
    facility_id = row['facility_id']

    if facility_id in df3_cleaned['facility_id'].values:
        # Retrieve corresponding rr_rule
        corresponding_report_name = df3_cleaned.loc[df3_cleaned['facility_id'] == facility_id, 'report_name'].values[0]
        matched_report_name.append(corresponding_report_name)
    else:
        matched_report_name.append("No corresponding report name found")

needed_columns['report_name'] = matched_report_name


needed_columns.sort_values(by='facility_id', inplace=True)
needed_columns.to_excel(output_excel_file_combined, index=False)


matched_recurrence = []
for index, row in combined_df_extended.iterrows():
    facility_id = row['facility_id']

    if facility_id in df4_cleaned['facility_id'].values:
        corresponding_recurrence = df4_cleaned.loc[df4_cleaned['facility_id'] == facility_id, 'recurrence'].values[0]
        matched_recurrence.append(corresponding_recurrence)
    else:
        matched_recurrence.append("No corresponding recurrence found")

needed_columns['recurrence'] = matched_recurrence
needed_columns['recurrence'] = needed_columns['recurrence'].astype(str)
needed_columns.sort_values(by='recurrence', inplace=True)
needed_columns = needed_columns[needed_columns['recurrence'] != '0']
needed_columns.to_excel(output_excel_file_combined, index=False)

