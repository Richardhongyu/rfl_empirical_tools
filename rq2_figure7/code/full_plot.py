import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
import os

bar_conf = dict(edgecolor='black', linewidth=1)

once_legend = 0
def comma_formatter(x, pos):
    if abs(x) >= 1e9:
        return '{:.0f}B'.format(x / 1e9)
    elif abs(x) >= 1e6:
        return '{:.0f}M'.format(x / 1e6)
    elif abs(x) >= 1e3:
        return '{:.0f}K'.format(x / 1e3)
    else:
        return '{:,.0f}'.format(x)

with open("../data/data.txt", 'r') as f:
    data = f.read()
data = data.replace('\n', '').split('&')
rust = []
c = []
for d in data:
    d = d.strip().split('/')
    rust.append(eval(d[0]))
    c.append(eval(d[1]))

rust = np.array(rust).reshape(7,8)[:,:5]
c = np.array(c).reshape(7,8)[:,:5]
rust_column = np.sum(rust[:,3:5], axis=1)
c_column = np.sum(c[:,3:5], axis=1)
rust = np.column_stack((rust[:,:3], rust_column))
c = np.column_stack((c[:,:3], c_column))
print(f'rust: {rust[-3:]}')
print(f'c: {c[-3:]}')

driver_name = ['*NVME', '*nblk', '*e1000', 'binder', 'cpufreq-dt', 'gpio', 'sem']
binary_size = ['text', 'data', 'bss', 'debug']
color = ['black', 'silver', 'white', 'white']
hatch = ['', '', '', '//']

fig, axs = plt.subplots(7,2,dpi=100, sharey=True, figsize=(10,12))
fig.subplots_adjust(wspace=0.2, hspace=0.5)
labels = ['C','Rust']
y_pos = np.arange(len(labels))
d = .5  # proportion of vertical to horizontal extent of the slanted line
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle="none", color='k', mec='k', mew=1, clip_on=False)

x_lim_end_c = max(i[3] for i in c)
x_lim_end_rust = max(i[3] for i in rust)
x_lim_end = max(x_lim_end_c, x_lim_end_rust)
x_lim_c = max((i[0] for i in c))
x_lim_rust = max((i[0] for i in rust))
x_lim = max(x_lim_c, x_lim_rust)
for i in range(7):
    sum_c = np.sum(c[i][:3])
    sum_rust = np.sum(rust[i][:3])
    axs[i,0].set_xlim(0, x_lim * 1.1)
    axs[i,1].set_xlim(0, x_lim_end * 1.1)
    axs[i,0].set_yticks(y_pos, labels=labels, size=20)
    axs[i,0].set_ylabel(driver_name[i], size=20)
    axs[i,0].spines['right'].set_visible(False)
    axs[i,1].spines['left'].set_visible(False)
    axs[i,1].get_yaxis().set_visible(False)
    axs[i,0].plot([1, 1], [1, 0], transform=axs[i,0].transAxes, **kwargs)
    axs[i,1].plot([0, 0], [0, 1], transform=axs[i,1].transAxes, **kwargs)
    for j in range(2):
        left = np.zeros(2)
        ax = axs[i,j]
        ax.tick_params(axis='x',rotation=45, labelsize=14)
        ax.xaxis.set_major_formatter(FuncFormatter(comma_formatter))
        for k in range(4):
            if j == 0 and k == 3:
                break
            if j == 1:
                if once_legend == 0:
                    once_legend = 1
                    ax.barh(y_pos, [c[i][k],rust[i][k]], color = "white", label = "debug", left=left, hatch="//", **bar_conf)
                else:
                    ax.barh(y_pos, [c[i][k],rust[i][k]], color = color[k],  left=left, hatch=hatch[k], **bar_conf)
            else: 
                if once_legend == 0:
                    ax.barh(y_pos, [c[i][k],rust[i][k]], label = binary_size[k], left=left, color = color[k], hatch=hatch[k], **bar_conf)
                else:
                    ax.barh(y_pos, [c[i][k],rust[i][k]], left=left, color = color[k], hatch=hatch[k], **bar_conf)
                left += [c[i][k],rust[i][k]]
            ax.label_outer()

fig.legend( ncol=4, frameon=False, loc="lower left", bbox_to_anchor=(0.1, 0.9), fontsize=20, columnspacing=3, handletextpad=0.5)
script_name = os.path.basename(__file__).split('.')[0]
fig.savefig(f'../imgs/{script_name}.pdf', bbox_inches="tight")