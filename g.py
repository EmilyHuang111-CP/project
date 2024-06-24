import pandas as pd
import rrule_decrypt as rr_d
import plotly.express as px
import plotly.subplots as sp
import io


def finding_rows_facility_id(keyword):
    fac_num = keyword
    full_list = pd.read_csv("full_list.csv")

    if fac_num != "all":
        mask = full_list['facility_id'].isin([int(fac_num)])

        masked_df = full_list[mask]

        # print(masked_df)
        final_df = using_fac_id_rrule_indiv(masked_df)
        return True, final_df
    final_df = all_fac_id_rrule(full_list)
    return False, final_df


def comparing_alerts(df):
    alert_list = list(df['report_file_name'])

    combined_alerts = pd.read_csv("report_names.csv")

    valid_alerts = []

    if alert_list:
        for i in range(len(alert_list)):
            alert_str = str(alert_list[i]).strip().replace(".pdf", "").title().replace("_", " ")
            if (combined_alerts == alert_str).any().any():
                valid_alerts.append(alert_str)
        return valid_alerts
    return None


def check_valid_ind(df):
    valid_inds = []

    for i in df:
        if not pd.isnull(i):
            valid_inds.append(df.index(i))
    return valid_inds


def using_fac_id_rrule_indiv(df):
    rrule_list = list(df['rr_rule'])
    rrule_starts = list(df['start_date'])

    valid_reports = comparing_alerts(df)
    # valid_reports = list(df['report_file_name'])

    # rrule_valid_inds = check_valid_ind(rrule_list)

    inds = []

    for i in rrule_list:
        # print(i)
        if pd.isnull(i):
            inds.append(rrule_list.index(i))
    # print(inds)

    for i in inds:
        rrule_list.pop(i)
        rrule_starts.pop(i)

    # idk whats going on here but theres an issue
    if rrule_list != [] and valid_reports != []:
        rrule_occurrences = {}
        # print(rrule_list)
        # print(valid_reports)

        for i in range(len(rrule_list)):
            rrule_occurrences.update({valid_reports[i]: 0})
        #
        # print("f", rrule_occurrences)

        for i in rrule_list:
            # print(len(rrule_list) + 1)
            # print(i)
            rrule_start_entry = rrule_starts[rrule_list.index(i)]
            # print("i", rrule_list.index(i))
            # print("v", valid_reports)
            # print("f", rrule_list)
            # print("d", rrule_occurrences)
            # print("s", rrule_starts)
            rrule_occurrences[valid_reports[rrule_list.index(i)]] += rr_d.get_occurrences(i, rrule_start_entry)

        rrule_df = pd.DataFrame(
            {"Reports": list(rrule_occurrences.keys()), "Occurrences": list(rrule_occurrences.values())})
    else:
        rrule_df = pd.DataFrame(
            {"Reports": [], "Occurrences": []})
    return rrule_df


def all_fac_id_rrule(df):
    facility_ids = []

    for i in df["facility_id"]:
        facility_ids.append(i)

    # valid_reports = comparing_alerts(df)
    combined_alerts = pd.read_csv("report_names.csv")
    combined_alerts = combined_alerts["Alert Reports!!"].tolist()
    rrule_df = {"Reports": combined_alerts}
    # print(combined_alerts)

    for i in facility_ids:
        rrule_df.update({i: []})
        for j in combined_alerts:
            rrule_df[i].append(0)

    for i in facility_ids:
        mask = df['facility_id'].isin([int(i)])
        masked_df = df[mask]
        valid_reports = comparing_alerts(masked_df)
        # print(valid_reports)
        for j in valid_reports:
            # print(j)
            rep_ind = combined_alerts.index(j)
            # print(rep_ind)
            rp_lst = rrule_df[i]
            rp_lst[rep_ind] += 1

    # print(rrule_df)
    final = pd.DataFrame(rrule_df)
    # print(final)
    return final


def init(keyword):
    indiv, rrule_df = finding_rows_facility_id(keyword)

    if indiv:
        final_fig = px.bar(rrule_df, x="Reports", y="Occurrences", color="Reports", barmode="group")
    else:
        rrule_df = rrule_df.melt(id_vars='Reports', var_name='Facilities', value_name='Occurrences')
        skip = 0
        interval = 6
        final_fig = sp.make_subplots(rows=interval, cols=1)
        for i in range(6):
            fig1 = px.bar(rrule_df[skip::interval], x="Reports", y="Occurrences", color="Facilities", barmode="group")
            skip += 1

            fig1_trace = []

            for trace in range(len(fig1["data"])):
                fig1_trace.append(fig1["data"][trace])

            for traces in fig1_trace:
                final_fig.add_trace(traces, row=skip, col=1)

        final_fig.update_traces(width=0.05)
        final_fig.update_layout(height=3600, width=2400, title_text="Total Facility With Occurrences", showlegend=False)
    # final_fig.show()

    img_buf = io.BytesIO()
    final_fig.write_image(img_buf, format='png')
    img_buf.seek(0)
    return img_buf


init("66")
