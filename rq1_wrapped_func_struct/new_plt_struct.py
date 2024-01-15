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

# (15+8+18)/(13+4+15+8+18+5+1+4)

# op1 = np.array([1.86 * 29, 1.86 * 29 * 2, 34.02 * 29]) # compute
# op2 = np.array([110.01 * 4 * 2] * 3) # communicate 
    # - sched && sync
    #   - 13/124
    # - mm
    #   - 4/34
    # - file
    #   - 15/2139
    # - net
    #   - 8/2744
    # - driver
    #   - 18/1280
    # - clock && irq
    #   - 5/87
    # - security
    #   - 1/196
    # - others(sounds, trace, arch, lib, ipc)
    #   - 4/(19106-6664)=4/12442

# new results
    # - mm
    #   - 4/34
    # - sched && sync
    #   - 13/124
    # - clock && irq
    #   - 5/87
    # - driver
    #   - 18/1280
    # - file
    #   - 15/2139
    # - security
    #   - 1/196
    # - net
    #   - 8/2744
    # - others(sounds, trace, arch, lib, ipc)
    #   - 4/(19106-6664)=4/12442

# op1 = np.array([71,13.0, 4.0, 15.0, 8.0, 18.0, 5.0, 1.0, 4.0]) # compute

op1 = np.array([71,4,13,5,18,15,1,8,4,]) # new
# op1 = np.array([71, 13,15,4,5,8,1,18,4,])
print(op1.shape[0])
# op2 = np.array([19106,124,34,2139,2744,1280,87,196,12442]) # communicate 

op2 = np.array([19106, 34,124,87,1280,2139,196,2744,12442,]) # new

# op2 = np.array([19106, 124,2139,34,87,2744,196,1280,12442,])
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

devices = ["Overall", "mm","sched", "irq&&clock", "driver","file", "security","net", "others"]
# devices = ["Overall", "mm","sched", "file",  "irq&&clock", "net", "security", "driver", "others"]
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

plt.xticks(rotation=30) # 倾斜70度
# bottom = bottom + op1_regular

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
# bottom=bottom
plt.bar(devices, op2_regular, width=0.4, label="unwrapped", color=color[1], bottom=0, edgecolor='black',)
plt.bar(devices, op1_regular, width=0.4, label="wrapped", color=color[0],edgecolor='black',)

plt.legend(fontsize=23, loc=4, ncol=4, bbox_to_anchor=(0.8, 1), frameon=False)

plt.savefig('wrapped_structers.png', bbox_inches="tight")