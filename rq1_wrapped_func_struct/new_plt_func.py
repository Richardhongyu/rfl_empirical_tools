# !pip install brewer2mpl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
#从pyplot导入MultipleLocator类，这个类用于设置刻度间隔
plt.rc('font',family='Times New Roman')

import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

fs = 30
# opBreakdown (percentage bar)

# op1 = np.array([1.86 * 29, 1.86 * 29 * 2, 34.02 * 29]) # compute
# op2 = np.array([110.01 * 4 * 2] * 3) # communicate 
    # - sched && sync
    #   - 50/388
    # - mm
    #   - 10/1050
    # - file
    #   - 27/2760
    # - net
    #   - 21/4526
    # - driver
    #   - 36/8766
    # - clock && irq
    #   - 15/333
    # - security
    #   - 6/535
    # - others(sounds, trace, arch, lib, ipc)
    #   - 23/8073

op1 = np.array([188,50,10, 27, 21, 36, 15, 6, 23]) # compute
op2 = np.array([28805,388,1050,2760,4526,8766,333,535,8073]) # communicate
# op1 = np.array([71,13.0, 4.0, 15.0, 8.0, 18.0, 5.0, 1.0, 4.0]) # compute
print(op1.shape[0])
# op2 = np.array([19106,124,34,2139,2744,1280,87,196,12442]) # communicate 
# op3 = np.array([5 * 29, 3 * 29 * 2, 40 * 29, 40*29, 40*29, 40*29, 40*29, 40*29]) # compute
# print(op1.shape[0])
# op4 = np.array([20 * 29, 17 * 29 * 2, 60 * 29, 60*29, 60*29, 60*29, 60*29, 60*29]) # compute
# print(op1.shape[0])
# op5 = np.array([60 * 29, 31 * 29 * 2, 80 * 29, 80*29, 80*29, 80*29, 80*29, 80*29]) # compute
# print(op1.shape[0])

# op_sum = op1/op2

op_sum = op2

op1_regular = op1/op_sum*100
op2_regular = op2/op_sum*100
# op3_regular = op3/op_sum*100
# op4_regular = op4/op_sum*100
# op5_regular = op5/op_sum*100

print(op1_regular)
print(op2_regular)
# print(op3_regular)
# print(op4_regular)
# print(op5_regular)

devices = ["Overall", "sched", "mm", "file", "net", "driver", "irq&&clock", "security", "others"]
# devices = ["Overall", "23/7", "23/3", "23/1", "22/10", "22/7", "22/4", "22/1"]
color = ['grey', 'white', 'green', '#FF8C00', '#9370DB', 'hotpink']
# color = ['grey', 'white', 'green', '#FF8C00', '#9370DB', 'hotpink']
# 横向
bottom = 0
plt.figure(figsize=(15,10))
plt.xlabel("Classifacation", fontsize=fs)
plt.ylabel("Percentage", fontsize=fs)
plt.ylim(0,100)
# plt.rcParams['mathtext.fontset'] = 'cm'
plt.yscale('symlog')
plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.bar(devices, op1_regular, width=0.4, label="wrapped", color=color[0],edgecolor='black',)
plt.xticks(rotation=30) # 倾斜70度
bottom = bottom + op1_regular

# plt.bar(devices, op3_regular, width=0.4, label="c2", color=color[3], bottom=bottom,edgecolor='black')

# bottom = bottom + op3_regular

# plt.bar(devices, op4_regular, width=0.4, label="c3", color=color[4], bottom=bottom,edgecolor='black')

# bottom = bottom + op4_regular

# plt.bar(devices, op5_regular, width=0.4, label="c4", color=color[5], bottom=bottom,edgecolor='black')

# bottom = bottom + op5_regular

# plt.bar(devices, op2_regular, width=0.4, label="c5", color=color[1], bottom=bottom,edgecolor='black')

# bottom = bottom + op5_regular

# plt.bar(devices, op2_regular, width=0.4, label="c6", color=color[1], bottom=bottom,edgecolor='black')

# bottom = bottom + op5_regular

# plt.bar(devices, op2_regular, width=0.4, label="c7", color=color[1], bottom=bottom,edgecolor='black')

# bottom = bottom + op5_regular

plt.bar(devices, op2_regular, width=0.4, label="unwrapped", color=color[1], bottom=bottom,edgecolor='black',)

plt.legend(fontsize=23, loc=4, ncol=4, bbox_to_anchor=(0.8, 1), frameon=False)

plt.savefig('wrapped_func.png', bbox_inches="tight")