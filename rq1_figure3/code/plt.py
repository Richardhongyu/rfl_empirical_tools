import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
from matplotlib.patches import ConnectionPatch

def plot(type):
    """
        type = 1 or 0
            - type = 1, use `ax.text()` draw the number upon the bar
            - type = 0, don't draw the number upon the bar
    """
    # 创建图的样式设置
    label_font_conf = {
        # "weight": "bold",
        "size": "22"
    }
    bar_confs = {
        "color": ["white", "silver"],
        "linewidth": 1,
        "hatch": ["//", ""],
        "edgecolor": "black",
    }
    bar_width = 0.05

    # 创建标签
    ylabel = "% of already wrapped"
    xlabels = ['sched', 'mm', 'irq&&clk', 'driver', 'file', 'net', 'security']
    x = [0.1, 0.1+bar_width*2.5]

    # 创建数据
    # The values is the old data, but the linux versions and config changes
    # values = np.array([
    #     [12.8866, 10.48387],
    #     [4.5045, 11.76471],
    #     [0.46399, 5.74713],
    #     [0.95238, 1.40625],
    #     [1.1215, 0.70126],
    #     [0.97826, 0.29155],
    #     [0.41068, 0.5102],
    # ])
    # The values is get from the bash script
    # first column: 
    # second column: 13/127, 4/34, 5/87, 18/1280, 15/2308, 8/2745, 1/196
    values = np.array([
        [0.15337423312883436*100, 0.10236220472440945*100]
        [0.011135857461024499*100, 0.11764705882352941*100]
        [0.0046686551679419016*100, 0.05747126436781609*100]
        [0.029469548133595286*100, 0.0140625*100]
        [0.011278195488721804*100, 0.006499133448873483*100]
        [0.005775577557755775*100, 0.0029143897996357013*100]
        [0.011342155009451797*100, 0.00510204081632653*100]
    ])

    # 创建1行7列的子图布局
    fig, axs = plt.subplots(1, 7, figsize=(12, 5), dpi=100)

    # 绘制柱状图
    # hatches = ['//', '']
    axs[0].set_ylabel(ylabel, **label_font_conf)
    for i, ax in enumerate(axs):
        ax.set_xlabel(xlabels[i], **label_font_conf)
        ax.set_xticks([])
        bars = ax.bar(x, values[i], width=0.08, **bar_confs)
        ax.set_xlim(min(x)-bar_width*2, max(x)+bar_width*2)
        
        # 为每个柱子设置不同的条纹样式
        # for j, bar in enumerate(bars):
        #     bar.set_hatch(hatches[j])  
        # 在柱子上添加数据标签
        if type == 1:
            for j, bar in enumerate(ax.patches):
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width() / 2, height*1.2, f'{height:.1f}', ha='center', va='bottom', rotation=90, size=18)
        
        # 设置y轴为对数比例尺
        ax.set_yscale('log')
        # 设置y轴刻度
        ax.set_yticks([100, 10, 1, 0.1])
        if i != 0:
            ax.tick_params(axis='y',left=False, which='both', labelleft=False)

        ax.grid(axis='y', alpha=0.3)
        ax.tick_params(labelsize=18)

    # 设置图例
    bars = axs[0].containers[0].get_children()
    labels = ['Wrapped Functions', 'Wrapped Structs']
    axs[0].legend(bars, labels, ncol=2, loc="lower left", bbox_to_anchor=(1, 1), frameon=False, fontsize=20, columnspacing=2, handletextpad=0.5)

    func = ConnectionPatch(xyA=(min(x)-bar_width*2,0.65266), xyB=(max(x)+bar_width*2,0.65266), coordsA="data", coordsB="data", axesA=axs[0], axesB=axs[6], color="red", linestyle='--')
    axs[6].add_artist(func)
    struct = ConnectionPatch(xyA=(min(x)-bar_width*2,0.37161), xyB=(max(x)+bar_width*2,0.37161), coordsA="data", coordsB="data", axesA=axs[0], axesB=axs[6], color="blue", linestyle='--')
    axs[6].add_artist(struct)
    plt.text(max(x)+bar_width*2+0.05, 0.74, 'func avg\n0.65', fontsize=18, color='red', va='center', ha='left')
    plt.text(max(x)+bar_width*2+0.05, 0.3, 'structs avg\n0.37', fontsize=18, color='blue', va='center', ha='left')

    plt.subplots_adjust(wspace=0.3)
    # plt.show()
    fig.supxlabel('Linux Subsystems', size=20, y=-.05)
    plt.savefig('./figure3.pdf', bbox_inches="tight")

if __name__ == '__main__':
    plot(1)