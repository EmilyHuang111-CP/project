#import necessary packages
import pandas as pd

#find the path of the excel file from desktop
excel_file = "/Users/emilyhuang/Desktop/combined data/combined everything.xlsx"
#read the the excel file
df = pd.read_excel(excel_file)

#get rid of whitespace from column names
df.columns = df.columns.str.strip()

#accessing columns
column1_data = df["facility_id"]
column2_data = df["facility_name"]
column3_data = df["institution_id"]
column4_data = df["institution_name"]

#asks for user facility ID input
user_facility_id = int(input("Enter Facility ID: "))

#define the match function
def match_info(facility_id):
    filtered_df = df[df['facility_id'] == facility_id]
    return filtered_df

#call the match function and output the facility_name, institution_id, and institution_name based on the facility_id
matched = match_info(user_facility_id)
print(matched)

