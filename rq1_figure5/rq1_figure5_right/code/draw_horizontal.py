import json
import matplotlib.pylab as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

jsonfile  = '''{
    "params": {
        "repoId": "207181317"
    },
    "requestedAt": "2024-01-10T08:09:41.266+00:00",
    "finishedAt": "2024-01-10T08:09:41.288+00:00",
    "spent": 0.022,
    "sql": "123",
    "fields": [
        {
            "name": "event_month",
            "columnType": 253
        },
        {
            "name": "p0",
            "columnType": 246
        },
        {
            "name": "p25",
            "columnType": 246
        },
        {
            "name": "p50",
            "columnType": 246
        },
        {
            "name": "p75",
            "columnType": 246
        },
        {
            "name": "p100",
            "columnType": 246
        }
    ],
    "data": [
        {
            "event_month": "2020-09-01",
            "p0": 0.00222222,
            "p25": 0.00222222,
            "p50": 1.41888889,
            "p75": 146.83416667,
            "p100": 176.67694444
        },
        {
            "event_month": "2020-10-01",
            "p0": 5.66777778,
            "p25": 5.66777778,
            "p50": 13.70833333,
            "p75": 13.70833333,
            "p100": 26.18111111
        },
        {
            "event_month": "2020-11-01",
            "p0": 0.07972222,
            "p25": 0.16138889,
            "p50": 1.39055556,
            "p75": 10.25166667,
            "p100": 1668.51916667
        },
        {
            "event_month": "2020-12-01",
            "p0": 0.02083333,
            "p25": 0.14027778,
            "p50": 0.44638889,
            "p75": 5.91444444,
            "p100": 47.61694444
        },
        {
            "event_month": "2021-01-01",
            "p0": 0.5075,
            "p25": 2.24916667,
            "p50": 8.71777778,
            "p75": 39.87555556,
            "p100": 3000.24638889
        },
        {
            "event_month": "2021-02-01",
            "p0": 0.20944444,
            "p25": 2.02138889,
            "p50": 7.56138889,
            "p75": 9.26833333,
            "p100": 317.82277778
        },
        {
            "event_month": "2021-03-01",
            "p0": 0.03027778,
            "p25": 0.29166667,
            "p50": 1.535,
            "p75": 72.71694444,
            "p100": 4030.15583333
        },
        {
            "event_month": "2021-04-01",
            "p0": 0.08416667,
            "p25": 0.41,
            "p50": 4.47277778,
            "p75": 38.32027778,
            "p100": 657.4775
        },
        {
            "event_month": "2021-05-01",
            "p0": 0.04527778,
            "p25": 1.05166667,
            "p50": 6.36805556,
            "p75": 93.96777778,
            "p100": 274.18222222
        },
        {
            "event_month": "2021-06-01",
            "p0": 0.0025,
            "p25": 1.77972222,
            "p50": 10.12972222,
            "p75": 37.43638889,
            "p100": 387.40361111
        },
        {
            "event_month": "2021-07-01",
            "p0": 0.03333333,
            "p25": 0.39027778,
            "p50": 0.8725,
            "p75": 48.99277778,
            "p100": 1966.81916667
        },
        {
            "event_month": "2021-08-01",
            "p0": 1.24972222,
            "p25": 4.16916667,
            "p50": 20.63833333,
            "p75": 682.09111111,
            "p100": 913.93805556
        },
        {
            "event_month": "2021-09-01",
            "p0": 0.00472222,
            "p25": 0.02833333,
            "p50": 0.53055556,
            "p75": 15.91861111,
            "p100": 29.91972222
        },
        {
            "event_month": "2021-10-01",
            "p0": 0.00416667,
            "p25": 0.37333333,
            "p50": 1.19805556,
            "p75": 54.2825,
            "p100": 1227.34527778
        },
        {
            "event_month": "2021-11-01",
            "p0": 0.35472222,
            "p25": 0.59166667,
            "p50": 5.26972222,
            "p75": 85.05972222,
            "p100": 2995.39833333
        },
        {
            "event_month": "2021-12-01",
            "p0": 0.30694444,
            "p25": 0.44888889,
            "p50": 0.62666667,
            "p75": 2.13638889,
            "p100": 56.31055556
        },
        {
            "event_month": "2022-01-01",
            "p0": 0.15055556,
            "p25": 0.5475,
            "p50": 1.80333333,
            "p75": 24.60444444,
            "p100": 838.665
        },
        {
            "event_month": "2022-02-01",
            "p0": 0.37805556,
            "p25": 0.50166667,
            "p50": 0.92944444,
            "p75": 26.49916667,
            "p100": 5877.16555556
        },
        {
            "event_month": "2022-03-01",
            "p0": 0.40138889,
            "p25": 0.83916667,
            "p50": 10.33111111,
            "p75": 141.59611111,
            "p100": 7619.47416667
        },
        {
            "event_month": "2022-04-01",
            "p0": 0.44944444,
            "p25": 0.64361111,
            "p50": 8.85611111,
            "p75": 157.75777778,
            "p100": 460.45305556
        },
        {
            "event_month": "2022-05-01",
            "p0": 0.0975,
            "p25": 0.49861111,
            "p50": 3.33972222,
            "p75": 48.47694444,
            "p100": 2039.28972222
        },
        {
            "event_month": "2022-06-01",
            "p0": 0.52444444,
            "p25": 0.90944444,
            "p50": 8.98333333,
            "p75": 35.04222222,
            "p100": 309.12305556
        },
        {
            "event_month": "2022-07-01",
            "p0": 0.01916667,
            "p25": 4.16694444,
            "p50": 17.28194444,
            "p75": 120.03305556,
            "p100": 9653.49861111
        },
        {
            "event_month": "2022-08-01",
            "p0": 0.40555556,
            "p25": 0.46388889,
            "p50": 0.47388889,
            "p75": 1.48055556,
            "p100": 4.03
        },
        {
            "event_month": "2022-09-01",
            "p0": 1.00944444,
            "p25": 1.42361111,
            "p50": 3.55805556,
            "p75": 1032.71583333,
            "p100": 4392.51027778
        },
        {
            "event_month": "2022-10-01",
            "p0": 0.06166667,
            "p25": 0.53305556,
            "p50": 5.35305556,
            "p75": 95.74944444,
            "p100": 12070.6375
        },
        {
            "event_month": "2022-11-01",
            "p0": 1063.17527778,
            "p25": null,
            "p50": 1063.17527778,
            "p75": 1063.17527778,
            "p100": 1063.17527778
        },
        {
            "event_month": "2023-01-01",
            "p0": 0.15944444,
            "p25": 0.3125,
            "p50": 399.7675,
            "p75": 3619.45611111,
            "p100": 13863.58194444
        },
        {
            "event_month": "2023-02-01",
            "p0": 9.37722222,
            "p25": 14.44861111,
            "p50": 18.66888889,
            "p75": 18.83222222,
            "p100": 3694.30833333
        },
        {
            "event_month": "2023-03-01",
            "p0": 0.01805556,
            "p25": 1.07361111,
            "p50": 192.99722222,
            "p75": 1529.00388889,
            "p100": 5039.46305556
        },
        {
            "event_month": "2023-04-01",
            "p0": 0.64722222,
            "p25": 0.64722222,
            "p50": 86.945,
            "p75": 95.64138889,
            "p100": 4837.55444444
        },
        {
            "event_month": "2023-06-01",
            "p0": 0.36694444,
            "p25": 0.36694444,
            "p50": 0.36694444,
            "p75": 6013.82472222,
            "p100": 6013.82472222
        },
        {
            "event_month": "2023-07-01",
            "p0": 0.33388889,
            "p25": 0.33388889,
            "p50": 12.85777778,
            "p75": 12.85777778,
            "p100": 55.07444444
        },
        {
            "event_month": "2023-08-01",
            "p0": 23.50138889,
            "p25": 2987.46277778,
            "p50": 3096.65027778,
            "p75": 6939.05861111,
            "p100": 13925.02611111
        },
        {
            "event_month": "2023-09-01",
            "p0": 1.00472222,
            "p25": 1.00472222,
            "p50": 646.23555556,
            "p75": 646.23555556,
            "p100": 8367.59194444
        },
        {
            "event_month": "2023-11-01",
            "p0": 20165.04888889,
            "p25": null,
            "p50": 20165.04888889,
            "p75": 20165.04888889,
            "p100": 20165.04888889
        }
    ],
    "expiresAt": "2024-01-11T08:09:41.288+00:00",
    "refresh": true
}'''
json_file = '../data/open-to-merged.json'
json_file_1 = '../data/number_pr.json'
label_conf = dict(size=20)
with open(json_file, 'r') as file: 
    a = json.load(file)
with open(json_file_1, 'r') as file:
    b = json.load(file)
num = [[],[],[],[],[]]
pr_number = []
time = []
labels = [f'p{25*j}' for j in range(5)]
for i in a["data"]:
    for j in range(5):
        num[j].append(i[labels[j]])
    t = np.datetime64(i["event_month"])
    if t <= np.datetime64("2023-11-01"):
        time.append(t)
for j in b["data"]:
    t = np.datetime64(j["event_month"])
    if t <= np.datetime64("2023-11-01"):
        pr_number.append(j['all_size'])
num = np.array(num)
num_df = pd.DataFrame(num)
# num_df = num_df.fillna(0)
num_df = num_df.infer_objects(copy=False)
new_time = []
for i in range(6):
    new_time.append(time[i*6])
new_time.append(time[-1])
new_num_df = pd.DataFrame()
new_num_df[0] = num_df.iloc[:,0]
new_num_df[1] = num_df.iloc[:,1:6].sum(axis=1)
for i in range(2,7):
    cur_df = num_df.iloc[:,6+6*(i-2):6+6*(i-2) + 6]
    r1 = cur_df.iloc[0].min()
    r2 = cur_df.iloc[1].mean()
    r3 = cur_df.iloc[2].mean()
    r4 = cur_df.iloc[3].mean()
    r5 = cur_df.iloc[4].max()
    s = pd.Series([r1,r2,r3,r4,r5])
    new_num_df[i] = s

x = [i for i in range(len(num))]
fig, ax = plt.subplots(figsize=(10,6), dpi=100)
plt.yscale("log")
new_num_df.loc[len(new_num_df)] = [10_0000 for _ in range(7)]
# print(new_num_df)
new_time = np.array(new_time)
ax.boxplot(new_num_df, positions=new_time.astype(int), widths=100, patch_artist=True,
            showmeans=False, showfliers=False,
            medianprops={"color": "white", "linewidth": 1.5},
            boxprops={"facecolor": "C0", "edgecolor": "white",
                        "linewidth": 0.5},
            whiskerprops={"color": "C0", "linewidth": 1.5},
            capprops={"color": "C0", "linewidth": 1.5})
ax.xaxis.set_major_formatter(mdates.DateFormatter('%y/%m'))
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=6))
ax.xaxis.set_minor_locator(mdates.MonthLocator(interval=3))
ax.tick_params(labelsize=20, size=10)
ax.tick_params(axis='x', rotation=0)
ax.set_xlabel("Time", **label_conf)
ax.set_ylabel("Reviewing time(h)", **label_conf)
ax.grid(axis='x', alpha=0.3)
# ax.legend(ncol=3, frameon=False, bbox_to_anchor=(0,1), loc='lower left',fontsize=18)
fig.savefig('../imgs/figure5_the_trend_of_RFL.pdf', bbox_inches='tight')