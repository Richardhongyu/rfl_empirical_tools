import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.dates import DateFormatter, date2num
import matplotlib.dates as mdates

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
    data = group_data_per_week(data)
    
    # 准备数据
    x = [mdates.date2num(x[0]) for x in data]
    y1 = [y[2] for y in data]  # Merged commits
    y2 = [y[1] + y[2] for y in data]  # Total commits
    
    # 创建图表
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # 绘制折线（不同颜色）
    line1, = ax.plot(x, y1, color='#1E90FF', linewidth=2, label='staged')
    line2, = ax.plot(x, y2, color='#EE82EE', linewidth=2, linestyle='--', label='under review')
    
    # 生成3个月间隔的日期点
    start_date = datetime(2020,9,1)
    end_date = datetime(2023, 7, 1)
    date_ticks_3month = pd.date_range(start=start_date, end=end_date, freq='3MS')  # 每3个月第一天
    
    # 转换为数值并筛选有效点
    x_ticks_3month = mdates.date2num(date_ticks_3month)
    valid_ticks = [tick for tick in x_ticks_3month if (tick >= min(x)) and (tick <= max(x))]
    
    # 找到最近的数据索引
    x_array = np.array(x)
    indices = [np.abs(x_array - tick).argmin() for tick in valid_ticks]
    
    # 绘制彩色点（与对应曲线颜色一致）
    ax.scatter(x_array[indices], np.array(y1)[indices],
               color=line1.get_color(), s=80, edgecolor='white', zorder=3,
               )
    ax.scatter(x_array[indices], np.array(y2)[indices],
               color=line2.get_color(), s=80, marker='s', edgecolor='white', zorder=3,
               )
    
    # 填充区域
    ax.fill_between(x, y1, y2, color='grey', alpha=0.2)
    
    # 坐标轴设置
    ax.set_ylabel("Number of Commits", fontsize=12)
    date_format = DateFormatter('%y/%m')
    ax.xaxis.set_major_formatter(date_format)
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=6))
    ax.xaxis.set_minor_locator(mdates.MonthLocator(interval=3))
    plt.xticks(rotation=0)
    
    # 图例设置
    ax.legend(ncol=2, fontsize=10, frameon=False, bbox_to_anchor=(0.5, 1.15),
              loc='upper center', borderaxespad=0.)
    
    # 保存图片
    plt.savefig('../imgs/figure5_the_trend_of_RFL.pdf', bbox_inches='tight')
    plt.close()