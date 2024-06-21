import pandas as pd
import rrule_decrypt as rr_d
from dash import Dash, html, dcc
import plotly.express as px
import plotly.subplots as sp


def finding_rows_facility_id():
    # fac_num = (input("input num: "))
    fac_num = 'all'
    full_list = pd.read_csv("full_list.csv")

    if fac_num != "all":
        mask = full_list['facility_id'].isin([int(fac_num)])

        masked_df = full_list[mask]

        print(masked_df)
        final_df = using_fac_id_rrule_indiv(masked_df)
        return True, final_df
    final_df = all_fac_id_rrule(full_list)
    return False, final_df


def comparing_alerts(df):
    alert_list = list(df['report_file_name'])

    combined_alerts = pd.read_csv("report_names.csv")

    valid_alerts = []

    for i in range(len(alert_list)):
        alert_str = str(alert_list[i]).replace("_", " ").title().strip()
        if (combined_alerts == alert_str).any().any():
            valid_alerts.append(alert_str)
    return valid_alerts


def using_fac_id_rrule_indiv(df):
    # check the alert list name with stuff from this combine alerts thing
    # easy peasey!

    rrule_list = list(df['rr_rule'])
    rrule_starts = list(df['start_date'])

    # valid = 0

    valid_reports = comparing_alerts(df)

    rrule_valid_inds = []

    for i in rrule_list:
        if not pd.isnull(i):
            # valid += 1
            rrule_valid_inds.append(rrule_list.index(i))
    rrule_occurrences = {}

    for i in rrule_valid_inds:
        rrule_occurrences.update({valid_reports[i]: 0})

    for i in rrule_valid_inds:
        rrule_start_entry = rrule_starts[i]
        rrule_occurrences[valid_reports[i]] += rr_d.get_occurrences(rrule_list[i], rrule_start_entry)

    # print("v", valid)
    print("f", rrule_occurrences)

    rrule_df = pd.DataFrame({"alert_names": list(rrule_occurrences.keys()), "Occurrences": list(rrule_occurrences.values())})
    # rrule_df = pd.DataFrame([rrule_occurrences])
    # print(rrule_df)
    return rrule_df


def all_fac_id_rrule(df):
    facility_ids = []

    for i in df["facility_id"]:
        facility_ids.append(i)

    # valid_reports = comparing_alerts(df)
    combined_alerts = pd.read_csv("report_names.csv")
    # print(combined_alerts)
    combined_alerts = combined_alerts["Alert Reports!!"].tolist()
    rrule_df = {"alert_names": combined_alerts}

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
    print(final)
    return final


indiv, rrule_df = finding_rows_facility_id()

app = Dash(__name__)

if indiv:
    print("indiv")
    pass
else:
    print("no indiv")
    rrule_df = rrule_df.melt(id_vars='alert_names', var_name='Facilities', value_name='Occurrences')

skip = 0
interval = 6
final_fig = sp.make_subplots(rows=interval, cols=1)
for i in range(6):
    fig1 = px.bar(rrule_df[skip::interval], x="alert_names", y="Occurrences", color="Facilities", barmode="group")
    skip += 1

    fig1_trace = []

    for trace in range(len(fig1["data"])):
        fig1_trace.append(fig1["data"][trace])

    for traces in fig1_trace:
        final_fig.add_trace(traces, row=skip, col=1)

final_fig.update_traces(width=0.05)
final_fig.update_layout(height=3600, width=2400, title_text="Total Facility With Occurrences", showlegend=False)


app.layout = html.Div(children=[
    dcc.Graph(
        id='rrule_graph',
        figure=final_fig
    )
])

if __name__ == '__main__':
    app.run(debug=True, port=8050)
