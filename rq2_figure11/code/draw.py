import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
from matplotlib.pyplot import MultipleLocator
import matplotlib

# 全局字体设置
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

def dup(A, B):
    """生成重复值列表"""
    C = []
    if len(A) != len(B):
        return C
    for i in range(len(A)):
        times = A[i]
        for j in range(times):
            C.append(B[i])
    return C

# 数据准备（公共部分）
commit_count = [
    [29, 1, 4, 2, 11, 5, 3, 2, 3, 2, 0, 0, 0],
    [24, 8, 14, 33, 31, 33, 20, 21, 12, 16, 14, 21, 20],
    [3, 9, 7, 9, 15, 11, 7, 2, 4, 0, 1, 2, 1],
    [2, 3, 2, 1, 0, 4, 2, 0, 2, 1, 1, 2, 1]
]
time_line = [0,3,6,12,24,48,72,96,120,144,168,192,216,240]
labels = ["RFL", "netdev", "ebpf", "io_uring"]
category_names = ['novice', 'expert', 'veteran']

# 生成公共数据
dup_time_line = []
for counts in commit_count:
    dup_time_line.append(dup(counts, time_line[1:]))

young_index = 4
mid_index = 8
result = {}
for k, line in enumerate(commit_count):
    new_list = [
        np.sum(line[:young_index + 1]),
        np.sum(line[young_index:mid_index + 1]),
        np.sum(line[mid_index:])
    ]
    result[labels[k]] = new_list

# ========================= 绘制CDF图 =========================
fig1, ax = plt.subplots(figsize=(10, 6))  # 独立画布

# 绘制经验累积分布
for j, time_data in enumerate(dup_time_line):
    ax.ecdf(time_data, label=labels[j], lw=2.5)

# 坐标轴设置
ax.set_xlabel('Experience (month)', size=16)
ax.set_ylabel('CDF', size=16)
ax.tick_params(labelsize=14)
ax.yaxis.set_major_locator(MultipleLocator(0.2))
ax.yaxis.set_minor_locator(MultipleLocator(0.05))
ax.xaxis.set_major_locator(MultipleLocator(50))
ax.xaxis.set_minor_locator(MultipleLocator(25))
ax.grid(alpha=0.3)
ax.legend(ncol=2, frameon=False, fontsize=12, 
          loc='upper center', bbox_to_anchor=(0.2, 1))

# 保存CDF图
fig1.savefig('figure11_cdf.pdf', dpi=300, bbox_inches='tight')
plt.close(fig1)

# ====================== 绘制堆叠条形图 ========================
fig2, ax1 = plt.subplots(figsize=(10, 6))  # 独立画布

def survey(results, category_names, ax):
    """堆叠条形图绘制函数"""
    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    
    # 转换为百分比
    for i in range(data.shape[0]):
        total = data[i].sum()
        data_cum[i] = data_cum[i] * 100 / total
        data[i] = data[i] * 100 / total
    
    # 颜色与样式设置
    category_colors = plt.cm.gray(np.linspace(0.2, 0.8, 3))
    hatchs = ['', '////', '....']
    
    ax.invert_yaxis()
    ax.set_xlabel('Percentage (%)', size=16)
    ax.xaxis.set_major_locator(MultipleLocator(25))
    ax.xaxis.set_minor_locator(MultipleLocator(5))
    ax.set_xlim(0, 100)
    ax.tick_params(labelsize=12)
    
    # 绘制堆叠条
    for i, (colname, color, hatch) in enumerate(zip(category_names, category_colors, hatchs)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.barh(labels, widths, left=starts, height=0.5,
                        label=colname, color=color, hatch=hatch, edgecolor='black', linewidth=1)
        r,g,b,_ = color
        text_color = ['white', 'white', 'black'] 
        ax.bar_label(rects, label_type='center', color=text_color[i], size=15)
    ax.legend(ncols=3, bbox_to_anchor=(0.1, 1),
              loc='lower left', fontsize=18, frameon=False)
    ax.tick_params(labelsize=20)

# 调用绘图函数
survey(result, category_names, ax1)

# 保存堆叠条形图
fig2.savefig('figure11_stackbar.pdf', dpi=300, bbox_inches='tight')
plt.close(fig2)