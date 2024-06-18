# Combines facility and institution csvs into one dataframe called active sites and returns the table sorted by institution id
def combined_active_facilities():
    facility = pd.read_csv("facility.csv")

    active_facilities = facility[["id", "facility_name", "institution_id"]].rename(columns={"id": "facility_id"})

    inst_table = pd.read_csv("institution.csv")

    inst_spliced = inst_table[["id", "institution_name"]].rename(columns={"id": "institution_id"})
    active_sites = pd.merge(active_facilities, inst_spliced, how='left')

    sorted_tab = active_sites.sort_values("institution_id")
    return sorted_tab


# Writes the active sites dataframe to a csv file
def combined_to_file():
    sorted_t = combined_active_facilities()
    sorted_t.to_csv("active_sites.csv", sep=',', index=False, encoding='utf-8')


# Gets a list of the active site ids and returns them
def active_facility_id():
    sorted_t = combined_active_facilities()

    id_list = sorted_t['facility_id'].to_string(index=False).split("\n")

    for x in id_list:
        id_list[id_list.index(x)] = x.strip().title()

    return id_list
