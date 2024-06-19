import pandas as pd

# Load the Excel file
excel_file_facility = "/Users/emilyhuang/Desktop/combined data/combined everything.xlsx"
excel_file_combined_everything = "/Users/emilyhuang/Desktop/combined data/combined everything.xlsx"

df = pd.read_excel(excel_file_facility)
df2 = pd.read_excel(excel_file_combined_everything)

# Strip any leading/trailing whitespace from the column names
df.columns = df.columns.str.strip()

# Prompt the user for a facility id
facility_id = int(input("Facility id: "))

def match_facility_name(facility_id):
    # Filter the dataframe to find the matching facility id
    filtered_df = df[df['facility_id'] == facility_id]

    # Check if any matching rows are found
    if not filtered_df.empty:
        # Extract the facility name
        facility_name = filtered_df['facility_name'].values[0]
        return facility_name
    else:
        return "Facility ID not found."


facility_name = match_facility_name(facility_id)


results = []

# Loop through all the values in the facility_id column
for id in df['facility_id']:
    # Find the matching facility name
    facility_name = match_facility_name(id)
    # Append the result to the list
    results.append({'facility_id': id, 'facility_name': facility_name})

# Convert the list of dictionaries to a DataFrame
result_df = pd.DataFrame(results)

# Save the new DataFrame to a new Excel file
output_file_path = "/Users/emilyhuang/Desktop/combined data/matched_facilities.xlsx"
result_df.to_excel(output_file_path, index=False)
