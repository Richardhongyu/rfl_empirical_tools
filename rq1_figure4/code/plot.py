with open('mid_value3', 'r') as f:
    a = f.read()

# help me generate the following data
# percentages = np.array([
#     [2.61628, 16.45435, 3.7037, 1.67364, 0, 0, 0],
#     [26.45349, 9.12951, 4.69136, 15.06276, 15.78947, 9.09091, 19.32367],
#     [12.7907,7.431,33.08642,43.51464,57.89474,33.33333,58.9372],
#     [0.5814, 1.06157, 3.20988, 0.83682, 0, 0, 2.89855],
#     [57.55814, 65.92357, 55.30864, 38.91213, 26.31579, 57.57576, 18.84058],
# ])

b = a.split("-----------------------------------------------------------")
blocks = []
for i in range(1,len(b)):
    print(b[i])
    print("-----------------------------------------------------------")
    lines = b[i].split("\n")
    for j, k in enumerate(lines):
        if "." in k:
            if i == 1:
                print(float(k))
                blocks.append([float(k)])
            else:
                blocks[j-1].append(float(k))
print(blocks)
import numpy as np
blocks = np.array(blocks)
blocks = blocks.T.T
print(blocks)
# make the blocks reverse in each row
blocks = blocks[:,::-1]
# change the order of row 0 and row 4
blocks[[0,4]] = blocks[[4,0]]


import matplotlib.pyplot as plt
import numpy as np
import time

label_font_conf = {
    # "weight": "bold",
    "size": "22"
}
# labels = ['rust', 'bugs', 'build', 'drivers', 'abstraction']
labels_1 = ['r', 'bugs', 'build', 'd', 'a']
labels_1 = ['rust', 'bugs', 'build', 'd', 'abstraction']
labels_2 = ['RFL', 'Review', 'Linux']
# 日期数据
dates = ['23/7', '23/4', '23/1', '22/10', '22/7', '22/4', '22/1']
dates.reverse()
# 对应的百分比数据
percentages = blocks
current_time = int(time.time())
np.random.seed(current_time)
process = np.random.rand(3, 7) * 60
# 创建画布和子图
fig, axs = plt.subplots(1, 1, figsize=(10,5),dpi=100)

# 绘制折线图
markers = ['o', '^', 'D', 's', 'v']
colors = ['b', 'r', 'g', 'y', 'purple']
for i, per in enumerate(percentages):
    per = per[::-1]
    if i != 3 and i !=1:
        axs.plot(dates, per, marker=markers[i], linestyle='-', color=colors[i], linewidth=1.5, label=labels_1[i], markersize=10)

# for i, pro in enumerate(process):
#     axs[1].plot(dates, pro, marker=markers[i], linestyle='-', color=colors[i], linewidth=1.5, label=labels_2[i], markersize=10)

# 设置横轴和纵轴标签
yticks = np.arange(0,100,20)
axs.set_xlabel('Time', **label_font_conf)
axs.set_ylabel('Patch Percentage (%)', **label_font_conf)
axs.set_yticks(yticks)
# axs.text(0.5, -0.5, '(a)', transform=axs.transAxes, fontsize=20, va='bottom', ha='center')
# axs[1].set_xlabel('Time', **label_font_conf)
# axs[1].set_ylabel('The Merged Process of RFL (%)', **label_font_conf)
# axs[1].set_yticks(yticks)
# axs[1].text(0.5, -0.5, '(b)', transform=axs[1].transAxes, fontsize=20, va='bottom', ha='center')

axs.grid(axis='y', alpha=0.3)
# axs[1].grid(axis='y', alpha=0.3)

axs.tick_params(labelsize=20)
# axs.tick_params(axis='x', rotation=45)
# axs[1].tick_params(labelsize=15)
# axs[1].tick_params(axis='x', rotation=45)
# axs[1].tick_params(axis='y', labelleft=False, left=False)

# 显示图形
plt.tight_layout()
# axs.legend(loc='lower left', ncol=5, bbox_to_anchor=(0, 1), frameon=False, columnspacing=2, fontsize=20)
axs.legend(loc='lower left', ncol=5, bbox_to_anchor=(0.1, 1), frameon=False, columnspacing=2, fontsize=20)
# axs[1].legend(loc='lower left', ncol=1, bbox_to_anchor=(0.1, 1), frameon=False, columnspacing=2, fontsize=20)
# plt.show()
plt.savefig('./figure4.pdf', bbox_inches="tight")
