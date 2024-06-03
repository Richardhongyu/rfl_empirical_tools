# !pip install brewer2mpl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import matplotlib.ticker as ticker
#从pyplot导入MultipleLocator类，这个类用于设置刻度间隔
plt.rc('font',family='Times New Roman')

import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

fs = 30
# opBreakdown (percentage bar)

# op1 = np.array([1.86 * 29, 1.86 * 29 * 2, 34.02 * 29]) # compute
# op2 = np.array([110.01 * 4 * 2] * 3) # communicate 

# op1 = np.array([1.86 * 29, 1.86 * 29 * 2, 34.02 * 29, 40*29, 4*29, 8*29, 9*29, 10*29]) # compute
# print(op1.shape[0])
# op2 = np.array([110.01 * 4 * 2] *op1.shape[0]) # communicate 
# op3 = np.array([5 * 29, 3 * 29 * 2, 40 * 29, 40*29, 40*29, 40*29, 40*29, 40*29]) # compute
# print(op1.shape[0])
# op4 = np.array([20 * 29, 17 * 29 * 2, 60 * 29, 60*29, 60*29, 60*29, 60*29, 60*29]) # compute
# print(op1.shape[0])
# op5 = np.array([60 * 29, 31 * 29 * 2, 80 * 29, 80*29, 80*29, 80*29, 80*29, 80*29]) # compute

oop1 = np.array([39,77,102,195,419,1040,1436])
oop2 = np.array([40,46,61,97,116,202,384])
oop3 = np.array([122,144,199,303,437,507,595])
oop4 = np.array([6,6,6,8,21,31,35])
oop5 = np.array([0,0,0,4,19,174,192])
# op = [15,22,38,88,96,117,124]
# op = [0,0,0,0,6,14,15]
# op = [44,48,48,48,48,48,48]
# op = [376,413,466,509,539,644,677]

op1 = []
op2 = []
op3 = []
op4 = []
op5 = []



for i in range(0,7):
    if i !=0:
        op1.append(oop1[i]-oop1[i-1])
        op2.append(oop2[i]-oop2[i-1])
        op3.append(oop3[i]-oop3[i-1])
        op4.append(oop4[i]-oop4[i-1])
        op5.append(oop5[i]-oop5[i-1])
    else:
        op1.append(oop1[i])
        op2.append(oop2[i])
        op3.append(oop3[i])
        op4.append(oop4[i])
        op5.append(oop5[i])

op1.append(oop1[-1])
op2.append(oop2[-1])
op3.append(oop3[-1])
op4.append(oop4[-1])
op5.append(oop5[-1])

op1 = np.array(op1)
op2 = np.array(op2)
op3 = np.array(op3)
op4 = np.array(op4)
op5 = np.array(op5)

op1 = op1[::-1]
op2 = op2[::-1]
op3 = op3[::-1]
op4 = op4[::-1]
op5 = op5[::-1]


print(op1)
print(op2)
print(op3)
print(op4)
print(op5)

print(op1.shape[0])

op_sum = op1 + op2+op3+op4+op5

op1_regular = op1/op_sum*100
op2_regular = op2/op_sum*100
op3_regular = op3/op_sum*100
op4_regular = op4/op_sum*100
op5_regular = op5/op_sum*100

print(op1_regular)
print(op2_regular)
print(op3_regular)
print(op4_regular)
print(op5_regular)

devices = ["Overall", "23/7", "23/3", "23/1", "22/10", "22/7", "22/4", "22/1"] 
# color = ['red', 'blue', 'green', '#FF8C00', '#9370DB', 'hotpink']
color = ['grey', 'white', 'green', '#FF8C00', '#9370DB', 'hotpink']
# 横向
bottom = 0
plt.figure(figsize=(15,10))
ax = plt.axes()
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
plt.xlabel("Time", fontsize=fs)
plt.ylabel("Percentage(%)", fontsize=fs)
plt.ylim(0,100)
# plt.ylim(0,100,10)
plt.xticks(fontsize=fs)
plt.yticks(fontsize=fs)
plt.bar(devices, op1_regular, width=0.4, label="abstraction", color=color[0],edgecolor='black')

bottom = bottom + op1_regular

plt.bar(devices, op2_regular, width=0.4, label="drivers", color=color[3], bottom=bottom,edgecolor='black')

bottom = bottom + op2_regular

plt.bar(devices, op3_regular, width=0.4, label="build", color=color[5], bottom=bottom,edgecolor='black')

bottom = bottom + op3_regular

plt.bar(devices, op4_regular, width=0.4, label="bugs", color=color[4], bottom=bottom,edgecolor='black')

bottom = bottom + op4_regular

plt.bar(devices, op5_regular, width=0.4, label="rust", color=color[1], bottom=bottom,edgecolor='black')

bottom = bottom + op5_regular

# plt.bar(devices, op2_regular, width=0.4, label="rust", color=color[1], bottom=bottom,edgecolor='black')

plt.legend(fontsize=23, loc='upper center' , ncol=5, bbox_to_anchor=(0.45, 1.15), frameon=False)

plt.savefig('eval-preliminary-breakdown-v1.png', bbox_inches="tight")