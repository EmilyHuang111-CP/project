import pandas as pd

# Load the Excel file
excel_file = "/Users/emilyhuang/Desktop/combined data/combined everything.xlsx"
df = pd.read_excel(excel_file)  # Read Excel file into a DataFrame
df.columns = df.columns.str.strip()  # Strip leading and trailing whitespace from column names


# Function to find duplicates for a specific facility_id
def finding_duplicates(facility_id):
    # Group by 'facility_id' and filter groups where the size is greater than 1 (i.e., duplicates)
    duplicates = df.groupby('facility_id').filter(lambda x: len(x) > 1)

    # Filter the duplicates for the specific user input facility ID
    specific_duplicates = duplicates[duplicates['facility_id'] == facility_id]

    return specific_duplicates


# Function to match rr_rule for a specific facility_id
def match_rrule(facility_id):
    filtered_df = df[df['facility_id'] == facility_id]  # Filter DataFrame for specific facility_id
    rr_rule = filtered_df.iloc[0, df.columns.get_loc('rr_rule')]  # Get rr_rule value for the first occurrence

    return rr_rule


# Function to match start_date for a specific facility_id
def match_start_date(facility_id):
    filtered_df = df[df['facility_id'] == facility_id]  # Filter DataFrame for specific facility_id
    start_date = filtered_df.iloc[0, df.columns.get_loc('start_date')]  # Get start_date value for the first occurrence

    return start_date


# Function to match report_name for a specific facility_id
def match_report_name(facility_id):
    filtered_df = df[df['facility_id'] == facility_id]  # Filter DataFrame for specific facility_id
    report_name = filtered_df.iloc[
        0, df.columns.get_loc('report_name')]  # Get report_name value for the first occurrence

    return report_name


# Get user input for the facility ID
facility_id = int(input("Facility ID: "))

# Find all duplicates for the user input facility_id
all_duplicates = finding_duplicates(facility_id)

# Initialize a list to store results
results = []

# Iterate through each duplicate and collect corresponding values
for index, row in all_duplicates.iterrows():
    rr_rule = match_rrule(row['facility_id'])  # Match rr_rule for current facility_id
    start_date = match_start_date(row['facility_id'])  # Match start_date for current facility_id
    report_name = match_report_name(row['facility_id'])  # Match report_name for current facility_id

    # Append a list containing facility_id, rr_rule, start_date, report_name to results
    results.append([row['facility_id'], rr_rule, start_date, report_name])

# Print the results list
for result in results:
    print(result)
