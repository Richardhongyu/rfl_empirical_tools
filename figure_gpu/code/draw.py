import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
import os
import pandas as pd

bar_conf = dict(edgecolor='black', linewidth=1)

def comma_formatter(x, pos):
    if abs(x) >= 1e9:
        return '{:.1f}B'.format(x / 1e9)
    elif abs(x) >= 1e6:
        return '{:.1f}M'.format(x / 1e6)
    elif abs(x) >= 1e3:
        return '{:.1f}K'.format(x / 1e3)
    else:
        return '{:.1f}'.format(x)

# 读取CSV文件
data = pd.read_csv('../data/data.csv')
columns = data.columns[1:]  # 排除Type列
rust_data = data[data['Type'] == 'Rust'].iloc[0, 1:].values
c_data = data[data['Type'] == 'C'].iloc[0, 1:].values

# 处理列名，分离标题和单位
def split_column_name(col):
    if ('(' in col):
        main_title = col.split('(')[0].strip()
        unit = f'({col.split("(")[1]}'
        return main_title, unit
    return col, ''

fig, axs = plt.subplots(1, len(columns), dpi=100, figsize=(24, 4))
fig.subplots_adjust(wspace=0.4, hspace=0.2)
labels = ['C','Rust']
y_pos = np.array([0, 1])

for i, (col, ax) in enumerate(zip(columns, axs)):
    # 设置双行标签
    main_title, unit = split_column_name(col)
    xlabel_text = main_title + '\n' + unit if unit else main_title
    
    # 计算最大值并设置y轴范围
    max_value = max(c_data[i], rust_data[i])
    ax.set_ylim(0, max_value * 1.05)
    
    ax.set_xticks(y_pos, labels=labels, size=16)  # 横坐标标签改为16
    ax.set_xlabel(xlabel_text, size=16)  # 子图标签改为18
    ax.spines['top'].set_visible(False)
    ax.tick_params(axis='y', rotation=0, labelsize=12)  # 从10改为12
    ax.yaxis.set_major_formatter(FuncFormatter(comma_formatter))
    
    # 设置柱状图的宽度
    bar_width = 0.6  # 从0.8改为0.6
    
    # 绘制柱状图，保持原有的颜色和样式
    ax.bar(y_pos, [c_data[i], rust_data[i]], width=bar_width, 
           color=['silver', 'black'], **bar_conf)
    
    ax.set_xlim(-0.6, 1.6)

# 保存图表
script_name = os.path.basename(__file__).split('.')[0]
fig.savefig(f'../imgs/mac_m1.pdf', bbox_inches="tight")
print("end")