import numpy
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator

def extract_data(data_file):
    # [(date_time, commit_number)]
    data = []
    with open(data_file, 'r') as f:
        for line in f.readlines():
            line = line[1:-2].split(',')
            pr_index, pr_date, commits, is_merged = line[0].strip("\'"), line[1].strip().strip("\'"), int(line[2].strip()), line[3].strip()
            format_string = '%Y-%m-%dT%H:%M:%SZ'
            pr_date = datetime.strptime(pr_date, format_string)
            is_merged = True if is_merged == 'True' else False
            if commits < 100:
                data.append((pr_date, int(commits), is_merged, pr_index))
    data.sort(key=lambda x: x[0])
    return data

def group_data_per_week(data):
    # sum commits within 1 day
    start_date = data[0][0]
    end_date = datetime(2023, 7, 1)
    time_list = pd.date_range(start=start_date, end=end_date, freq=pd.to_timedelta('1D'))
    grouped_data = []
    for i, time in enumerate(time_list):
        no_merged_number = 0
        merged_number = 0
        if i == 0:
            for date, commits, is_merged, _ in data:
                if date <= time:
                    if not is_merged:
                        no_merged_number += commits
                    else:
                        merged_number += commits
                else:
                    break
            grouped_data.append((time, no_merged_number, merged_number))
        else:
            for date, commits, is_merged, _ in data:
                if date > time_list[i-1] and date < time:
                    no_merged_number = grouped_data[len(grouped_data) - 1][1]
                    merged_number = grouped_data[len(grouped_data) - 1][2]
                    if not is_merged:
                        no_merged_number += commits
                    else:
                        merged_number += commits
                    grouped_data.append((time, no_merged_number, merged_number))
                elif date > time:
                    break
    return grouped_data

if __name__ == '__main__':
    file = '../data/data.txt'
    data = extract_data(file)

    # Comment code are used to debug
    # print(len(data))
    # print(sum([i[1] for i in data]))
    # print(sum([i[1] for i in list(filter(lambda x:x[1] > 10, data))]))
    # for i in list(filter(lambda x:x[1] > 10, data)):
    #     print(i[3], i[1])
    # print(list(filter(lambda x:x[2], data)))
    # print(list(filter(lambda x:not x[2], data)))
    # print(len(list(filter(lambda x:x[2], data))))
    
    data = group_data_per_week(data)
    # print(list(filter(lambda x: x[0] > datetime(2022,3,1) and x[0] < datetime(2023,1,1), data)))
    x = [mdates.date2num(x[0]) for x in data]
    y1 = [y[2] for y in data]
    y2 = [y[1] + y[2] for y in data]
    fig, ax = plt.subplots()
    ax.plot(x, y1, color='darkblue', label='staged', linewidth=2.5)
    ax.plot(x, y2, color='red', label='under review', linewidth=2.5)
    ax.fill_between(x, y1, y2, color='grey', alpha=0.3)
    ax.set_ylabel("Number of Commits", fontsize=16)
    ax.set_xlabel("Time", fontsize=16)
    ax.legend(frameon=False, fontsize=16)
    date_format = DateFormatter('%y/%m')  # 设置时间格式
    ax.xaxis.set_major_formatter(date_format)
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=6))  
    ax.xaxis.set_minor_locator(mdates.MonthLocator(interval=3))  
    ax.grid(axis='x', alpha=0.3)
    plt.tick_params(rotation=0, labelsize=16)
    plt.savefig('../imgs/figure5_the_trend_of_RFL.pdf', bbox_inches='tight')