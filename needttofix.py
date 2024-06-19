import pandas as pd

excel_file = "/Users/emilyhuang/Desktop/combined data/combined everything.xlsx"
df = pd.read_excel(excel_file)
df.columns = df.columns.str.strip()
column1_data = df["facility_id"]
column5_data = df["rr_rule"]
column6_data = df["start_date"]



facility_id = int(input("Facility ID: "))

def match_rrule(facility_id):
    filtered_df = df[df['facility_id'] == facility_id]
    rr_rule = filtered_df.iloc[:, -2:-1].values[0]

    return rr_rule

def match_start_date(facility_id):
    filtered_df = df[df['facility_id'] == facility_id]
    start_date = filtered_df.iloc[:, -1:].values[0]

    return start_date


matched_rrule = match_rrule(facility_id)
print(matched_rrule)

matched_start_date = match_start_date(facility_id)
print(matched_start_date)

"""result=df.loc[df['facility_id'] == facility_id,'rr_rule'].values[0]
print(result)"""




















